# Tooling

Use this reference when the task is not only to find information, but also to process, reshape, score, evaluate, or present it.

## Tooling Roles

Treat tools as serving one or more of these functions:

- `source`: retrieve or expose data
- `enrichment`: add attributes, identifiers, profiles, metrics, or relationships
- `transform`: convert between structured and unstructured forms
- `summarize`: compress multi-source material into usable findings
- `taxonomy`: normalize labels, types, properties, and relations
- `deduce`: infer likely matches or relationships from evidence
- `sherlock_deduce`: connect non-obvious paths and test structured hypotheses when explicitly requested
- `eval`: score quality, confidence, coverage, or consistency
- `report`: produce human-readable output
- `visualize`: shape results for graphs, dashboards, or BI tools
- `notify`: propagate critical findings to alerting channels

## Tool-As-Source Pattern

When using a tool-backed source:

- record the tool name as `source_of_information` when it materially affects provenance
- preserve the underlying URL, platform, or canonical source when available
- separate raw source extraction from normalized interpretation
- do not hide whether a fact came from a first-party page, public database, platform listing, map result, or social source

## Data Enrichment

Use enrichment tools or source families to add:

- identifiers
- profile links
- organization and account relations
- location and time context
- ratings, reviews, and public signals
- incident and employment/life-event signals
- taxonomy labels

Enrichment should:

- prefer high-trust sources first
- preserve source and confidence
- avoid filling unsupported fields

## Structure Transformation

The skill should support both directions:

### Structured to unstructured

Use when the user wants:

- executive summary
- narrative report
- investigation memo
- verification note
- BI commentary

### Unstructured to structured

Use when the user wants:

- schema record
- SurrealDB records
- normalized relation edges
- action records
- timelines
- important data points

## Summarization

Summarization should:

- compress without losing provenance
- preserve important caveats
- keep trust distinctions visible
- maintain ranking and confidence where needed

## Taxonomy Building

Use taxonomy-building tools or workflows to:

- normalize schema types
- normalize relation labels
- normalize skills, industries, topics, brands, and risk signals
- align records to schema.org where possible
- define custom extensions only where needed

## Deduction

Deduction is allowed only as evidence-based reasoning, not guesswork.

Use deduction for:

- likely duplicate detection
- probable identity linking
- relationship inference from multiple public signals
- timeline and correlation interpretation

Always:

- preserve confidence
- separate inference from fact
- keep the supporting evidence attached

Use `sherlock_deduce` only when the user explicitly asks for deeper dot-connecting. In that mode:

- compare multiple hypotheses
- surface missing links instead of smoothing them over
- emit traces so the deduction path can be reviewed
- keep speculative leaps out of the final fact set

## Eval

Use eval logic to score:

- resolution quality
- source coverage
- confidence calibration
- ranking quality
- schema completeness
- graph usefulness
- SurrealDB readiness

Useful eval dimensions:

- `coverage_score`
- `consistency_score`
- `confidence_quality`
- `ranking_quality`
- `schema_completeness`
- `provenance_quality`

## Reporting

Common report outputs:

- verification report
- enrichment report
- entity resolution report
- risk signal report
- social cause ecosystem report
- timeline report
- correlation report

Each report should preserve:

- source links
- trust markers
- confidence
- caveats
- important data points

## Visual Output

Support these presentation targets:

- Mermaid knowledge graph
- BI-ready tables
- node-edge export
- timeline table
- correlation matrix
- SurrealDB records

## Notification

Use notification tooling when a result needs to be propagated quickly after filtering and scoring.

See [notifications.md](notifications.md) for:

- notification payload shape
- escalation rules
- generic webhook and API delivery guidance

When preparing BI-friendly output, favor:

- flat tables for metrics
- normalized edge lists for relationships
- explicit timestamp fields
- explicit geography fields
- stable taxonomy labels

## BI Tool Readiness

For BI tools, produce:

- entity table
- action table
- source table
- relation table
- timeline/event table
- incident/risk table

Recommended fields:

- ids
- schema type
- normalized categories
- timestamps
- locations
- confidence
- trust score
- ranking fields

## Minimal Rule

Every transformation, deduction, summary, or visualization step must keep:

- provenance
- trust distinction
- confidence
- the ability to audit back to source
