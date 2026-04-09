# AutonomyX Finder Summary

AutonomyX Finder is a research and investigation platform for resolving entities, enriching records, connecting evidence, and producing knowledge-graph-ready output.

It combines:

- web-visible research
- source-aware enrichment
- identity and account relationship mapping
- duplicate detection
- timeline and causal analysis
- log-aware evidence handling
- structured output for downstream systems

## What It Produces

AutonomyX Finder can return:

- narrative summaries
- schema-structured records
- knowledge graph payloads
- source lists with trust indicators
- traces for provider routing and storage behavior
- SurrealDB-ready records

## Current Runtime

The repo currently includes:

- a Codex skill bundle in [autonomyx-finder](../autonomyx-finder/SKILL.md)
- a Finder API in [apps/findr-api](../apps/findr-api/README.md)
- a standalone React SPA in [apps/findr-web](../apps/findr-web/README.md)
- local runtime services through [docker-compose.yml](../docker-compose.yml)

## Current Capabilities

- standard search
- topic lookup
- entity-oriented search and enrichment
- trust-aware source handling
- Redis caching
- OpenSearch indexing
- SurrealDB persistence
- proxy-trust authentication flow (works with any reverse proxy)

## Current Live Connectors

These provider paths are live today:

- Wikipedia
- Google Programmable Search, when credentials are configured
- direct official-site fetches for URL/domain queries

These are still placeholder-routed and need live connector work:

- Google Maps
- G2
- LinkedIn
- log ingestion connectors

## Deployment Model

Recommended deployment shape:

- React SPA served by any static host (Nginx, Netlify, Vercel, S3, etc.)
- Finder API at `/api/v1`
- same-origin reverse proxy (Nginx, Caddy, oauth2-proxy, Authelia, etc.)
  injecting trusted user headers server-side for auth
- SurrealDB, OpenSearch, and Redis on private network paths

## Best Use Cases

- named entity resolution
- identity fabric mapping
- duplicate account review
- data enrichment
- evidence mapping
- timeline and correlation analysis
- causal investigation
- graph-ready research workflows
