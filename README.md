# AutonomyX Finder

Git-ready export of the `autonomyx-finder` Codex skill.

AutonomyX Finder helps investigate entities, enrich records, connect evidence, and produce graph-ready research output.

## Marketplace Blurb

AutonomyX Finder investigates people, organizations, products, accounts, and incidents by combining web research, identity resolution, enrichment, causal analysis, log-aware evidence handling, and knowledge-graph output.

## Contents

- `autonomyx-finder/`
  - the skill bundle
  - references, assets, evals, and examples
- `apps/findr-api/`
  - FastAPI backend with `POST /api/v1/search`
- `apps/findr-web/`
  - React SPA frontend (standalone, deploys to any static host)
- `docker-compose.yml`
  - local API + UI + SurrealDB/OpenSearch/Redis integration slice
- `docs/credentials.md`
  - local `.env` setup
  - production secret placement
  - currently used provider credentials
- `docs/summary.md`
  - concise project overview
  - current capability status
- `docs/how-to-use.md`
  - local run instructions
  - API usage examples
- `docs/blog-autonomyx-finder-launch.md`
  - launch-style blog draft

## Use

Copy `autonomyx-finder/` into:

```text
~/.codex/skills/
```

Then restart Codex or start a new session so skill discovery refreshes.

## Public URLs

- Website: `https://findr.openautonomyx.com`
- Repository: `https://github.com/openautonomyx/findr`
- Privacy: `https://findr.openautonomyx.com/privacy`
- Terms: `https://findr.openautonomyx.com/terms`

## Included

- main skill: `autonomyx-finder`
- schema/output assets
- eval pack
- examples
- user and runtime references
- runnable API and frontend

## Highlights

- entity resolution and duplicate detection
- identity fabric mapping
- data enrichment and source-backed normalization
- timeline, correlation, and causal-chain analysis
- audit, access, network, transaction, and workflow log support
- knowledge graph and structured schema output
- marketplace/plugin packaging and clean release artifacts

## Architecture

Finder is three independent pieces that can be deployed together or separately:

- **Skill layer** (`autonomyx-finder/`) — Codex skill that defines how
  research should be routed, normalized, traced, and returned
- **API layer** (`apps/findr-api/`) — FastAPI service with provider
  routing, evidence ranking, and SurrealDB/OpenSearch/Redis persistence
- **Web layer** (`apps/findr-web/`) — React SPA that talks to the API;
  no portal, CMS, or plugin system required

For production auth, Finder uses a **proxy-trust model**: any reverse
proxy (Nginx, Caddy, oauth2-proxy, Authelia, Kong, Traefik) can inject
the trusted user headers after authenticating the user.

## Release Assets

- `autonomyx-finder-repo-clean.zip`
- `autonomyx-finder-plugin-clean.zip`

## GitHub Release

Suggested title:

```text
AutonomyX Finder v1.0.0
```

Suggested short summary:

```text
Initial public release of AutonomyX Finder for entity resolution, enrichment, evidence mapping, and graph-ready research output.
```

## Notes

- This export is git-initialized for easy publishing.
- The backward-compatible `entity-finder` alias is not included in this repo export.
- API credentials go in `apps/findr-api/.env`.
- Frontend env goes in `apps/findr-web/.env`.

## Quick Links

- [Project Summary](./docs/summary.md)
- [How To Use](./docs/how-to-use.md)
- [Credentials](./docs/credentials.md)
- [Launch Blog Draft](./docs/blog-autonomyx-finder-launch.md)
