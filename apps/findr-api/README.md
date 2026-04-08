# Finder API

Minimal backend scaffold for the Liferay-integrated Finder service.

## Run

```bash
cd apps/findr-api
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
uvicorn app.main:app --reload --port 8000
```

## First endpoint

- `POST /o/findr-api/search`

This scaffold now includes:

- provider selection and routing stubs
- structured search trace output
- storage health endpoint for SurrealDB/OpenSearch/Redis wiring

Current implementation is still a structured stub, but no longer a single hard-coded source path.

## Container

```bash
docker build -t findr-api .
docker run --rm -p 8000:8000 findr-api
```

## Storage Health

- `GET /o/findr-api/health/storage`
