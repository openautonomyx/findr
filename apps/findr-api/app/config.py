from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

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
    auth_required: bool = False
    trusted_shared_secret: Optional[str] = None
    default_search_roles: str = "findr-user,findr-analyst,findr-admin"


settings = Settings()
