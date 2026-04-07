# Taxonomy

Use these taxonomies to normalize the subject and graph.

Canonical reference for type expansion and subtype validation:

- `https://schema.org/docs/full.html`

## Schema Types

- Root: `Thing`
- Top-level: `Action`, `BioChemEntity`, `CreativeWork`, `Event`, `Intangible`, `MedicalEntity`, `Organization`, `Person`, `Place`, `Product`, `Taxon`

Common useful subtypes:

- `Person`: `Patient`
- `Organization`: `Airline`, `Consortium`, `Cooperative`, `Corporation`, `EducationalOrganization`, `FundingScheme`, `GovernmentOrganization`, `LibrarySystem`, `LocalBusiness`, `MedicalOrganization`, `NGO`, `NewsMediaOrganization`, `OnlineBusiness`, `PerformingGroup`, `PoliticalParty`, `Project`, `ResearchOrganization`, `SearchRescueOrganization`, `SportsOrganization`, `WorkersUnion`
- `Place`: `Accommodation`, `AdministrativeArea`, `ApartmentComplex`, `CivicStructure`, `DefinedRegion`, `GatedResidenceCommunity`, `Landform`, `LandmarksOrHistoricalBuildings`, `LocalBusiness`, `Residence`, `TouristAttraction`, `TouristDestination`
- `Product`: `DietarySupplement`, `Drug`, `IndividualProduct`, `ProductCollection`, `ProductGroup`, `ProductModel`, `SomeProducts`, `Vehicle`
- `CreativeWork`: `Article`, `Blog`, `Book`, `Course`, `Dataset`, `Episode`, `Guide`, `HowTo`, `Legislation`, `Map`, `MediaObject`, `Message`, `Movie`, `MusicComposition`, `MusicPlaylist`, `MusicRecording`, `Photograph`, `Review`, `SoftwareApplication`, `SoftwareSourceCode`, `TVSeason`, `TVSeries`, `WebContent`, `WebPage`, `WebSite`
- `Action`: `AchieveAction`, `AssessAction`, `ConsumeAction`, `ControlAction`, `CreateAction`, `FindAction`, `InteractAction`, `MoveAction`, `OrganizeAction`, `PlayAction`, `SearchAction`, `SeekToAction`, `SolveMathAction`, `TradeAction`, `TransferAction`, `UpdateAction`

Choose the most specific supported type. If unclear, choose the nearest stable parent type.

## Data Types

- `Boolean`
- `Date`
- `DateTime`
- `Number`
- `Quantity`
- `Text`
- `Time`

## Core Context Attributes

Treat these as first-class normalized attributes whenever available:

- `time`
- `date`
- `datetime`
- `published_at`
- `event_time`
- `location`
- `address`
- `geo_area`
- `distance`
- `timezone`
- `journey_path`
- `origin`
- `destination`
- `mode_of_transport`
- `relevancy`
- `recency`
- `contextuality`
- `incident_type`
- `risk_signal`
- `important_data_points`
- `employment_signal`
- `life_event_signal`
- `timeline`
- `timeseries_window`
- `correlation_score`
- `co_occurrence_score`
- `aligned_entities`
- `aligned_locations`
- `event_sequence`
- `state_transition`

Use them in schema records, action records, ranking, filtering, and graph nodes when they materially affect interpretation.

## Relation Taxonomy

Prefer these graph edge labels:

