from __future__ import annotations

from dataclasses import dataclass
from typing import Optional
from urllib.parse import quote, urlparse

import httpx

from .config import settings
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
            ProviderPlan(provider="wikipedia", reason="default topic-capable public source", priority=1)
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


def resolve_provider_sources(request: SearchRequest, plans: list[ProviderPlan]) -> list[SourceCandidate]:
    sources: list[SourceCandidate] = []
    with httpx.Client(timeout=settings.request_timeout_seconds, follow_redirects=True) as client:
        for plan in plans:
            if plan.provider == "wikipedia":
                sources.extend(fetch_wikipedia_sources(client, request.query))
            elif plan.provider == "programmable_search":
                sources.extend(fetch_programmable_search_sources(client, request.query))
            elif plan.provider == "official_web":
                sources.extend(fetch_official_web_sources(client, request.query))
            elif plan.provider == "google_maps":
                sources.extend(build_catalog_source("google_maps"))
            elif plan.provider == "g2":
                sources.extend(build_catalog_source("g2"))
            elif plan.provider == "linkedin":
                sources.extend(build_catalog_source("linkedin"))
            elif plan.provider == "logs":
                sources.extend(build_catalog_source("logs"))

    return dedupe_sources(sources)


def fetch_wikipedia_sources(client: httpx.Client, query: str) -> list[SourceCandidate]:
    title = quote(query.replace(" ", "_"))
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
    try:
        response = client.get(url)
        response.raise_for_status()
        payload = response.json()
    except Exception:
        return []

    page_url = payload.get("content_urls", {}).get("desktop", {}).get("page")
    if not page_url:
        return []
    return [
        SourceCandidate(
            label=payload.get("title", "Wikipedia"),
            url=page_url,
            source_tier=2,
            trust_score=0.78,
            provider="wikipedia",
            snippet=payload.get("extract"),
        )
    ]


def fetch_programmable_search_sources(client: httpx.Client, query: str) -> list[SourceCandidate]:
    if not settings.programmable_search_api_key or not settings.programmable_search_engine_id:
        return []

    try:
        response = client.get(
            "https://customsearch.googleapis.com/customsearch/v1",
            params={
                "key": settings.programmable_search_api_key,
                "cx": settings.programmable_search_engine_id,
                "q": query,
            },
        )
        response.raise_for_status()
        payload = response.json()
    except Exception:
        return []

    items = payload.get("items", [])[:3]
    return [
        SourceCandidate(
            label=item.get("title", item.get("link", "Search result")),
            url=item["link"],
            source_tier=2,
            trust_score=0.8,
            provider="programmable_search",
            snippet=item.get("snippet"),
        )
        for item in items
        if item.get("link")
    ]


def fetch_official_web_sources(client: httpx.Client, query: str) -> list[SourceCandidate]:
    domain = normalize_domain(query)
    if not domain:
        return []

    url = f"https://{domain}"
    try:
        response = client.get(url)
        response.raise_for_status()
    except Exception:
        return []

    return [
        SourceCandidate(
            label=domain,
            url=str(response.url),
            source_tier=1,
            trust_score=0.98,
            provider="official_web",
            snippet=response.text[:200].strip() if response.text else None,
        )
    ]


def build_catalog_source(provider: str) -> list[SourceCandidate]:
    catalog: dict[str, ProviderDefinition] = {
        "google_maps": ProviderDefinition(
            name="Google Maps",
            reason="place and map data",
            priority=1,
            source_tier=1,
            trust_score=0.95,
            url="https://maps.google.com",
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
    }
    definition = catalog.get(provider)
    if not definition:
        return []
    return [
        SourceCandidate(
            label=definition.name,
            url=definition.url,
            source_tier=definition.source_tier,
            trust_score=definition.trust_score,
            provider=provider,
            snippet=definition.reason,
        )
    ]


def dedupe_sources(sources: list[SourceCandidate]) -> list[SourceCandidate]:
    deduped: dict[str, SourceCandidate] = {}
    for source in sources:
        deduped.setdefault(source.url, source)
    return list(deduped.values())


def normalize_domain(query: str) -> Optional[str]:
    text = query.strip()
    if "://" in text:
        parsed = urlparse(text)
        return parsed.netloc or None
    if "." in text and " " not in text:
        return text.removeprefix("www.")
    return None
