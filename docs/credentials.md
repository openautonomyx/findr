# Credentials

Use local `.env` files for development and your deployment platform's secret store for production.

## API

File:

```text
apps/findr-api/.env
```

Start from:

```text
apps/findr-api/.env.example
```

Important variables:

- `SURREALDB_URL`
- `SURREALDB_NAMESPACE`
- `SURREALDB_DATABASE`
- `SURREALDB_USER`
- `SURREALDB_PASSWORD`
- `OPENSEARCH_URL`
- `OPENSEARCH_INDEX`
- `REDIS_URL`
- `PROGRAMMABLE_SEARCH_API_KEY`
- `PROGRAMMABLE_SEARCH_ENGINE_ID`
- `AUTH_REQUIRED`
- `TRUSTED_SHARED_SECRET`

Example local API file:

```dotenv
API_TITLE=AutonomyX Finder API
API_VERSION=0.1.0
SURREALDB_URL=http://localhost:8001/rpc
SURREALDB_NAMESPACE=findr
SURREALDB_DATABASE=findr
SURREALDB_USER=root
SURREALDB_PASSWORD=root
OPENSEARCH_URL=http://localhost:9200
OPENSEARCH_INDEX=findr-search
REDIS_URL=redis://localhost:6379/0
REDIS_TTL_SECONDS=300
REQUEST_TIMEOUT_SECONDS=10
PROGRAMMABLE_SEARCH_API_KEY=
PROGRAMMABLE_SEARCH_ENGINE_ID=
AUTH_REQUIRED=false
TRUSTED_SHARED_SECRET=
```

The API now loads `.env` automatically through `pydantic-settings`.

## Frontend

File:

```text
apps/findr-liferay-client-extension/.env
```

Start from:

```text
apps/findr-liferay-client-extension/.env.example
```

Important variables:

- `VITE_FINDR_API_BASE`
- `VITE_FINDR_APP_BASE`
- `VITE_FINDR_AUTH_MODE`
- `VITE_FINDR_SHARED_SECRET`

Example local frontend file:

```dotenv
VITE_FINDR_API_BASE=http://localhost:8000
VITE_FINDR_APP_BASE=/web/findr
VITE_FINDR_AUTH_MODE=proxy
VITE_FINDR_SHARED_SECRET=
```

## Docker Compose

For local container runs, `docker-compose.yml` already provides default service URLs for:

- `findr-api`
- `surrealdb`
- `opensearch`
- `redis`

Do not hardcode production secrets into `docker-compose.yml`.

## Production

For production deployment, inject the same variables from your hosting platform or CI/CD secret manager.

Recommended rule:

- local development: `.env`
- shared non-secret defaults: `.env.example`
- production: secret manager or platform environment configuration

## Current External Credential Need

Only these provider credentials are currently consumed by live code paths:

- `PROGRAMMABLE_SEARCH_API_KEY`
- `PROGRAMMABLE_SEARCH_ENGINE_ID`

Other providers such as Google Maps, G2, and LinkedIn are still routed as catalog placeholders until live connectors are implemented.

## Liferay Auth Integration

Recommended production setup:

- keep `AUTH_REQUIRED=true` in the API
- inject a trusted `TRUSTED_SHARED_SECRET` only on the server side or trusted proxy path
- keep the frontend in `VITE_FINDR_AUTH_MODE=proxy`
- have the Liferay page or proxy send:
  - `X-Findr-User-Id`
  - `X-Findr-User-Name`
  - `X-Findr-Roles`
  - `X-Findr-Shared-Secret`

Do not expose a long-lived shared secret to public browser code if you can avoid it. Prefer a same-origin trusted proxy, API gateway, or Liferay-backed server-side injection path.

Reference:

- [docs/liferay/auth-proxy.md](./liferay/auth-proxy.md)