- Organization: `parent_of`, `subsidiary_of`, `owned_by`, `acquired`, `acquired_by`, `partner_of`, `vendor_to`, `customer_of`, `competes_with`, `integrates_with`, `member_of`, `affiliated_with`
- People and role: `employee_of`, `founder_of`, `cofounder_of`, `ceo_of`, `cto_of`, `board_member_of`, `advisor_to`, `reports_to`, `works_with`, `speaks_at`, `author_of`, `creator_of`
- Identity and account: `has_account`, `account_on`, `member_of_workspace`, `identity_managed_by`, `authenticated_via`, `provisioned_by`, `belongs_to_org`, `single_sign_on_with`, `directory_sync_with`, `scim_provisioned_by`, `trusts_identity_from`, `connected_identity`, `has_workspace`, `administers`
- Resolution and enrichment: `same_as`, `possible_duplicate_of`, `enriched_from`, `resolved_to`, `alias_of`, `has_identifier`, `has_profile`, `has_handle`
- Product and feature: `has_feature`, `part_of`, `depends_on`, `available_on`, `supports`, `uses`, `replaces`, `version_of`
- Media and content: `directed_by`, `starring`, `published_by`, `distributed_by`, `streaming_on`, `recorded_by`, `performed_by`, `mentions`, `references`, `cites`, `reviews`, `quotes`, `published_on`, `belongs_to_series`
- Local and commerce: `located_in`, `located_at`, `near`, `nearby_to`, `serves_area`, `serves`, `headquartered_in`, `bookable_via`, `sold_by`, `priced_at`
- Integration and capability: `has_trigger`, `has_action`, `authenticates_via`, `available_in`, `connects_to`, `automates`, `has_capability`, `supports_tool`, `installs_from`, `configured_by`, `uses_protocol`, `exposes_resource`, `exposes_tool`
- Evidence and classification: `documented_by`, `listed_in`, `categorized_as`, `requires_skill`, `operates_in_industry`
- Risk and incident: `reported_by`, `banned_by`, `sanctioned_by`, `accused_of`, `involved_in`, `affected_by`, `flagged_by`

## Action Record Taxonomy

When the query involves an incident, activity, allegation, workflow step, or notable behavior, normalize it into an action record.

Core action fields:

- `actor`
- `action_type`
- `object`
- `target`
- `time`
- `location`
- `journey_path`
- `mode_of_transport`
- `source`
- `source_tier`
- `confidence`
- `status`

Optional non-action fields:

- `non_action`
- `non_action_type`
- `expected_action`
- `absence_window`
- `absence_reason`

Log-derived event fields:

- `log_source`
- `event_id`
- `event_type`
- `session_id`
- `request_path`
- `ip_address`
- `network`
- `user_agent`
- `device`
- `status_code`
- `outcome`
- `raw_timestamp`
- `ingested_at`

Useful `action_type` examples:

- `created`
- `updated`
- `deleted`
- `posted`
- `commented`
- `reviewed`
- `reported`
- `visited`
- `purchased`
- `booked`
- `joined`
- `left`
- `partnered`
- `acquired`
- `integrated`
- `logged_in`
- `provisioned`
- `sent`
- `received`
- `non_action`

Useful `non_action_type` examples:

- `no_response`
- `no_acknowledgement`
- `no_login`
- `no_transaction`
- `no_movement`
- `no_update`
- `no_public_statement`
- `no_workflow_progress`

Useful `status` values:

- `verified`
- `reported_publicly`
- `unverified`
- `disputed`
- `official_action`
- `platform_action`
- `observed_absence`

## Audit And Workflow Log Taxonomy

Use these labels when the evidence comes from structured operational systems:

- `audit_log`
- `access_log`
- `network_access_log`
- `transaction_log`
- `workflow_log`
- `security_event_log`
- `identity_event_log`
- `application_activity_log`
- `incident_report`

Common log event types:

- `login`
- `logout`
- `authentication_failure`
- `password_reset`
- `mfa_challenge`
- `token_issued`
- `token_revoked`
- `account_created`
- `account_updated`
- `account_deleted`
- `permission_changed`
- `role_assigned`
- `resource_accessed`
- `file_downloaded`
- `api_called`
- `payment_attempted`
- `payment_completed`
- `payment_failed`
- `workflow_started`
- `workflow_step_completed`
- `workflow_failed`
- `session_started`
- `session_ended`
- `network_connection`
- `policy_violation_detected`

Treat these as observed system events when they come from logs, not as inferred narratives.

