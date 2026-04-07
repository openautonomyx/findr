# Notifications

Use this reference when the workflow needs to propagate critical findings to downstream systems or people.

## Purpose

Notifications are for:

- critical incident awareness
- high-severity public-signal escalation
- operational alerting
- workflow handoff to downstream responders

They should be driven by structured evidence, not vague suspicion.

## Delivery Model

Keep the delivery layer simple:

- outbound `webhook`
- outbound `API`

Use them as propagation mechanisms, not as source-of-truth systems.

## Notification Trigger Conditions

Trigger notifications only when one or more of these are true:

- severity is high
- source trust is high enough
- the signal is corroborated
- the event is recent enough to matter operationally
- the result crosses a defined alert threshold

## Notification Payload

A notification payload should include:

- `alert_id`
- `title`
- `severity`
- `summary`
- `entity`
- `incident_type`
- `alert_type`
- `status`
- `source_of_information`
- `trust_score`
- `confidence`
- `relevancy`
- `recency`
- `contextuality`
- `time`
- `location`
- `recommended_action`
- `source_links`
- `knowledge_graph_ref`
- `schema_record_ref`

Example:

```json
{
  "alert_id": "alert:critical_public_signal_001",
  "title": "Critical public signal detected",
  "severity": "high",
  "summary": "Multiple high-trust public sources reported a new incident affecting the entity.",
  "entity": "thing:example",
  "incident_type": "regulatory_action",
  "alert_type": "critical_finding",
  "status": "open",
  "source_of_information": ["official_notice", "news_coverage"],
  "trust_score": 0.91,
  "confidence": "high",
  "relevancy": 0.95,
  "recency": 0.89,
  "contextuality": 0.84,
  "time": "2026-04-07T12:30:00Z",
  "location": "India",
  "recommended_action": "review_immediately",
  "source_links": ["https://example.com/notice"],
  "knowledge_graph_ref": "graph:example_1",
  "schema_record_ref": "thing:example"
}
```

## Escalation Rules

Use escalation tiers such as:

- `info`
- `warning`
- `high`
- `critical`

Escalation should consider:

- trust score
- confidence
- recency
- contextuality
- incident type
- affected geography
- number of corroborating sources

## Webhook Delivery

Use `webhook` when:

- the receiving system can accept a JSON payload
- the alert should be forwarded into an existing workflow engine
- the sender does not need delivery-state orchestration inside this skill

Recommended minimal fields:

- `url`
- `method`
- `headers`
- `payload`

## API Delivery

Use `API` delivery when:

- the downstream system expects an authenticated application call
- the alert should create or update a case, incident, or workflow object
- the receiver needs a stable typed contract

Recommended minimal fields:

- `endpoint`
- `method`
- `auth`
- `payload`

## Alert Types

Common alert types:

- `critical_finding`
- `risk_signal`
- `incident_update`
- `identity_conflict`
- `duplicate_review_required`
- `policy_or_compliance_event`
- `watchlist_change`

## Safety Rule

Do not generate high-severity alerts from a single low-trust or weakly attributable public signal.

Always preserve:

- provenance
- confidence
- source links
- whether the event is `official`, `reported_publicly`, or `unverified`
