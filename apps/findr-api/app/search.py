from .models import SearchRequest, SearchResponse, SearchTrace
from .providers import resolve_provider_sources, select_providers
from .storage import SearchStorage


def build_search_response(request: SearchRequest) -> SearchResponse:
    storage = SearchStorage.from_settings()
    cached = storage.get_cached(request)
    if cached:
        if cached.trace:
            cached.trace.cache_status = "hit"
            if cached.trace.storage_status is not None:
                cached.trace.storage_status["cache"] = "hit"
        return cached

    filters = {k: v for k, v in request.filters.model_dump().items() if v is not None}
    location = request.filters.location or "global"
    schema_type = request.filters.schema_type or "Thing"
    query_slug = request.query.strip().lower().replace(" ", "_")
    plans = select_providers(request)
    sources = resolve_provider_sources(request, plans)

    summary = (
        f"Search result for '{request.query}' using {request.depth_mode} mode"
        f" with location context '{location}' via {', '.join(plan.provider for plan in plans)}."
    )

    storage_status = {
        "cache": "configured" if storage.redis_client else "not_configured",
        "surrealdb": "persisted" if False else "pending",
        "opensearch": "indexed" if False else "pending",
    }

    response = SearchResponse(
        search_mode=request.search_mode,
        schema_type=schema_type,
        summary=summary,
        schema_record={
            "schema_type": schema_type,
            "name": request.query,
            "filters": filters,
            "canonical_id": f"thing:{query_slug}",
        },
        knowledge_graph={
            "nodes": [
                {"id": f"thing:{query_slug}", "label": request.query, "type": schema_type},
                *[
                    {"id": f"source:{index}", "label": source.label, "type": "Source"}
                    for index, source in enumerate(sources, start=1)
                ],
            ],
            "edges": [
                {
                    "from": f"thing:{query_slug}",
                    "to": f"source:{index}",
                    "type": "documented_by",
                }
                for index, _ in enumerate(sources, start=1)
            ],
        },
        sources=sources,
        trace=SearchTrace(
            query=request.query,
            search_mode=request.search_mode,
            depth_mode=request.depth_mode,
            filters=filters,
            selected_providers=plans,
            ranking_factors=["provider_priority", "source_tier", "trust_score", "location"],
            cache_status="miss",
            storage_status=storage_status,
        )
        if request.include_trace
        else None,
    )

    persisted = storage.persist_search(request, response)
    indexed = storage.index_search(request, response)
    if response.trace:
        response.trace.storage_status = {
            "cache": "pending",
            "surrealdb": "stored" if persisted else "unavailable",
            "opensearch": "indexed" if indexed else "unavailable",
        }
    cached_ok = storage.set_cached(request, response)
    if response.trace:
        response.trace.storage_status["cache"] = "stored" if cached_ok else "unavailable"
    return response
