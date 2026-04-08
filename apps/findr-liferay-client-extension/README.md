# Finder Liferay Client Extension

Minimal React shell for the Finder experience at:

```text
/web/findr
```

This is a starter frontend that can be adapted into a Liferay client extension or custom module.

## What it does

- renders a basic query form
- posts to `/o/findr-api/search`
- renders summary, schema record, sources, and a simple graph payload
- forwards Finder user and role headers to the API

## Run

```bash
cd apps/findr-liferay-client-extension
npm install
npm run dev
```

Use `VITE_FINDR_API_BASE` to point the UI to the Finder API outside Liferay.
Use `VITE_FINDR_SHARED_SECRET` only when the API expects a trusted shared secret in non-production or proxy setups.

## Liferay Packaging

Included:

- `client-extension.yaml`

This is a starter descriptor for a custom element style client extension. Adjust asset paths after the first production build if your Liferay packaging pipeline outputs different filenames.

The frontend now registers the `findr-web` custom element directly so it can run both:

- in standalone local development
- inside Liferay custom element packaging

The custom element can receive runtime values from:

- `window.Liferay.ThemeDisplay`
- `window.Liferay.FINDR_CONFIG`
- custom element `data-*` attributes such as:
  - `data-api-base`
  - `data-user-id`
  - `data-user-name`
  - `data-roles`
  - `data-shared-secret`
