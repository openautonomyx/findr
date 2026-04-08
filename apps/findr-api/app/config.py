import os

from typing import Optional

from pydantic import BaseModel


class Settings(BaseModel):
    api_title: str = "AutonomyX Finder API"
    api_version: str = "0.1.0"
    api_prefix: str = "/o/findr-api"
    allowed_origins: list[str] = [
        "http://localhost:5173",
        "http://localhost:3000",
        "https://www.openautonomyx.com",
    ]
    surrealdb_url: Optional[str] = None
    opensearch_url: Optional[str] = None
    redis_url: Optional[str] = None
    surrealdb_namespace: str = "findr"
    surrealdb_database: str = "findr"
    surrealdb_user: str = "root"
    surrealdb_password: str = "root"
    opensearch_index: str = "findr-search"
    redis_ttl_seconds: int = 300
    request_timeout_seconds: float = 10.0
    programmable_search_api_key: Optional[str] = None
    programmable_search_engine_id: Optional[str] = None


settings = Settings(
    api_title=os.getenv("API_TITLE", "AutonomyX Finder API"),
    api_version=os.getenv("API_VERSION", "0.1.0"),
    surrealdb_url=os.getenv("SURREALDB_URL"),
    opensearch_url=os.getenv("OPENSEARCH_URL"),
    redis_url=os.getenv("REDIS_URL"),
    surrealdb_namespace=os.getenv("SURREALDB_NAMESPACE", "findr"),
    surrealdb_database=os.getenv("SURREALDB_DATABASE", "findr"),
    surrealdb_user=os.getenv("SURREALDB_USER", "root"),
    surrealdb_password=os.getenv("SURREALDB_PASSWORD", "root"),
    opensearch_index=os.getenv("OPENSEARCH_INDEX", "findr-search"),
    redis_ttl_seconds=int(os.getenv("REDIS_TTL_SECONDS", "300")),
    request_timeout_seconds=float(os.getenv("REQUEST_TIMEOUT_SECONDS", "10")),
    programmable_search_api_key=os.getenv("PROGRAMMABLE_SEARCH_API_KEY"),
    programmable_search_engine_id=os.getenv("PROGRAMMABLE_SEARCH_ENGINE_ID"),
)
