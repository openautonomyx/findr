# Finder API

Minimal backend scaffold for the Liferay-integrated Finder service.

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

## First endpoint

- `POST /o/findr-api/search`

This scaffold now includes:

- provider selection and live provider execution where supported
- structured search trace output
- storage health endpoint for SurrealDB/OpenSearch/Redis wiring
- role-aware Liferay header authentication support

Current implementation:

- executes live Wikipedia summary lookups
- executes Google Programmable Search when API credentials are configured
- executes direct official-site fetches when the query is a domain or URL
- persists/indexes/caches responses when SurrealDB/OpenSearch/Redis are configured

## Container

```bash
docker build -t findr-api .
docker run --rm -p 8000:8000 findr-api
```

## Storage Health

- `GET /o/findr-api/health/storage`

## Auth

When `AUTH_REQUIRED=true`, the API expects trusted Liferay-style headers:

- `X-Findr-User-Id`
- `X-Findr-User-Name`
- `X-Findr-Roles`
- `X-Findr-Shared-Secret`

Useful endpoint:

- `GET /o/findr-api/me`

## Credentials

Use:

```text
apps/findr-api/.env
```

Reference:

```text
docs/credentials.md
```
