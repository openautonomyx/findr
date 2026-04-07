# Routing

Choose the best source family before generic search.

## Execution Mode

This skill is LLM-agnostic. Use the same schema, routing, and ranking logic regardless of model.

Choose a depth mode:

- `fast pass`: minimal sufficient sources, quick resolution, concise output
- `standard`: balanced verification and coverage
- `deep research`: broader source sweep, more corroboration, stronger ranking comparison, richer graph output, and fuller trace data
- `graph traversal`: crawl outward from the seed through linked entities, profiles, docs, directories, maps, posts, and registries while preserving path evidence
- `crawl everything`: exhaustive expansion across all reachable high-signal nodes with checkpointing, deduping, and crawl budgets
- `sherlock deduction`: connect less-obvious evidence paths, infer plausible missing links, and test structured hypotheses while keeping all inferences labeled and traceable

Use `deep research` when the user asks for depth, investigation, or higher-confidence resolution.
Use `graph traversal` when the user wants distant related nodes, ecosystem mapping, or network expansion.
Use `crawl everything` only when exhaustive expansion is materially useful.
Use `sherlock deduction` only when the user explicitly wants deeper dot-connecting beyond obvious links.

## Sherlock Deduction Rules

When `sherlock deduction` mode is enabled:

- expand beyond direct explicit links into plausible multi-step evidence paths
- compare alternative explanations instead of locking onto the first plausible story
- keep each inferred link attached to observable evidence or an explicit missing-link note
- label outputs as `verified fact`, `observed signal`, `inference`, or `missing link`
- require trace output so the deduction path is reviewable
- do not turn weak multi-hop inference into a merge, accusation, or factual conclusion without corroboration

## Graph Traversal Rules

When traversing the web graph from an entity:

- start from the seed entity and trusted seed sources
- expand through explicit links only: official profiles, referenced organizations, linked docs, partner pages, customer pages, map entities, public posts, citations, registries
- record the path for each discovered node
- rank candidate nodes by trust, relevancy, recency, and contextuality
- stop expansion when nodes become weakly related, repetitive, or low trust

Use bounded traversal defaults unless the user specifies otherwise:

- `max_depth`: 2 for normal deep research
- `max_depth`: 3 for graph traversal mode
- `max_branching`: keep only the top trusted and most relevant children per node
- `max_nodes`: cap the explored graph to avoid noise

Do not treat distant nodes as equally important to direct neighbors. Surface hop distance and path strength in the output.

## Exhaustive Crawl Rules

When running `crawl everything` mode:

- crawl all reachable trusted or potentially relevant nodes until a crawl budget is exhausted
- checkpoint progress so the crawl can resume
- deduplicate nodes by normalized identifiers, domains, handles, and profile links
- keep a frontier queue ordered by trust, relevancy, recency, and contextuality
- preserve excluded nodes separately when they were seen but filtered out
- emit periodic summaries rather than only a final dump

Minimum controls:

- `crawl_budget_pages`
- `crawl_budget_nodes`
- `crawl_budget_depth`
- `checkpoint_interval`
- `dedupe_keys`
- `frontier_ordering`

Even in exhaustive mode, do not promote low-trust signals to facts without corroboration.

## Source Trust Filter

Rank sources before using them:

1. `Tier 1`: official sites, official docs, verified provider-managed directories, official profiles, official app directories, official company/team pages, Google Business profiles, official map/business listings
2. `Tier 2`: strong public secondary sources such as reputable news, local news media channels, institutional databases, major registries, authoritative catalogs, trusted review/comparison platforms such as G2
3. `Tier 3`: attributable public social/profile sources such as verified or strongly attributable X/Twitter, Instagram, Facebook, Reddit, YouTube, public WhatsApp channels, GitHub, or public posts
4. `Tier 4`: weak signals such as reposts, unattributed mentions, screenshots without provenance, comments, forums with low attribution, or low-trust aggregators

