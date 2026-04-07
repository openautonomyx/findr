# Traces

Use traces when you want the skill to expose how it reached an answer without dumping chain-of-thought.

## Purpose

Trace output helps with:

- eval review
- ranking inspection
- source trust debugging
- duplicate-resolution audit
- SurrealDB ingestion debugging
- inference-path review for `sherlock deduction`

## Trace Structure

Use a compact trace object when requested:

```json
{
  "trace": {
    "query": "original user task",
    "search_mode": "named entity resolution",
    "source_candidates": [
      {
        "source": "Official website",
        "source_tier": 1,
        "trust_score": 0.98,
        "relevancy": 0.95,
        "recency": 0.80,
        "contextuality": 0.92
      }
    ],
    "classification": {
      "schema_type": "Organization"
    },
    "resolution": {
      "confidence": "high",
      "recommended_action": "merge"
    },
    "ranking_factors": [
      "domain match",
      "official profile linkage",
      "location consistency"
    ],
    "inference_labels": [
      "observed signal",
      "inference",
      "missing link"
    ]
  }
}
```

## Trace Rules

- Do not expose hidden reasoning or unsupported internal speculation.
- Keep traces factual, compact, and auditable.
- Include only observable ranking and normalization factors.
- Prefer trace summaries over verbose step-by-step prose.
- In `sherlock deduction` mode, expose only compact hypothesis and evidence-path summaries, not hidden reasoning.

## Trace Fields

Useful fields include:

- `query`
- `search_mode`
- `source_candidates`
- `source_tier`
- `trust_score`
- `relevancy`
- `recency`
- `contextuality`
- `classification`
- `resolution`
- `ranking_factors`
- `excluded_sources`
- `important_data_points`
- `hypotheses`
- `inferred_links`
- `missing_links`
- `inference_labels`

## When To Emit Traces

Emit a trace when the user asks for:

- debugging
- evaluation
- audit trail
- why a match was chosen
- why a source was ranked higher
- why a merge was or was not recommended
- how a non-obvious inferred link was formed
