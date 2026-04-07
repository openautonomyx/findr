# Examples

## Entity Resolution

```text
Resolve whether these two records belong to the same company:
- https://example.com
- https://www.linkedin.com/company/example
Return confidence, evidence, and recommended_action.
```

## Account Deduplication

```text
These two customer records might be duplicates. Compare domains, handles, location, provider identity, and public profiles. Return merge, review, or keep_separate.
```

## Identity Fabric

```text
Map the identity fabric across Okta, Slack, GitHub, and Google Workspace for this user and organization. Include account, workspace, provider, and authentication relations.
```

## Enrichment

```text
Enrich this organization with official site, G2, LinkedIn, Google Business, and public news sources. Include industry, profiles, relations, and important data points.
```

## Risk Signal Review

```text
Find public risk signals for this company from official notices, public databases, local news, Reddit, and social media. Separate verified findings from reported_publicly signals.
```

## Employment Signal

```text
Find public employment signals for this person: promotion, resignation, job loss, board appointment, investment activity, and relocation.
```

## Local Search

```text
Find nearby hotels near MG Road Bangalore and rank by location, rating, trust_score, relevancy, and contextuality.
```

## Action Record

```text
From these public posts and articles, identify who did what, when, where, and upon whom. Return an action record and graph.
```

## SurrealDB Export

```text
Return the result as `thing`, `action`, `source`, and `relation` records suitable for SurrealDB ingestion.
```