Use `Tier 1` and `Tier 2` for facts whenever possible.
Use `Tier 3` mainly for enrichment, attribution, leads, and public claims.
Do not use `Tier 4` as factual support unless independently corroborated.

## Supported Public Source Families

Use these source families when relevant:

- Google Business and Google review signals
- Google Maps and local map signals
- X/Twitter
- Instagram
- G2
- Facebook
- public WhatsApp channels
- Reddit
- local news media channels
- official sites and docs
- authoritative directories and registries
- public fraud and scam reporting databases
- public accident and incident databases
- public enforcement, sanction, or ban announcements
- public platform suspension or ban notices

Use these structured source families when the user has authorized or provided them:

- audit logs
- access logs
- network access logs
- transaction logs
- workflow logs
- security event logs
- identity provider sign-in and provisioning logs
- application activity logs
- system log exports and incident reports
- personal chats and message threads

## Identity Resolution First

When the request is about named entity resolution, identity fabric, duplicate account removal, or enrichment:

- start from the seed record the user provides
- gather candidate matches from official, public, or authorized sources
- compare stable identifiers before soft signals
- prefer exact domain, official profile, verified handle, directory entry, employer page, or provider-managed identity evidence
- treat name similarity alone as weak evidence
- return confidence, evidence, and unresolved ambiguity when records might not match
- never collapse two identities into one without source-backed evidence

## General

- Use official sites first for core identity, ownership, leadership, pricing, and product details.
- Use Google Programmable Search API for general structured web search when no better specialized source exists.
- Use Wikipedia first for broad topic orientation, then supplement with stronger/current sources when needed.

## Business and Product

- Use official product docs, pricing, release notes, and company pages for products, applications, and features.
- Use G2 for SaaS review, comparison, alternatives, and category-style queries.
- Use Amazon or other marketplaces for e-commerce listing, seller, rating, shipping, and stock queries.
- Use partner directories, customer story pages, and official vendor pages for customer, vendor, and partner queries.

## People and Identity

- Use Google People API only for authorized contact/directory-style lookup.
- Use LinkedIn, employer pages, team pages, and official bios for employment/profile lookup.
- Use official IdP docs and app directories for Okta, Slack identity, SSO, SCIM, provisioning, and directory questions.
- Do not claim access to private Slack workspaces, Okta tenants, or internal directories without authorized data.
- For enrichment, prefer official profiles, verified social accounts, employer pages, personal sites, and provider-managed identity references.
- Treat social posts about misconduct, trust, or reputation as public claims only. Capture them with source, date, and attribution, but do not convert them into facts without corroboration.
- Treat employment and life-event updates on attributable social profiles as important public signals for enrichment and ranking, especially for job loss, promotion, hiring, role changes, investments, launches, moves, marriage, and other major life events.
- When such signals come only from social media, label them as `reported publicly` unless corroborated by stronger sources.

## Logs And Audit Evidence

When the request involves internet transactions, account activity, investigations, or security-relevant behavior:

- treat audit logs, access logs, and network logs as high-value structured evidence when they are authorized or user-provided
- prioritize timestamp, actor, action, target, IP, device, session, request path, network endpoint, result, and status fields
- preserve raw event identifiers and log provenance alongside normalized interpretation
- correlate logs with official platform notices, provider docs, public incident reports, or workflow events when useful
- distinguish `observed event in logs` from `public claim` and from `inferred explanation`
- do not claim access to private logs unless the user supplied them or explicitly authorized the connected source

## Social Causes

- Use official nonprofit, NGO, coalition, campaign, charity, and foundation pages first.
- Use government, grant, research, and reputable news sources to validate causes, policy, funding, and public impact claims.
- Map organizations, campaigns, beneficiaries, sponsors, partners, and public advocates as distinct entities.

## Maps and Local

- Use Google Maps / local business search for places, local businesses, hotels, nearby results, and services.
- For local results, capture address, category, rating, hours, map link, and distance/area context when available.
- Treat map signals, location, and time as first-class ranking inputs for sort and filter decisions.

