from .models import SearchRequest, SearchResponse, SourceCandidate


def build_search_response(request: SearchRequest) -> SearchResponse:
    filters = {k: v for k, v in request.filters.model_dump().items() if v is not None}
    location = request.filters.location or "global"
    schema_type = request.filters.schema_type or "Thing"
    query_slug = request.query.strip().lower().replace(" ", "_")

    sources = [
        SourceCandidate(
            label="Official site",
            url="https://findr.openautonomyx.com",
            source_tier=1,
            trust_score=0.98,
        )
    ]

    summary = (
        f"Stub search result for '{request.query}' using {request.depth_mode} mode"
        f" with location context '{location}'."
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
        trace={
            "query": request.query,
            "search_mode": request.search_mode,
            "depth_mode": request.depth_mode,
            "filters": filters,
            "ranking_factors": ["source_tier", "trust_score", "location"],
        },
    )
