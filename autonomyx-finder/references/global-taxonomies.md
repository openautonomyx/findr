# Global Taxonomies

Use this file when the user wants broad normalization across entities, relations, roles, skills, brands, topics, and storage.

Store taxonomy-aligned values in SurrealDB as normalized labels, arrays, and edge types rather than freeform prose whenever possible.

## Relation Taxonomy

Use normalized edge labels for graph consistency.

### Identity and account

- `same_as`
- `possible_duplicate_of`
- `resolved_to`
- `alias_of`
- `has_identifier`
- `has_profile`
- `has_handle`
- `has_account`
- `account_on`
- `identity_managed_by`
- `authenticated_via`
- `single_sign_on_with`
- `directory_sync_with`
- `scim_provisioned_by`
- `member_of_workspace`
- `belongs_to_org`
- `connected_identity`

### Organization and business

- `parent_of`
- `subsidiary_of`
- `owned_by`
- `acquired`
- `acquired_by`
- `partner_of`
- `vendor_to`
- `customer_of`
- `competes_with`
- `operates_in_industry`
- `listed_in`
- `documented_by`

### Product and platform

- `has_feature`
- `part_of`
- `depends_on`
- `available_on`
- `supports`
- `uses`
- `replaces`
- `version_of`
- `integrates_with`
- `has_trigger`
- `has_action`
- `automates`
- `supports_tool`
- `uses_protocol`
- `exposes_tool`
- `exposes_resource`

### People and professional

- `employee_of`
- `founder_of`
- `cofounder_of`
- `ceo_of`
- `cto_of`
- `board_member_of`
- `advisor_to`
- `reports_to`
- `works_with`
- `has_title`
- `has_seniority`
- `works_in_function`
- `has_skill`
- `worked_at`

### Local, media, and evidence

- `located_in`
- `located_at`
- `near`
- `nearby_to`
- `serves_area`
- `bookable_via`
- `sold_by`
- `priced_at`
- `published_by`
- `distributed_by`
- `streaming_on`
- `recorded_by`
- `performed_by`
- `mentions`
- `references`
- `cites`
- `reviews`
- `quotes`

## Skill Level Taxonomy

Use this when describing proficiency or role maturity.

### Generic levels

- `awareness`
- `basic`
- `working`
- `practitioner`
- `advanced`
- `expert`
- `authority`

### SFIA-aligned levels

Use compact normalized values:

- `sfia_1_follow`
- `sfia_2_assist`
- `sfia_3_apply`
- `sfia_4_enable`
- `sfia_5_ensure_advise`
- `sfia_6_initiate_influence`
- `sfia_7_set_strategy_inspire_mobilise`

Store both when helpful:

```json
{
  "skill_level": "advanced",
  "sfia_level": "sfia_5_ensure_advise"
}
```

## Skill Taxonomy

Normalize skills into stable buckets.

### Engineering and data

- `python`
- `javascript`
- `typescript`
- `sql`
- `java`
- `go`
- `rust`
- `api_design`
- `backend`
- `frontend`
- `mobile_development`
- `data_engineering`
- `data_analysis`
- `machine_learning`
- `cloud_architecture`
- `devops`
- `security`
- `integration_automation`

### Product and business

- `product_management`
- `program_management`
- `sales`
- `marketing`
- `customer_success`
- `operations`
- `finance`
- `procurement`
- `vendor_management`
- `partnerships`

### Research and creative

- `technical_research`
- `market_research`
- `ux_research`
- `writing`
- `editing`
- `design`
- `teaching`
- `public_speaking`

### Domain and trust

- `identity_management`
- `sso`
- `scim`
- `compliance`
- `risk_analysis`
- `fraud_detection`
- `trust_and_safety`
- `background_verification`
- `entity_resolution`
- `knowledge_graph_modeling`

## Brand Taxonomy

Use brand attributes when the user cares about identity, market position, or reputation.

### Core brand fields

- `brand_name`
- `brand_architecture`
- `brand_type`
- `brand_positioning`
- `brand_voice`
- `brand_tone`
- `brand_values`
- `brand_trust_signals`
- `brand_region`
- `brand_audience`

### Brand type

- `corporate_brand`
- `product_brand`
- `employer_brand`
- `personal_brand`
- `house_of_brands`
- `branded_house`

### Brand trust signals

- `verified_profile`
- `official_domain`
- `press_coverage`
- `case_studies`
- `customer_reviews`
- `certifications`
- `security_compliance`
- `community_presence`

