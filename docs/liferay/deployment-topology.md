# Deployment Topology

## Public Entry Points

- `https://www.openautonomyx.com/web/findr`
- `https://www.openautonomyx.com/o/findr-api`

## Logical Topology

```text
Browser
  -> Liferay page /web/findr
  -> Finder UI client extension
  -> Finder API /o/findr-api
  -> Redis job queue
  -> Worker services
  -> SurrealDB
  -> OpenSearch
  -> Object storage
  -> Webhook/API alert targets
```

## Runtime Components

### Liferay

Responsibilities:

- page routing
- authentication
- role-based access
- UI shell
- case and dashboard views
- injection of Finder user context into the client extension or trusted proxy path

### Finder API

Responsibilities:

- request validation
- search orchestration
- entity resolution
- enrichment
- graph assembly
- timeline and causal analysis
- alert generation

Recommended implementation:

- `FastAPI` or `NestJS`

### Workers

Responsibilities:

- deep research jobs
- traversal jobs
- crawl everything jobs
- log ingestion jobs
- monitoring/watchlist jobs

### Data Services

- `SurrealDB`
- `OpenSearch`
- `Redis`
- object store

## Container Layout

Suggested containers:

- `liferay`
- `findr-api`
- `findr-worker`
- `surrealdb`
- `opensearch`
- `redis`
- optional `nginx` or ingress

## Recommended Auth Topology

Use same-origin proxying so:

- `/web/findr` is served by Liferay
- `/o/findr-api` is proxied to Finder API
- the proxy or portal layer injects trusted Finder auth headers
- the browser stays in `proxy` auth mode and does not need the Finder shared secret

## Deployment Notes

- keep `SurrealDB`, `OpenSearch`, `Redis`, and object storage on private network paths
- expose only Liferay and the API ingress publicly
- if Liferay proxies the API internally, prefer same-origin routing through `/o/findr-api`
- if possible, inject the shared secret server-side or at the proxy layer instead of exposing it directly to public browser code
- use async jobs for deep research and crawl-heavy modes
- keep alert delivery outbound-only

## Minimum Production Checklist

- TLS enabled on `www.openautonomyx.com`
- authenticated route protection for analyst/admin pages
- API rate limits
- queue retry rules
- storage backup policy
- source provenance retention
- alert delivery logging
