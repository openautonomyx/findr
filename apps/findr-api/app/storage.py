from pydantic import BaseModel


class StorageTargets(BaseModel):
    surrealdb_url: str | None = None
    opensearch_url: str | None = None
    redis_url: str | None = None


class StorageHealth(BaseModel):
    surrealdb: str
    opensearch: str
    redis: str


def storage_health(targets: StorageTargets) -> StorageHealth:
    return StorageHealth(
        surrealdb="configured" if targets.surrealdb_url else "not_configured",
        opensearch="configured" if targets.opensearch_url else "not_configured",
        redis="configured" if targets.redis_url else "not_configured",
    )
