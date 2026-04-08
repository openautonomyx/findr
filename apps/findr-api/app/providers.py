from __future__ import annotations

from dataclasses import dataclass

from .models import ProviderPlan, SearchRequest, SourceCandidate


@dataclass(frozen=True)
class ProviderDefinition:
    name: str
    reason: str
    priority: int
    source_tier: int
    trust_score: float
    url: str


def select_providers(request: SearchRequest) -> list[ProviderPlan]:
    query = request.query.lower()
    plans: list[ProviderPlan] = []

    if any(keyword in query for keyword in ("nearby", "hotel", "place", "map", "local")):
        plans.append(
            ProviderPlan(provider="google_maps", reason="local and place-oriented query", priority=1)
        )
    if any(keyword in query for keyword in ("topic", "history", "what is", "wikipedia")):
        plans.append(
            ProviderPlan(provider="wikipedia", reason="topic-orientation query", priority=1)
        )
    if any(keyword in query for keyword in ("company", "product", "software", "saas", "review")):
        plans.append(
            ProviderPlan(provider="official_web", reason="official company or product lookup", priority=1)
        )
        plans.append(
            ProviderPlan(provider="g2", reason="product comparison or review context", priority=2)
        )
    if any(keyword in query for keyword in ("person", "employee", "linkedin", "profile")):
        plans.append(
            ProviderPlan(provider="linkedin", reason="people or employment context", priority=1)
        )
    if any(keyword in query for keyword in ("log", "audit", "workflow", "access", "network")):
        plans.append(
            ProviderPlan(provider="logs", reason="log or audit evidence requested", priority=1)
        )

    if not plans:
        plans.append(
            ProviderPlan(provider="official_web", reason="default official web routing", priority=1)
        )
        plans.append(
            ProviderPlan(
                provider="programmable_search",
                reason="fallback general web routing",
                priority=2,
            )
        )

    deduped: dict[str, ProviderPlan] = {}
    for plan in sorted(plans, key=lambda item: item.priority):
        deduped.setdefault(plan.provider, plan)
    return list(deduped.values())


def stub_sources_for_providers(plans: list[ProviderPlan]) -> list[SourceCandidate]:
    catalog: dict[str, ProviderDefinition] = {
        "google_maps": ProviderDefinition(
            name="Google Maps",
            reason="place and map data",
            priority=1,
            source_tier=1,
            trust_score=0.95,
            url="https://maps.google.com",
        ),
        "wikipedia": ProviderDefinition(
            name="Wikipedia",
            reason="topic orientation",
            priority=1,
            source_tier=2,
            trust_score=0.78,
            url="https://www.wikipedia.org",
        ),
        "official_web": ProviderDefinition(
            name="Official Web",
            reason="first-party source",
            priority=1,
            source_tier=1,
            trust_score=0.98,
            url="https://findr.openautonomyx.com",
        ),
        "g2": ProviderDefinition(
            name="G2",
            reason="product comparison",
            priority=2,
            source_tier=2,
            trust_score=0.82,
            url="https://www.g2.com",
        ),
        "linkedin": ProviderDefinition(
            name="LinkedIn",
            reason="employment and profile context",
            priority=1,
            source_tier=2,
            trust_score=0.84,
            url="https://www.linkedin.com",
        ),
        "logs": ProviderDefinition(
            name="Log Evidence",
            reason="user-provided or authorized logs",
            priority=1,
            source_tier=1,
            trust_score=0.97,
            url="https://www.openautonomyx.com/web/findr",
        ),
        "programmable_search": ProviderDefinition(
            name="Programmable Search",
            reason="general structured web search",
            priority=2,
            source_tier=2,
            trust_score=0.8,
            url="https://programmablesearchengine.google.com",
        ),
    }

    sources: list[SourceCandidate] = []
    for plan in plans:
        definition = catalog.get(plan.provider)
        if not definition:
            continue
        sources.append(
            SourceCandidate(
                label=definition.name,
                url=definition.url,
                source_tier=definition.source_tier,
                trust_score=definition.trust_score,
                provider=plan.provider,
            )
        )
    return sources