## Media and Content

- Use authoritative movie databases, studio/distributor pages, and streaming/catalog sources for movies.
- Use official artist/label/streaming/discography sources for music.
- Use official or authoritative publication pages for articles, books, reviews, and other creative works.

## Integration and Tooling

- Use official docs, registries, directories, repos, manifests, and app catalogs for integrations, actions, agents, skills, and MCPs.
- For automation questions, identify triggers, actions, auth, supported apps, required fields, and constraints.

## Data

- Use official statistical, regulatory, institutional, or company-reporting sources for datasets and metrics.
- Always capture timeframe, geography, unit, and methodology when those matter.

## Cause And Impact Analysis

When the user asks why something happened or how one event affected another:

- build a source-backed chain from upstream event to downstream effect
- prefer direct records such as loan status, payment history, workflow logs, notices, chats, and dated statements over narrative summaries
- capture intermediate states such as `disbursal_delayed`, `cash_shortfall`, `payment_missed`, or `service_interrupted`
- distinguish `causal hypothesis` from `observed sequence` and from `correlation`
- if the chain is incomplete, return the missing link explicitly instead of forcing a causal conclusion

## Risk And Incident Signals

When the query involves trust, misconduct, fraud, accidents, bans, or public safety:

- prefer official public databases, regulatory notices, court or enforcement announcements, platform policy notices, and reputable news coverage
- treat media coverage as evidence of reporting, not proof of underlying guilt or causation
- capture the exact type of signal, date, location, source, and current status
- separate `official action`, `reported incident`, `platform action`, and `public allegation`
- use public ban or suspension information only when it is explicitly published by the platform or otherwise strongly corroborated

## Employment And Life Event Signals

When the query depends on professional or personal milestones:

- capture public signals such as `new job`, `promotion`, `job loss`, `stepped down`, `raised funding`, `invested in`, `moved`, `married`, `engaged`, `joined board`, `launched`, or `graduated`
- treat attributable social-profile updates as meaningful evidence signals, especially when they come from the subject, employer, investor, or official organization account
- prefer corroboration from employer pages, official announcements, filings, or strong secondary coverage when available
- if the update remains social-only, preserve the signal with source, date, and confidence rather than discarding it

## Personal Chats And Impact Evidence

When the user provides or authorizes personal chats, direct messages, or message threads:

- treat them as sensitive evidence, not generic public content
- preserve speaker, time, platform, and conversation context when available
- use them to capture reported distress, impact, conflict, threats, coercion, or notable silence/non-response
- distinguish `reported feeling or impact in chat` from verified medical, legal, or psychological conclusions
- do not claim access to private chats unless the user supplied them or explicitly authorized the connected source

## Sort And Filter Attributes

When ranking or filtering results, prefer explicit attributes over vague relevance:

- `location`
- `distance`
- `time`
- `recency`
- `relevancy`
- `contextuality`
- `published_at`
- `event_time`
- `rating`
- `review_count`
- `source_tier`
- `verification_status`
- `platform`

For local, trust, and incident-style queries, location and time are especially important and should be surfaced prominently in the answer.

For log-driven queries, also prioritize:

- `ip_address`
- `network`
- `session_id`
- `request_path`
- `status_code`
- `actor`
- `target`
- `event_type`
- `log_source`

Use these ranking ideas consistently:

- `relevancy`: how directly the source/result matches the user’s requested subject or action
- `recency`: how recent the source or event is relative to the task
- `contextuality`: how well the source fits the exact context, such as place, relationship, industry, workspace, or incident pattern

Do not let a high-recency but weak-context source outrank a lower-recency, stronger-context source without explaining the tradeoff.

## Deduplication Heuristics

Compare in this order when possible:

1. exact identifiers
2. official domains and verified profile links
3. provider-managed identity records
4. employment, org, workspace, or campaign context
5. location and title consistency
6. handles, aliases, and display-name similarity

If the evidence is mixed, keep the records separate and mark the ambiguity.
