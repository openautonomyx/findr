# Runtime

Use this reference when you need the skill to emit a consistent machine-readable result.

## Output Contract

Primary machine-readable schema:

- [output-schema.json](../assets/output-schema.json)

Primary SurrealDB bootstrap:

- [surrealdb-template.surql](../assets/surrealdb-template.surql)

Sample outputs:

- [entity-resolution-sample.json](../examples/entity-resolution-sample.json)
- [local-risk-signal-sample.json](../examples/local-risk-signal-sample.json)
- [identity-fabric-sample.json](../examples/identity-fabric-sample.json)

## Runtime Steps

1. Determine `search_mode`.
2. Choose execution depth:
   - `fast pass`
   - `standard`
   - `deep research`
   - `graph traversal`
   - `crawl everything`
3. Collect and rank sources.
4. Build normalized records:
   - `schema_record`
   - `action_record`, when relevant
   - `resolution_result`, when relevant
   - `knowledge_graph`
5. Attach:
   - `sort_filter_attributes`
   - `important_data_points`
   - `employment_life_signals`
   - `timeline` / `correlations`, when relevant
6. Validate shape against `output-schema.json`.
7. If persistence is requested, convert to `thing`, `action`, `source`, and `relation` records.

## Minimal Emission Rules

- Always emit `search_mode`, `schema_type`, `summary`, and `sources`.
- Emit `schema_record` whenever normalization is possible.
- Emit `knowledge_graph` whenever linked entities exist.
- Emit `action_record` whenever the task involves who-did-what-when-where.
- Emit `resolution_result` for resolution, dedupe, or enrichment tasks.
- Emit ranking fields when ranking/filtering influenced the answer.

## Validation Notes

- Omit unsupported fields rather than inventing values.
- Keep custom fields stable.
- Preserve source provenance for every nontrivial claim.
