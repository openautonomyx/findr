from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
from uuid import uuid4

from .models import LogEvent, LogIngestRequest, LogIngestResponse, SourceCandidate
from .storage import SearchStorage


def ingest_logs(request: LogIngestRequest) -> LogIngestResponse:
    case_id = request.case_id or f"case-{uuid4().hex[:12]}"
    events = [_normalize_event(event) for event in request.events]
    severity_counts = Counter(event.severity for event in events)
    source_counts = Counter(event.source for event in events)
    sources = _build_sources(source_counts)
    knowledge_graph = _build_graph(case_id, events)

    response = LogIngestResponse(
        case_id=case_id,
        accepted=len(events),
        summary=_build_summary(case_id, events, severity_counts),
        schema_record={
            "schema_type": "LogIngest",
            "case_id": case_id,
            "event_count": len(events),
            "severity_counts": dict(severity_counts),
            "source_counts": dict(source_counts),
            "first_seen": min((event.timestamp for event in events if event.timestamp), default=None),
            "last_seen": max((event.timestamp for event in events if event.timestamp), default=None),
        },
        knowledge_graph=knowledge_graph,
        sources=sources,
        storage_status={
            "surrealdb": "pending",
            "opensearch": "pending",
        },
        trace={
            "case_id": case_id,
            "event_types": sorted({event.event_type for event in events}),
            "actor_count": len({event.actor for event in events if event.actor}),
            "target_count": len({event.target for event in events if event.target}),
        }
        if request.include_trace
        else None,
    )

    storage = SearchStorage.from_settings()
    persisted = storage.persist_log_ingest(case_id, events, response)
    indexed = storage.index_log_ingest(case_id, events, response)
    response.storage_status = {
        "surrealdb": "stored" if persisted else "unavailable",
        "opensearch": "indexed" if indexed else "unavailable",
    }
    return response


def _normalize_event(event: LogEvent) -> LogEvent:
    timestamp = event.timestamp or datetime.now(timezone.utc).isoformat()
    return event.model_copy(
        update={
            "source": event.source.strip(),
            "event_type": event.event_type.strip(),
            "message": event.message.strip(),
            "timestamp": timestamp,
            "actor": event.actor.strip() if event.actor else None,
            "target": event.target.strip() if event.target else None,
        }
    )


def _build_summary(
    case_id: str,
    events: list[LogEvent],
    severity_counts: Counter[str],
) -> str:
    most_common = ", ".join(
        f"{severity}={count}" for severity, count in severity_counts.most_common()
    )
    return f"Ingested {len(events)} log events into {case_id}; severity mix: {most_common}."


def _build_sources(source_counts: Counter[str]) -> list[SourceCandidate]:
    return [
        SourceCandidate(
            label=source,
            url=f"log://{source}",
            source_tier=1,
            trust_score=0.97,
            provider="logs",
            snippet=f"{count} event{'s' if count != 1 else ''} ingested",
        )
        for source, count in sorted(source_counts.items())
    ]


def _build_graph(case_id: str, events: list[LogEvent]) -> dict[str, list[dict[str, str]]]:
    nodes: dict[str, dict[str, str]] = {
        f"case:{case_id}": {"id": f"case:{case_id}", "label": case_id, "type": "Case"}
    }
    edges: list[dict[str, str]] = []

    for index, event in enumerate(events, start=1):
        event_id = f"event:{case_id}:{index}"
        nodes[event_id] = {
            "id": event_id,
            "label": event.event_type,
            "type": "LogEvent",
        }
        edges.append({"from": f"case:{case_id}", "to": event_id, "type": "contains"})

        if event.actor:
            actor_id = f"actor:{event.actor}"
            nodes.setdefault(actor_id, {"id": actor_id, "label": event.actor, "type": "Actor"})
            edges.append({"from": actor_id, "to": event_id, "type": "performed"})

        if event.target:
            target_id = f"target:{event.target}"
            nodes.setdefault(target_id, {"id": target_id, "label": event.target, "type": "Target"})
            edges.append({"from": event_id, "to": target_id, "type": "affected"})

    return {"nodes": list(nodes.values()), "edges": edges}
