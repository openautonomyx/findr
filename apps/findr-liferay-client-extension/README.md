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

## Run

```bash
cd apps/findr-liferay-client-extension
npm install
npm run dev
```

Use `VITE_FINDR_API_BASE` to point the UI to the Finder API outside Liferay.

## Liferay Packaging

Included:

- `client-extension.yaml`

This is a starter descriptor for a custom element style client extension. Adjust asset paths after the first production build if your Liferay packaging pipeline outputs different filenames.
