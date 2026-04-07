# SurrealDB

Use this reference when the result should be persisted in SurrealDB.

## Core Model

Store resolved entities, actions, sources, and relations as separate records.

Suggested tables:

- `thing`
- `action`
- `source`
- `relation`

Optional specialized tables:

- `profile`
- `workspace`
- `provider`
- `place`
- `incident`

## Minimal SurrealQL

```sql
DEFINE TABLE thing SCHEMALESS;
DEFINE TABLE action SCHEMALESS;
DEFINE TABLE source SCHEMALESS;
DEFINE TABLE relation SCHEMALESS;
```

## Record Shape

### `thing`

Use for resolved entities.

```json
{
  "id": "thing:okta",
  "schema_type": "Organization",
  "name": "Okta",
  "industries": ["identity", "security", "saas"],
  "identifiers": [
    {"type": "domain", "value": "okta.com"}
  ],
  "profiles": [
    {"platform": "linkedin", "url": "https://www.linkedin.com/company/okta-inc/"}
  ],
  "location": "San Francisco, California, USA"
}
```

### `action`

Use for incidents, activities, and who-did-what records.

```json
{
  "id": "action:auth_1",
  "schema_type": "AuthenticateAction",
  "actor": "thing:user_1",
  "object": "workspace session",
  "target": "thing:slack_workspace_1",
  "time": "2026-04-07T10:30:00Z",
  "location": "Bangalore, India",
  "source": "source:post_1",
  "source_tier": 3,
  "confidence": "medium",
  "status": "reported_publicly"
}
```

### `source`

Use for documents, posts, profiles, map entries, and review pages.

```json
{
  "id": "source:post_1",
  "url": "https://example.com/post",
  "platform": "x",
  "source_tier": 3,
  "published_at": "2026-04-07T10:31:00Z",
  "location": "Bangalore, India",
  "verification_status": "attributable_public_source"
}
```

### `relation`

Use for normalized edges.

```json
{
  "id": "relation:1",
  "from": "thing:okta",
  "type": "single_sign_on_with",
  "to": "thing:slack",
  "source": "source:doc_1",
  "confidence": "high"
}
```

## Edge Strategy

Prefer storing normalized relationships as explicit edge-like records:

- `same_as`
- `possible_duplicate_of`
- `has_account`
- `identity_managed_by`
- `single_sign_on_with`
- `customer_of`
- `partner_of`
- `employee_of`
- `located_in`
- `documented_by`

## Sort And Filter Fields

Make these easy to query:

- `time`
- `published_at`
- `event_time`
- `location`
- `address`
- `geo_area`
- `distance`
- `rating`
- `review_count`
- `source_tier`
- `verification_status`
- `confidence`

## Persistence Rules

- Store only normalized fields supported by evidence.
- Keep raw source claims separate from verified resolved facts.
- Do not store a `merge` result for duplicates unless confidence is high.
- Keep socially sourced claims as source-linked signals or action records unless corroborated.
- Preserve source URLs, times, and platforms so downstream review is possible.

