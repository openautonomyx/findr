from typing import Any, Literal

from pydantic import BaseModel, Field


DepthMode = Literal[
    "fast pass",
    "standard",
    "deep research",
    "graph traversal",
    "crawl everything",
    "sherlock deduction",
]


class SearchFilters(BaseModel):
    location: str | None = None
    time: str | None = None
    source_tier: int | None = Field(default=None, ge=1, le=4)
    schema_type: str | None = None


class SearchRequest(BaseModel):
    query: str = Field(min_length=1)
    search_mode: str = "standard_search"
    depth_mode: DepthMode = "fast pass"
    filters: SearchFilters = Field(default_factory=SearchFilters)
    include_trace: bool = True


class SourceCandidate(BaseModel):
    label: str
    url: str
    source_tier: int
    trust_score: float
    provider: str


class ProviderPlan(BaseModel):
    provider: str
    reason: str
    priority: int


class SearchTrace(BaseModel):
    query: str
    search_mode: str
    depth_mode: str
    filters: dict[str, Any]
    selected_providers: list[ProviderPlan]
    ranking_factors: list[str]


class SearchResponse(BaseModel):
    search_mode: str
    schema_type: str
    summary: str
    schema_record: dict[str, Any]
    knowledge_graph: dict[str, Any]
    sources: list[SourceCandidate]
    trace: SearchTrace | None = None
