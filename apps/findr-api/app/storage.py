from __future__ import annotations

import json
from datetime import datetime, timezone
from dataclasses import dataclass
from typing import Optional
from uuid import uuid4

import httpx
import redis
from pydantic import BaseModel

from .config import settings
from .models import SearchRequest, SearchResponse


class StorageTargets(BaseModel):
    surrealdb_url: Optional[str] = None
    opensearch_url: Optional[str] = None
    redis_url: Optional[str] = None


class StorageHealth(BaseModel):
    surrealdb: str
    opensearch: str
    redis: str


@dataclass
class SearchStorage:
    redis_client: Optional[redis.Redis]
    surrealdb_url: Optional[str]
    opensearch_url: Optional[str]

    @classmethod
    def from_settings(cls) -> "SearchStorage":
        return cls.from_targets(
            StorageTargets(
                surrealdb_url=settings.surrealdb_url,
                opensearch_url=settings.opensearch_url,
                redis_url=settings.redis_url,
            )
        )

    @classmethod
    def from_targets(cls, targets: StorageTargets) -> "SearchStorage":
        client = None
        if targets.redis_url:
            try:
                client = redis.from_url(targets.redis_url, decode_responses=True)
            except Exception:
                client = None
        return cls(
            redis_client=client,
            surrealdb_url=targets.surrealdb_url,
            opensearch_url=targets.opensearch_url,
        )

    def cache_key(self, request: SearchRequest) -> str:
        return "findr:search:" + json.dumps(request.model_dump(), sort_keys=True)

    def get_cached(self, request: SearchRequest) -> Optional[SearchResponse]:
        if not self.redis_client:
            return None
        try:
            payload = self.redis_client.get(self.cache_key(request))
            if not payload:
                return None
            return SearchResponse.model_validate_json(payload)
        except Exception:
            return None

    def set_cached(self, request: SearchRequest, response: SearchResponse) -> bool:
        if not self.redis_client:
            return False
        try:
            self.redis_client.setex(
                self.cache_key(request),
                settings.redis_ttl_seconds,
                response.model_dump_json(),
            )
            return True
        except Exception:
            return False

    def check_redis(self) -> str:
        if not self.redis_client:
            return "not_configured"
        try:
            return "healthy" if self.redis_client.ping() else "unavailable"
        except Exception:
            return "unavailable"

    def check_surrealdb(self) -> str:
        if not self.surrealdb_url:
            return "not_configured"
        try:
            with httpx.Client(timeout=settings.request_timeout_seconds) as client:
                sql_url = self.surrealdb_url.replace("/rpc", "/sql")
                response = client.post(
                    sql_url,
                    content=(
                        f"USE NS {settings.surrealdb_namespace} DB {settings.surrealdb_database};"
                        " INFO FOR DB;"
                    ),
                    auth=(settings.surrealdb_user, settings.surrealdb_password),
                    headers={"Accept": "application/json"},
                )
                response.raise_for_status()
            return "healthy"
        except Exception:
            return "unavailable"

    def check_opensearch(self) -> str:
        if not self.opensearch_url:
            return "not_configured"
        try:
            with httpx.Client(timeout=settings.request_timeout_seconds) as client:
                response = client.get(self.opensearch_url)
                response.raise_for_status()
            return "healthy"
        except Exception:
            return "unavailable"

    def persist_search(self, request: SearchRequest, response: SearchResponse) -> bool:
        if not self.surrealdb_url:
            return False
        try:
            with httpx.Client(timeout=settings.request_timeout_seconds) as client:
                sql_url = self.surrealdb_url.replace("/rpc", "/sql")
                record_id = f"search_result:{uuid4().hex}"
                payload = {
                    "query": request.query,
                    "search_mode": response.search_mode,
                    "schema_type": response.schema_type,
                    "summary": response.summary,
                    "schema_record": response.schema_record,
                    "knowledge_graph": response.knowledge_graph,
                    "sources": [source.model_dump() for source in response.sources],
                    "trace": response.trace.model_dump() if response.trace else None,
                    "created_at": datetime.now(timezone.utc).isoformat(),
                }
                surreal_response = client.post(
                    sql_url,
                    content=(
                        f"USE NS {settings.surrealdb_namespace} DB {settings.surrealdb_database};"
                        f" CREATE {record_id} CONTENT {json.dumps(payload)};"
                    ),
                    auth=(settings.surrealdb_user, settings.surrealdb_password),
                    headers={"Accept": "application/json"},
                )
                surreal_response.raise_for_status()
                body = surreal_response.json()
                if not body or any(item.get("status") != "OK" for item in body):
                    return False
            return True
        except Exception:
            return False

    def index_search(self, request: SearchRequest, response: SearchResponse) -> bool:
        if not self.opensearch_url:
            return False
        try:
            with httpx.Client(timeout=settings.request_timeout_seconds) as client:
                client.post(
                    f"{self.opensearch_url}/{settings.opensearch_index}/_doc",
                    json={
                        "query": request.query,
                        "search_mode": response.search_mode,
                        "schema_type": response.schema_type,
                        "summary": response.summary,
                        "schema_record": response.schema_record,
                    },
                ).raise_for_status()
            return True
        except Exception:
            return False


def storage_health(targets: StorageTargets) -> StorageHealth:
    storage = SearchStorage.from_targets(targets)
    return StorageHealth(
        surrealdb=storage.check_surrealdb(),
        opensearch=storage.check_opensearch(),
        redis=storage.check_redis(),
    )
