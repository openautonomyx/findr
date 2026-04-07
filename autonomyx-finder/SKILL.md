---
name: autonomyx-finder
description: Resolve named entities, identity records, account relationships, and web-visible subjects, then answer with verified details, links, a schema-structured record, and a knowledge graph. Use when the user asks for named entity resolution, identity fabric mapping, duplicate account removal, data enrichment, social-cause research, or to find, research, explain, compare, or summarize people, organizations, products, applications, features, customers, vendors, partners, employees, identity providers, movies, music, places, hotels, local businesses, nearby results, integrations, actions, agents, skills, MCPs, topics, datasets, statistics, or other web-verifiable subjects.
---

# AutonomyX Finder

Use this skill to turn an open-ended discovery or resolution query into:

- a sourced answer
- a normalized schema-style record
- a knowledge graph
- a SurrealDB-ready record and edge model when persistence is needed
- transformed structured or unstructured output for downstream tools
- reports, eval artifacts, and visual-ready graph output when needed

This skill is model-agnostic and can be used with any capable LLM. Adjust depth by task:

- `fast pass`: quick source selection and normalization
- `deep research`: broader source collection, stronger corroboration, richer ranking, and fuller graph extraction
- `graph traversal`: multi-hop web crawling from the seed entity through related nodes, with bounds, trust filtering, and traceable path expansion
- `crawl everything`: exhaustive crawl mode with checkpointing, deduplication, budgets, and path tracking for large graph expansion
- `sherlock deduction`: optional high-inference mode for connecting non-obvious evidence paths, weak signals, and missing links; keep it off unless explicitly requested
- `alerting`: emit a structured critical-finding payload to an outbound webhook or API when the workflow requires propagation

## Quick Decision Tree

1. Identify the search mode.
   - `named entity resolution`, `identity fabric`, `duplicate account removal`, `data enrichment`: treat the task as an identity-resolution workflow first.
   - `social causes`, `nonprofit ecosystem`, `campaign network`: treat the task as cause-and-organization discovery with relationship mapping.
   - `deep research`, `deep search`, `investigate thoroughly`: increase source breadth, corroboration, and trace detail.
   - `crawl deeply`, `follow related nodes`, `path traversal`, `find distant related entities`: switch to bounded graph traversal mode.
   - `crawl everything`, `exhaustive crawl`, `expand all reachable nodes`: switch to exhaustive crawl mode with explicit crawl limits and checkpointing.
   - `sherlock deduction`, `connect the dots`, `deduce hidden links`, `investigate less obvious links`: enable optional high-inference mode with explicit trace output.
2. Pick the best source family before generic search.
3. Classify the subject to the closest schema type.
4. Normalize relations, job profile, industry, skills, and profiles when relevant.
5. Return the answer, sources, schema record, and knowledge graph.

## Search Mode Guide

- `named entity resolution`: decide whether multiple records refer to the same person, org, account, app, or asset.
- `identity fabric`: map users, accounts, providers, workspaces, orgs, and systems into a single relationship graph.
- `duplicate account removal`: identify duplicate or overlapping accounts, compare evidence, and surface merge candidates rather than guessing.
- `data enrichment`: add verified attributes, identifiers, profiles, industries, skills, and relations to an existing entity record.
- `social causes`: identify the cause, campaigns, nonprofits, coalitions, sponsors, partners, and public actors around it.
- `cause analysis`, `impact analysis`, `why did this happen`: model source-backed causal chains, dependencies, and downstream effects without overstating certainty.
- `people`, `employee`, `relationship`: use public profile, directory, and employment sources.
- `identity provider`, `SSO`, `directory`, `workspace identity`: use official IdP docs, app directories, and security/setup docs.
- `audit log`, `access log`, `network log`, `transaction log`: use structured log and event evidence first, then enrich with public or official context.
- `product`, `application`, `feature`, `vendor`, `partner`, `customer`: use official product/company sources, catalogs, and comparison sources.
- `integration`, `action`, `agent`, `skill`, `MCP`: use official docs, registries, directories, repos, and manifests.
- `map`, `hotel`, `local business`, `services`, `nearby`: use map/local sources first.
- `movie`, `music`, `publication`, `creative work`, `topic`: use the most authoritative media/reference source for that type.
- `data point`, `dataset`, `metric`: use official statistical or reporting sources.

## Source Routing

Read [routing.md](references/routing.md) when choosing sources or shaping a search strategy.

## Taxonomy

Read [taxonomy.md](references/taxonomy.md) when you need:

- schema-style subject classification
- data typing
- relation labels for the graph
- job profile normalization
- industry normalization
- skills normalization

Read [global-taxonomies.md](references/global-taxonomies.md) when you need:

- extensive relation taxonomy
- skill level taxonomy
- SFIA-aligned skill normalization
- brand taxonomy
- topic taxonomy
- broader global normalization labels for storage

Read [schema-mapping.md](references/schema-mapping.md) when you need:

- schema.org-native vs custom field distinctions
- SurrealDB storage keys
- normalized field mapping for records and edges

## Output

Read [output.md](references/output.md) before finalizing the response.

## Storage

Read [surrealdb.md](references/surrealdb.md) when the user wants the result shaped for SurrealDB records, edges, or ingestion pipelines.
Read [runtime.md](references/runtime.md) when the user wants a consistent machine-readable output contract.

## Tooling

Read [tooling.md](references/tooling.md) when the user wants to:

- enrich data from multiple tools or sources
- transform structured data to unstructured summaries or vice versa
- summarize or normalize source material
- build or extend taxonomies
- deduce likely matches or relationships from evidence
- run eval-style checks
- generate reports
- present results in visual graph form or BI-friendly structures
- trigger notifications or escalation workflows for critical findings

Read [notifications.md](references/notifications.md) when the user wants:

- a critical-finding alert payload
- webhook or API delivery guidance
- alert thresholds and escalation rules

## User Docs

For user-facing guidance and prompt examples, read:

- [user-guide.md](references/user-guide.md)
- [examples.md](references/examples.md)

## Evals And Traces

For testing and auditability, use:

- [evals.json](evals/evals.json)
- [traces.md](references/traces.md)

## Rules

- Prefer primary and authoritative sources.
- Filter sources by trust tier before using them in resolution or enrichment.
- Verify time-sensitive facts.
- For entity resolution, compare stable identifiers before soft signals.
- For duplicate removal, present confidence and evidence. Do not auto-merge ambiguous identities.
- For data enrichment, add only attributes that are directly supported or strongly corroborated.
- Keep `sherlock deduction` off by default. Only use it when the user explicitly asks for stronger deduction or hidden-link analysis.
- In `sherlock deduction` mode, separate `verified fact`, `observed signal`, `inference`, and `missing link`.
- Do not infer private identity, friend, workspace, or tenant relationships without authorized data.
- Treat social profiles as trustworthy only when official, verified, directly linked from a trusted source, or strongly attributable.
- Present a knowledge graph whenever the subject has meaningful linked entities.