## Risk And Incident Taxonomy

Use normalized labels for public trust and incident signals.

### Incident types

- `fraud_report`
- `scam_report`
- `accident`
- `injury_incident`
- `suspension`
- `ban`
- `account_restriction`
- `lawsuit`
- `regulatory_action`
- `consumer_complaint`
- `policy_violation_report`

### Risk signals

- `public_database_match`
- `official_notice`
- `platform_notice`
- `news_coverage`
- `public_allegation`
- `repeated_complaints`

### Important data points

- `incident_count`
- `complaint_count`
- `ban_count`
- `report_count`
- `latest_incident_date`
- `latest_public_report_date`
- `affected_platform`
- `affected_region`
- `severity`

Treat these as structured public signals, not automatic proof of wrongdoing.

## Sensitive Message Evidence Taxonomy

Use these labels when the evidence comes from user-provided or authorized personal chats or direct messages:

- `personal_chat`
- `direct_message`
- `message_thread`
- `chat_excerpt`

Useful evidence labels:

- `reported_distress`
- `reported_psychological_impact`
- `reported_fear`
- `reported_harm`
- `reported_conflict`
- `reported_threat`
- `reported_coercion`
- `reported_non_response`

Treat these as reported message-level evidence. Do not upgrade them to medical, legal, or psychological fact without stronger corroboration.

## Employment And Life Event Taxonomy

Use normalized labels for milestone-like public updates.

### Employment signals

- `new_job`
- `promotion`
- `job_loss`
- `layoff`
- `resigned`
- `stepped_down`
- `joined_company`
- `left_company`
- `board_appointment`
- `investment_activity`
- `funding_event`

### Life event signals

- `marriage`
- `engagement`
- `relocation`
- `graduation`
- `birth`
- `death_notice`
- `public_relationship_update`

### Signal status

- `officially_confirmed`
- `reported_publicly`
- `social_only`
- `corroborated`
- `unverified`

Treat these as high-importance enrichment signals when they are attributable, even if they originate from social media.

## Timeseries And Correlation Taxonomy

Use these fields when the task involves multiple people, multiple timelines, multiple events, or cross-location temporal patterns.

### Timeseries fields

- `timeline`
- `event_sequence`
- `state_transition`
- `timeseries_window`
- `first_seen_at`
- `last_seen_at`

### Correlation fields

- `correlation_score`
- `co_occurrence_score`
- `pattern_type`
- `aligned_entities`
- `aligned_locations`
- `aligned_time_window`

### Pattern types

- `co_occurrence`
- `trend_alignment`
- `sequence_repeat`
- `state_change_alignment`
- `temporal_cluster`
- `cross_location_alignment`
- `journey_alignment`

Treat correlation as a pattern signal, not proof of causation.

## Cause And Impact Taxonomy

Use these fields when the task requires explicit cause analysis:

### Causal fields

- `cause_event`
- `effect_event`
- `intermediate_events`
- `causal_chain`
- `causal_link_type`
- `causal_confidence`
- `causal_evidence`
- `counterfactual_note`
- `missing_link`

### Causal link types

- `direct_dependency`
- `resource_constraint`
- `payment_dependency`
- `workflow_blockage`
- `service_interruption`
- `policy_constraint`
- `timing_dependency`
- `reported_impact`

### Example causal events

- `loan_not_disbursed`
- `cash_shortfall`
- `payment_failed`
- `school_fees_unpaid`
- `service_denied`
- `deadline_missed`

Treat causal analysis as a structured argument backed by dated evidence, not as automatic truth from sequence alone.

Prefer these schema-style action types when they fit:

