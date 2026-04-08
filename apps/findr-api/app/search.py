from .models import SearchRequest, SearchResponse, SearchTrace
from .providers import select_providers, stub_sources_for_providers


def build_search_response(request: SearchRequest) -> SearchResponse:
    filters = {k: v for k, v in request.filters.model_dump().items() if v is not None}
    location = request.filters.location or "global"
    schema_type = request.filters.schema_type or "Thing"
    query_slug = request.query.strip().lower().replace(" ", "_")
    plans = select_providers(request)

    sources = stub_sources_for_providers(plans)

    summary = (
        f"Stub search result for '{request.query}' using {request.depth_mode} mode"
        f" with location context '{location}' via {', '.join(plan.provider for plan in plans)}."
    )

    return SearchResponse(
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
                {"id": "source:official", "label": "Official site", "type": "Source"},
            ],
            "edges": [
                {
                    "from": f"thing:{query_slug}",
                    "to": "source:official",
                    "type": "documented_by",
                }
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
        )
        if request.include_trace
        else None,
    )
