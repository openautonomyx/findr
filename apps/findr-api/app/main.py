from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .models import SearchRequest, SearchResponse
from .search import build_search_response

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


@app.post(f"{settings.api_prefix}/search", response_model=SearchResponse)
def search(request: SearchRequest) -> SearchResponse:
    return build_search_response(request)
