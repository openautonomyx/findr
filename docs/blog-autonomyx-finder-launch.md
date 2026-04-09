# Launching AutonomyX Finder

AutonomyX Finder started as a focused entity-resolution skill and grew into a broader investigation stack for research, enrichment, and graph-ready analysis.

The problem was straightforward: most research workflows still fragment search, profile matching, evidence review, and relationship mapping across too many tools. Teams search one system, verify in another, export into spreadsheets, and still have to connect the dots manually.

AutonomyX Finder is designed to reduce that fragmentation.

It brings together:

- entity and identity resolution
- source-aware enrichment
- duplicate account review
- trust-aware evidence handling
- timeline and causal analysis
- log-aware investigation workflows
- knowledge-graph output

The project now has three clear layers.

First, the skill layer. The Finder skill defines how research should be routed, normalized, traced, and returned. It captures the operating model for schema-structured output, taxonomies, graph representation, and evidence-aware reasoning.

Second, the runtime layer. The repo includes a working Finder API with live provider execution where supported, plus Redis caching, OpenSearch indexing, and SurrealDB persistence. It is no longer just a static design artifact.

Third, the presentation layer. Finder ships with a standalone React SPA that can be deployed to any static host — Nginx, Netlify, Vercel, S3, Cloudflare Pages — with a proxy-trust authentication model for production use.

The current live connector set is intentionally narrow and honest:

- Wikipedia
- Google Programmable Search when credentials are configured
- direct official-site fetches for URL and domain queries

Some source families are still scaffolded rather than fully integrated:

- Google Maps
- G2
- LinkedIn
- log ingestion connectors

That matters because Finder is meant to be operationally credible. It should be explicit about what is live, what is placeholder-routed, and what still needs connector work.

The infrastructure shape is also deliberate. Finder is designed for a clean, portable production topology:

- React SPA served by any static host
- Finder API at `/api/v1`
- same-origin reverse proxy injecting trusted user headers server-side
- SurrealDB, OpenSearch, and Redis behind private network paths

Any identity-aware proxy works — Nginx, Caddy, oauth2-proxy, Authelia, Kong, Traefik. Finder trusts whatever the proxy tells it, as long as the shared secret matches.

This model gives teams a path from research prompt to structured output, and from structured output to downstream storage, graphing, and review workflows.

AutonomyX Finder is already useful as a foundation for:

- investigation portals
- analyst workbenches
- enrichment workflows
- identity fabric mapping
- evidence review systems
- graph-backed research interfaces

The next phase is straightforward:

- deepen provider coverage
- expand graph and timeline UX
- add richer background jobs and monitoring
- semantic / vector search over indexed evidence
- production deployment hardening

AutonomyX Finder is now beyond the idea stage. It has a usable skill, a working API, a standalone React frontend, and a clear architecture for production hardening.
