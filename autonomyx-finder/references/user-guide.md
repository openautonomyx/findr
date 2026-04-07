# User Guide

This guide explains how to use `autonomyx-finder` in practical terms.

## What This Skill Does

`autonomyx-finder` helps with:

- named entity resolution
- identity fabric mapping
- duplicate account removal
- data enrichment
- source-aware web research
- schema-structured output
- knowledge-graph generation
- SurrealDB-ready record shaping

It is designed for cases where the answer should include:

- verified details
- source links
- structured fields
- relationship mapping
- confidence and provenance

## What To Ask

Ask for one of these outcomes:

- resolve whether records match
- enrich a profile or company
- map relationships between users, accounts, workspaces, apps, or companies
- collect public signals with trust-aware filtering
- rank or filter by time, location, trust, relevancy, or contextual fit
- produce a schema record or SurrealDB-ready output

## Good Prompt Pattern

Use this pattern when possible:

```text
Task: <what you want>
Subject: <person, company, product, account, app, place, etc.>
Goal: <resolve / enrich / dedupe / rank / map>
Important fields: <time, location, source, profiles, actions, etc.>
Output: <summary / schema record / knowledge graph / SurrealDB records>
Constraints: <public sources only / prefer official / social signals allowed / etc.>
```

## Core Example Prompts

### 1. Named Entity Resolution

```text
Resolve whether these two profiles refer to the same person. Return confidence, evidence, schema record, and knowledge graph.
```

### 2. Identity Fabric

```text
Build an identity fabric for Okta, Slack, and this user account. Show account, workspace, SSO, SCIM, and provider relations.
```

### 3. Duplicate Account Removal

```text
Check whether these two customer accounts are duplicates. Recommend merge, review, or keep_separate and explain why.
```

### 4. Data Enrichment

```text
Enrich this company record using its official site, LinkedIn, G2, and Google Business. Include industries, profiles, important data points, and relationship edges.
```

### 5. Public Signal Review

```text
Find public signals for this person, including employment changes, promotions, life events, bans, complaints, and fraud-related signals. Keep social-only signals labeled clearly.
```

### 6. Local and Map Search

```text
Find nearby coworking spaces in Bangalore. Rank them using location, rating, relevancy, recency, contextuality, and trust_score.
```

### 7. Action Extraction

```text
From these sources, create an action record showing who did what, when, where, and upon whom.
```

### 8. Social Cause Mapping

```text
Map the ecosystem around this social cause. Identify nonprofits, campaigns, sponsors, public advocates, and related organizations, then return a knowledge graph.
```

### 9. Identity Provider Research

```text
Compare Okta and Microsoft Entra for SSO, SCIM, app directory coverage, and workspace identity relationships.
```

### 10. SurrealDB Output

```text
Return the result as SurrealDB-ready `thing`, `action`, `source`, and `relation` records.
```

## Example Output Shape

Typical output should include:

- summary
- schema type
- schema record
- key details
- action record, when relevant
- resolution result, when relevant
- important data points
- knowledge graph
- sources

## How Social Sources Are Handled

The skill can use public social sources such as:

- LinkedIn
- X/Twitter
- Instagram
- Facebook
- Reddit
- public WhatsApp channels

But it should:

- treat them as signals or public claims unless corroborated
- preserve source, date, and trust score
- avoid upgrading social-only claims to verified fact without stronger evidence

## Ranking and Filtering

When ranking matters, ask explicitly for:

- `relevancy`
- `recency`
- `contextuality`
- `trust_score`
- `location`
- `time`

Example:

```text
Rank the candidate matches using relevancy, recency, contextuality, trust_score, and location.
```

## When To Ask For Structured Output

Ask for structured output when you want to:

- store the result in SurrealDB
- compare candidates programmatically
- review merge decisions
- build a downstream graph or dashboard

Example:

```text
Return a schema record, action record, resolution result, and SurrealDB-ready relation edges.
```

## Safe Usage Notes

- Prefer public, official, or clearly authorized data.
- Use confidence and evidence for identity matching.
- Keep private or inaccessible data out of scope.
- Treat social, ban, complaint, or incident signals as structured public signals, not automatic proof.