- `Action`
- `AchieveAction`
- `LoseAction`
- `TieAction`
- `WinAction`
- `AssessAction`
- `ChooseAction`
- `IgnoreAction`
- `ReactAction`
- `ReviewAction`
- `ConsumeAction`
- `DrinkAction`
- `EatAction`
- `InstallAction`
- `ListenAction`
- `PlayGameAction`
- `ReadAction`
- `UseAction`
- `ViewAction`
- `WatchAction`
- `ControlAction`
- `ActivateAction`
- `AuthenticateAction`
- `DeactivateAction`
- `LoginAction`
- `ResetPasswordAction`
- `ResumeAction`
- `SuspendAction`
- `CreateAction`
- `CookAction`
- `DrawAction`
- `FilmAction`
- `PaintAction`
- `PhotographAction`
- `WriteAction`
- `FindAction`
- `CheckAction`
- `DiscoverAction`
- `TrackAction`
- `InteractAction`
- `BefriendAction`
- `CommunicateAction`
- `FollowAction`
- `JoinAction`
- `LeaveAction`
- `MarryAction`
- `RegisterAction`
- `SubscribeAction`
- `UnRegisterAction`
- `MoveAction`
- `ArriveAction`
- `DepartAction`
- `TravelAction`
- `OrganizeAction`
- `AllocateAction`
- `ApplyAction`
- `BookmarkAction`
- `PlanAction`
- `PlayAction`
- `ExerciseAction`
- `PerformAction`
- `SearchAction`
- `SeekToAction`
- `SolveMathAction`
- `TradeAction`
- `BuyAction`
- `OrderAction`
- `PayAction`
- `PreOrderAction`
- `QuoteAction`
- `RentAction`
- `SellAction`
- `TipAction`
- `TransferAction`
- `BorrowAction`
- `DonateAction`
- `DownloadAction`
- `GiveAction`
- `LendAction`
- `MoneyTransfer`
- `ReceiveAction`
- `ReturnAction`
- `SendAction`
- `TakeAction`
- `UpdateAction`
- `AddAction`
- `DeleteAction`
- `ReplaceAction`

Use the closest specific action type that the evidence supports. If none fit cleanly, keep a simpler normalized `action_type` value.

## Job Profile Taxonomy

Core fields:

- `job_title`
- `seniority`
- `function`
- `department`
- `employer`
- `employment_type`
- `location`
- `current_or_former`
- `public_profile_source`

Common seniority:

- `intern`, `junior`, `mid`, `senior`, `staff`, `principal`, `lead`, `manager`, `director`, `vp`, `c_level`, `founder`

Common functions:

- `engineering`, `product`, `design`, `sales`, `marketing`, `operations`, `finance`, `legal`, `hr`, `support`, `research`, `data`, `security`, `it`

Common employment types:

- `full_time`, `part_time`, `contract`, `consulting`, `freelance`, `advisor`, `board`

## Industry Taxonomy

Common industries:

- `software`, `saas`, `ai`, `fintech`, `healthcare`, `biotech`, `edtech`, `ecommerce`, `retail`, `manufacturing`, `logistics`, `transportation`, `travel`, `hospitality`, `media`, `gaming`, `telecom`, `cybersecurity`, `cloud`, `devtools`, `hrtech`, `legaltech`, `proptech`, `govtech`, `climate`, `energy`, `agriculture`, `real_estate`, `automotive`, `sports`, `entertainment`, `nonprofit`, `research`

## Skills Taxonomy

Technical:

- `python`, `javascript`, `typescript`, `sql`, `machine_learning`, `data_analysis`, `cloud_architecture`, `devops`, `security`, `api_design`, `integration_automation`, `frontend`, `backend`, `mobile_development`, `data_engineering`

Business:

- `sales`, `marketing`, `product_management`, `customer_success`, `operations`, `finance`, `procurement`, `vendor_management`, `partnerships`, `program_management`

Creative and research:

- `writing`, `editing`, `design`, `ux_research`, `market_research`, `technical_research`, `teaching`, `public_speaking`

## Resolution Confidence

- `high`: multiple stable identifiers or official links agree
- `medium`: strong contextual match, but no single definitive identifier
- `low`: weak or partial evidence only

Do not present `medium` or `low` confidence matches as definite merges.
