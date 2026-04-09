# Finder Web

Minimal React shell for the AutonomyX Finder experience — a standalone
single-page app that can be served from any static host.

## What it does

- renders a basic query form
- posts to `/api/v1/search`
- renders summary, schema record, sources, and a simple graph payload
- forwards Finder user and role headers to the API (opt-in, for testing only)

## Run locally

```bash
cd apps/findr-web
npm install
npm run dev
```

The dev server starts at http://localhost:5173.

## Configuration

Environment variables (create `.env` from `.env.example`):

| Variable | Purpose | Default |
|---|---|---|
| `VITE_FINDR_API_BASE` | Finder API base URL | `http://localhost:8000` |
| `VITE_FINDR_APP_BASE` | Public path the SPA is mounted at | `/` |
| `VITE_FINDR_AUTH_MODE` | `proxy` (production) or `browserHeaders` (testing) | `proxy` |
| `VITE_FINDR_SHARED_SECRET` | Only used with `browserHeaders` for local testing | empty |

## Auth modes

**`proxy` (recommended for production)**
The frontend sends no auth headers. A reverse proxy in front of the Finder API
(Nginx, Caddy, oauth2-proxy, or any identity-aware gateway) injects the trusted
headers server-side:

- `X-Findr-User-Id`
- `X-Findr-User-Name`
- `X-Findr-Roles`
- `X-Findr-Shared-Secret`

The browser never sees the shared secret.

**`browserHeaders` (local/testing only)**
The frontend sends Finder headers directly from the browser. Do not use this
in production — never expose a long-lived shared secret to public browser code.

## Build and deploy

```bash
npm run build
```

Output lives in `build/`. Copy it to any static host:

- Nginx / Caddy / Apache (serve the directory)
- Netlify, Vercel, Cloudflare Pages, GitHub Pages (drag-and-drop or CI)
- S3 + CloudFront, Azure Static Web Apps, Google Cloud Storage

No portal, CMS, or plugin system is required.