## Topic Taxonomy

Use topics as normalized tags instead of vague categories.

### Technology

- `artificial_intelligence`
- `identity`
- `cybersecurity`
- `cloud_computing`
- `developer_tools`
- `data_platforms`
- `automation`
- `saas`

### Business

- `go_to_market`
- `procurement`
- `partnerships`
- `customer_success`
- `vendor_risk`
- `compliance`
- `trust_and_safety`

### Society and public-interest

- `social_causes`
- `public_policy`
- `education`
- `healthcare`
- `climate`
- `nonprofit`
- `human_rights`
- `community_safety`

### Media and culture

- `movies`
- `music`
- `gaming`
- `sports`
- `news`
- `publishing`

## Mobility And Journey Taxonomy

Use this when the query involves movement, travel, route reconstruction, or transport behavior.

### Core mobility attributes

- `origin`
- `destination`
- `journey_path`
- `waypoints`
- `mode_of_transport`
- `departure_time`
- `arrival_time`
- `travel_duration`
- `distance`
- `geo_area`

### Common transport modes

- `walking`
- `running`
- `cycling`
- `motorbike`
- `car`
- `taxi`
- `bus`
- `train`
- `metro`
- `tram`
- `flight`
- `boat`
- `rideshare`
- `freight`
- `mixed_mode`

### Journey relations

- `originated_at`
- `departed_from`
- `arrived_at`
- `traveled_via`
- `passed_through`
- `moved_to`
- `returned_to`
- `used_transport_mode`

### Journey status

- `planned`
- `in_progress`
- `completed`
- `reported_publicly`
- `estimated`
- `verified`

Use these labels only when location/time/path evidence supports them.

## Multi-Entity Timeline Taxonomy

Use this when comparing multiple people, multiple timelines, and multiple events.

### Timeline grouping keys

- `entity`
- `entity_group`
- `event_type`
- `location_group`
- `time_window`

### Multi-entity analysis fields

- `timeline`
- `event_sequence`
- `aligned_entities`
- `aligned_locations`
- `aligned_time_window`
- `correlation_score`
- `co_occurrence_score`
- `pattern_type`

### Pattern examples

- `temporal_cluster`
- `cross_location_alignment`
- `sequence_repeat`
- `state_change_alignment`
- `journey_alignment`

Use these fields to compare groups without collapsing distinct entities into one timeline.

## Causal Analysis Taxonomy

Use this when the user wants cause-and-effect chains across finances, actions, timelines, or workflows.

### Causal analysis fields

- `cause_event`
- `effect_event`
- `intermediate_events`
- `causal_chain`
- `causal_link_type`
- `causal_confidence`
- `causal_evidence`
- `missing_link`

### Common causal link types

- `resource_constraint`
- `payment_dependency`
- `workflow_blockage`
- `timing_dependency`
- `service_interruption`
- `reported_impact`

## Industry Taxonomy

Use one or more normalized industries only when supported by evidence.

- `software`
- `saas`
- `ai`
- `fintech`
- `healthcare`
- `biotech`
- `edtech`
- `ecommerce`
- `retail`
- `manufacturing`
- `logistics`
- `transportation`
- `travel`
- `hospitality`
- `media`
- `gaming`
- `telecom`
- `cybersecurity`
- `cloud`
- `devtools`
- `hrtech`
- `legaltech`
- `proptech`
- `govtech`
- `climate`
- `energy`
- `agriculture`
- `real_estate`
- `automotive`
- `sports`
- `entertainment`
- `nonprofit`
- `research`

## Storage Guidance

When storing taxonomy data in SurrealDB:

- store stable labels, not long prose
- keep arrays normalized and lowercase with underscores
- store relation types as explicit edge values
- keep source evidence separate from normalized facts
- store confidence beside any inferred or resolved label

Example:

```json
{
  "id": "thing:person_1",
  "schema_type": "Person",
  "industries": ["software", "identity"],
  "skills": [
    {"name": "identity_management", "skill_level": "advanced", "sfia_level": "sfia_5_ensure_advise"},
    {"name": "python", "skill_level": "practitioner", "sfia_level": "sfia_4_enable"}
  ],
  "topics": ["identity", "trust_and_safety"],
  "brand": {
    "brand_type": "personal_brand",
    "brand_trust_signals": ["verified_profile", "official_domain"]
  }
}
```
