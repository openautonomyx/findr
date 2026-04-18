# Finder API

FastAPI backend for AutonomyX Finder — research, enrichment, and
evidence-mapping service.

## Run

```bash
cd apps/findr-api
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
cp .env.example .env
uvicorn app.main:app --reload --port 8000
```

The API reads credentials and service URLs from `.env` automatically.

## Endpoints

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/health` | Liveness probe |
| `GET` | `/api/v1/health/storage` | SurrealDB + OpenSearch + Redis health |
| `GET` | `/api/v1/me` | Current authenticated context |
| `POST` | `/api/v1/search` | Run a Finder search |
| `POST` | `/api/v1/logs/ingest` | Ingest authorized log events into a case graph |

## Features

- provider selection and live provider execution where supported
- structured search trace output
- log event normalization with graph-ready case output
- storage health endpoint for SurrealDB/OpenSearch/Redis wiring
- role-aware proxy-trust header authentication

## Live connectors

- Wikipedia summary lookups
- Google Programmable Search (when API credentials are configured)
- direct official-site fetches when the query is a domain or URL
- authorized log event ingestion from caller-supplied payloads

Search responses are persisted to SurrealDB, indexed in OpenSearch, and
cached in Redis when those services are configured. Log ingests are
persisted to SurrealDB and indexed in OpenSearch when configured.

## Log Ingestion

```bash
curl -X POST http://localhost:8000/api/v1/logs/ingest \
  -H 'Content-Type: application/json' \
  -d '{
    "case_id": "case-demo",
    "events": [
      {
        "source": "auth-service",
        "event_type": "login_failure",
        "severity": "warning",
        "actor": "user@example.com",
        "target": "vpn",
        "message": "Repeated failed login attempts"
      }
    ]
  }'
```

The response includes a normalized schema record, source summary, and
knowledge graph linking the case, event, actor, and target.

## Container

```bash
docker build -t findr-api .
docker run --rm -p 8000:8000 findr-api
```

## Authentication

When `AUTH_REQUIRED=true`, the API expects trusted proxy-set headers:

- `X-Findr-User-Id`
- `X-Findr-User-Name`
- `X-Findr-Roles`
- `X-Findr-Shared-Secret`

The "proxy-trust" model means any reverse proxy (Nginx, Caddy,
oauth2-proxy, Authelia, etc.) in front of the API can inject these
headers server-side. The browser never sees the shared secret.

For local development, set `AUTH_REQUIRED=false` to bypass auth.

## Credentials

Store all credentials in:

```text
apps/findr-api/.env
```

Reference:

```text
docs/credentials.md
```
