# How To Use AutonomyX Finder

This guide covers the fastest path to run and use the current project.

## 1. Configure Local Environment

Create or edit these files:

- [apps/findr-api/.env](../apps/findr-api/.env)
- [apps/findr-liferay-client-extension/.env](../apps/findr-liferay-client-extension/.env)

At minimum, replace these placeholders in the API env file if you want live Google Programmable Search:

- `PROGRAMMABLE_SEARCH_API_KEY`
- `PROGRAMMABLE_SEARCH_ENGINE_ID`

Reference:

- [docs/credentials.md](./credentials.md)

## 2. Start Local Services

From the repo root:

```bash
docker compose up -d surrealdb opensearch redis
```

This starts:

- `SurrealDB`
- `OpenSearch`
- `Redis`

## 3. Run the API

```bash
cd apps/findr-api
source .venv/bin/activate
uvicorn app.main:app --reload --port 8000
```

Useful endpoints:

- `GET /health`
- `GET /o/findr-api/health/storage`
- `GET /o/findr-api/me`
- `POST /o/findr-api/search`

## 4. Run the Frontend

```bash
cd apps/findr-liferay-client-extension
npm run dev
```

For local development, the frontend uses the values in:

- [apps/findr-liferay-client-extension/.env](../apps/findr-liferay-client-extension/.env)

## 5. Try A Search

Example payload:

```json
{
  "query": "OpenSearch Project",
  "search_mode": "standard_search",
  "depth_mode": "fast pass",
  "filters": {
    "location": "global"
  },
  "include_trace": true
}
```

Expected result shape:

- summary
- schema record
- sources
- knowledge graph
- trace

## 6. Use In Liferay

Recommended production setup:

- mount the UI at `/web/findr`
- expose the API at `/o/findr-api`
- keep frontend auth mode as `proxy`
- have Liferay or a trusted proxy inject Finder headers server-side

Reference:

- [docs/liferay/page-map.md](./liferay/page-map.md)
- [docs/liferay/auth-proxy.md](./liferay/auth-proxy.md)
- [docs/liferay/deployment-topology.md](./liferay/deployment-topology.md)

## 7. Understand Auth Modes

Preferred production mode:

- `proxy`

Use only for local or controlled testing:

- `browserHeaders`

The browser should not carry a long-lived Finder shared secret in production.

## 8. Know The Current Limits

What is implemented:

- runtime API
- Liferay client-extension shell
- Redis cache
- OpenSearch index writes
- SurrealDB persistence
- proxy-first auth model

What still needs expansion:

- Google Maps connector
- G2 connector
- LinkedIn connector
- log ingestion pipeline
- richer graph and timeline UI
- background jobs beyond the current scaffold
