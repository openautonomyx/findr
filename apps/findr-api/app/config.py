import os

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
    surrealdb_url: str | None = None
    opensearch_url: str | None = None
    redis_url: str | None = None


settings = Settings(
    api_title=os.getenv("API_TITLE", "AutonomyX Finder API"),
    api_version=os.getenv("API_VERSION", "0.1.0"),
    surrealdb_url=os.getenv("SURREALDB_URL"),
    opensearch_url=os.getenv("OPENSEARCH_URL"),
    redis_url=os.getenv("REDIS_URL"),
)
