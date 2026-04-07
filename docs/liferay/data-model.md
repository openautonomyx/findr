# Data Model

Primary persistence model:

- `SurrealDB` for graph-oriented records
- `OpenSearch` for full-text retrieval and faceted filtering

## SurrealDB Tables

### `thing`

Use for:

- person
- organization
- product
- place
- account
- service

Key fields:

- `id`
- `schema_type`
- `name`
- `identifiers`
- `profiles`
- `industries`
- `skills`
- `brand`

### `action`

Use for:

- observed actions
- non-actions
- timeline events
- workflow events
- payment and activity events

Key fields:

- `id`
- `action_type`
- `non_action`
- `actor`
- `target`
- `time`
- `location`
- `status`
- `confidence`

### `source`

Use for:

- web pages
- public profiles
- reviews
- logs
- messages
- official notices

Key fields:

- `id`
- `source_url`
- `source_of_information`
- `source_tier`
- `trust_score`
- `published_at`
- `log_source`

### `relation`

Use for:

- graph edges between records

Key fields:

- `id`
- `from`
- `type`
- `to`
- `confidence`

## Search Index

Use `OpenSearch` for:

- full-text search
- phrase search
- filters by location, time, source type, trust tier, and schema type
- ranking across relevance, recency, and contextuality

Recommended indexed fields:

- `summary`
- `name`
- `alternate_names`
- `topics`
- `skills`
- `industries`
- `location`
- `published_at`
- `source_tier`
- `trust_score`

## Evidence and Logs

Normalize these as first-class evidence:

- `audit_log`
- `access_log`
- `network_access_log`
- `transaction_log`
- `workflow_log`
- `personal_chat`
- `direct_message`

## Cases

Recommended case object:

- `case_id`
- `title`
- `status`
- `owner`
- `subjects`
- `saved_result_refs`
- `alert_refs`
- `created_at`
- `updated_at`

## Alert Records

Store alert payloads with:

- `alert_id`
- `alert_type`
- `severity`
- `entity`
- `summary`
- `delivery_mode`
- `status`
- `source_links`
