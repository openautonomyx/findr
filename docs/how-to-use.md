# How To Use AutonomyX Finder

This guide covers the fastest path to run and use the current project.

## 1. Configure Local Environment

Create or edit these files:

- [apps/findr-api/.env](../apps/findr-api/.env)
- [apps/findr-web/.env](../apps/findr-web/.env)

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
- `GET /api/v1/health/storage`
- `GET /api/v1/me`
- `POST /api/v1/search`
- `POST /api/v1/logs/ingest`

## 4. Run the Frontend

```bash
cd apps/findr-web
npm install
npm run dev
```

For local development, the frontend uses the values in:

- [apps/findr-web/.env](../apps/findr-web/.env)

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

## 6. Ingest Log Evidence

Use log ingestion when you already have authorized audit, access,
workflow, transaction, or network events and want Finder to normalize
them into a case graph.

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

Expected result shape:

- case id
- accepted event count
- severity and source summary
- case/event/actor/target graph
- storage status
- trace

## 7. Deploy to Production

Recommended production setup:

- serve the React SPA from any static host (Nginx, Caddy, Netlify,
  Vercel, S3 + CloudFront, Cloudflare Pages, GitHub Pages)
- expose the Finder API at `/api/v1` behind the same reverse proxy as
  the frontend (same-origin avoids CORS entirely)
- keep frontend `VITE_FINDR_AUTH_MODE=proxy`
- configure your reverse proxy (Nginx, Caddy, oauth2-proxy, Authelia,
  Kong, Traefik) to inject Finder headers server-side after
  authenticating the user

See `docs/credentials.md` for the full proxy-trust auth setup.

## 8. Understand Auth Modes

Preferred production mode:

- `proxy`

Use only for local or controlled testing:

- `browserHeaders`

The browser should not carry a long-lived Finder shared secret in production.

## 9. Know The Current Limits

What is implemented:

- runtime API
- standalone React SPA frontend
- Redis cache
- OpenSearch index writes
- SurrealDB persistence
- log ingestion endpoint
- proxy-trust auth model (works with any reverse proxy)

What still needs expansion:

- Google Maps connector
- G2 connector
- LinkedIn connector
- richer graph and timeline UI
- background jobs beyond the current scaffold
