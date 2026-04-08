from fastapi import FastAPI

from .config import settings
from .models import SearchRequest, SearchResponse
from .search import build_search_response

app = FastAPI(title=settings.api_title, version=settings.api_version)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post(f"{settings.api_prefix}/search", response_model=SearchResponse)
def search(request: SearchRequest) -> SearchResponse:
    return build_search_response(request)
