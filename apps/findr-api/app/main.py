from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .models import SearchRequest, SearchResponse
from .search import build_search_response
from .storage import StorageTargets, storage_health

app = FastAPI(title=settings.api_title, version=settings.api_version)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get(f"{settings.api_prefix}/health/storage")
def health_storage() -> dict[str, str]:
    return storage_health(
        StorageTargets(
            surrealdb_url=settings.surrealdb_url,
            opensearch_url=settings.opensearch_url,
            redis_url=settings.redis_url,
        )
    ).model_dump()


@app.post(f"{settings.api_prefix}/search", response_model=SearchResponse)
def search(request: SearchRequest) -> SearchResponse:
    return build_search_response(request)
