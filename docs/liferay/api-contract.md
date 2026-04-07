# Finder API Contract

Recommended API base:

```text
https://www.openautonomyx.com/o/findr-api
```

## Auth Model

- Liferay authenticates the user
- Finder API receives Liferay-backed identity or a trusted service token
- API enforces route access from Liferay roles

## Core Endpoints

### `POST /o/findr-api/search`

Use for:

- standard search
- topic lookup
- local/place search
- quick entity discovery

Request:

```json
{
  "query": "Find Okta in Bangalore",
  "search_mode": "standard_search",
  "depth_mode": "fast pass",
  "filters": {
    "location": "Bangalore",
    "time": "last_90_days"
  }
}
```

### `POST /o/findr-api/resolve`

Use for:

- entity resolution
- duplicate detection
- identity fabric mapping

Request:

```json
{
  "records": [
    {"name": "Example User", "profile": "https://example.com/a"},
    {"name": "Example User", "profile": "https://example.com/b"}
  ],
  "depth_mode": "standard"
}
```

### `POST /o/findr-api/enrich`

Use for:

- record enrichment
- profile and attribute expansion

### `POST /o/findr-api/graph`

Use for:

- knowledge graph generation
- relationship extraction
- traversal output

### `POST /o/findr-api/timeline`

Use for:

- event timeline generation
- correlation analysis

### `POST /o/findr-api/causal-analysis`

Use for:

- cause and impact analysis
- dependency chain analysis

Example:

```json
{
  "query": "How did loan non-disbursal affect school fee payment?",
  "events": [
    {"event": "loan_not_disbursed", "time": "2026-03-28"},
    {"event": "school_fees_unpaid", "time": "2026-04-03"}
  ]
}
```

### `POST /o/findr-api/logs/ingest`

Use for:

- audit logs
- access logs
- network logs
- workflow logs

### `POST /o/findr-api/alerts`

Use for:

- critical-finding webhook/API payload generation
- alert propagation

### `POST /o/findr-api/jobs`

Use for:

- deep research
- crawl everything
- long-running enrichment

Response:

```json
{
  "job_id": "job_123",
  "status": "queued"
}
```

### `GET /o/findr-api/jobs/{id}`

Use for:

- polling async work
- progress and result retrieval

### `GET /o/findr-api/cases`

Use for:

- list saved cases

### `POST /o/findr-api/cases`

Use for:

- create a saved investigation

### `GET /o/findr-api/export/{id}`

Use for:

- export report
- download graph payload
- download schema records

## Response Shape

Responses should follow the skill runtime model in:

- [runtime.md](../../autonomyx-finder/references/runtime.md)
- [output-schema.json](../../autonomyx-finder/assets/output-schema.json)

Core response fields:

- `search_mode`
- `schema_type`
- `summary`
- `schema_record`
- `action_record`
- `knowledge_graph`
- `resolution_result`
- `sources`
- `trace`

## Async Pattern

For `deep research`, `graph traversal`, `crawl everything`, or large log ingestion:

1. create async job
2. return `job_id`
3. poll `/jobs/{id}`
4. render result at `/web/findr/results/{jobId}`
