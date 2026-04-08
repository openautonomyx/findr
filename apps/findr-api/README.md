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

This scaffold returns a structured stub response that matches the project runtime shape closely enough for frontend integration and further implementation.

## Container

```bash
docker build -t findr-api .
docker run --rm -p 8000:8000 findr-api
```
