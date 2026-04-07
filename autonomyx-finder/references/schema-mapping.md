# Schema Mapping

Use this file to separate:

- native `schema.org` properties
- normalized taxonomy values
- custom extension fields used by this skill

This is the bridge between:

- `schema.org`
- normalized skill output
- `SurrealDB` storage fields

## Mapping Rules

1. Use the native `schema.org` property when it exists and fits.
2. Use a normalized taxonomy value when the property exists but the value needs standardization.
3. Use a custom extension field when `schema.org` does not model the requirement well enough.
4. Keep custom fields clearly named and stable for storage.

## Core Field Mapping

| Logical field | schema.org property/type | Custom extension | Storage key |
|---|---|---:|---|
| name | `name` | no | `name` |
| legal name | `legalName` or `name` | sometimes | `legal_name` |
| alternate name | `alternateName` | no | `alternate_names` |
| description | `description` | no | `description` |
| official website | `url` | no | `url` |
| profile link | `sameAs` | no | `profiles` |
| identifier | `identifier` | no | `identifiers` |
| email | `email` | no | `email` |
| phone | `telephone` | no | `telephone` |
| image | `image` | no | `image` |
| logo | `logo` | no | `logo` |
| brand | `brand` | no | `brand` |
| knows about | `knowsAbout` | no | `knows_about` |
| subject type | `@type` | no | `schema_type` |

## Person And Employment Mapping

| Logical field | schema.org property/type | Custom extension | Storage key |
|---|---|---:|---|
| person | `Person` | no | `schema_type=Person` |
| job title | `jobTitle` | no | `job_title` |
| works for | `worksFor` | no | `works_for` |
| member of | `memberOf` | no | `member_of` |
| alumni of | `alumniOf` | no | `alumni_of` |
| affiliation | `affiliation` | no | `affiliation` |
| award | `award` | no | `awards` |
| birth date | `birthDate` | no | `birth_date` |
| death date | `deathDate` | no | `death_date` |
| nationality | `nationality` | no | `nationality` |
| seniority | no strong native field | yes | `seniority` |
| employment type | no strong native field | yes | `employment_type` |
| current/former | partial via dates | yes | `current_or_former` |
| employment signal | no | yes | `employment_signal` |
| life event signal | no | yes | `life_event_signal` |

## Organization Mapping

| Logical field | schema.org property/type | Custom extension | Storage key |
|---|---|---:|---|
| organization | `Organization` | no | `schema_type=Organization` |
| founding date | `foundingDate` | no | `founding_date` |
| founder | `founder` | no | `founders` |
| parent organization | `parentOrganization` | no | `parent_organization` |
| sub organization | `subOrganization` | no | `sub_organizations` |
| number of employees | `numberOfEmployees` | no | `employee_count` |
| department | `department` | no | `departments` |
| slogan | `slogan` | no | `slogan` |
| duns | `duns` | no | `duns` |
| naics | `naics` | no | `naics` |
| global location number | `globalLocationNumber` | no | `gln` |
| industry | weak/native-adjacent | yes | `industries` |
| trust signals | no | yes | `brand_trust_signals` |

## Place And Address Mapping

| Logical field | schema.org property/type | Custom extension | Storage key |
|---|---|---:|---|
| place | `Place` | no | `schema_type=Place` |
| location | `location` | partial | `location` |
| address | `address` | no | `address` |
| street | `streetAddress` | no | `street_address` |
| city | `addressLocality` | no | `city` |
| region/state | `addressRegion` | no | `region` |
| postal code | `postalCode` | no | `postal_code` |
| country | `addressCountry` | no | `country` |
| geo | `geo` | no | `geo` |
| latitude | `latitude` | no | `latitude` |
| longitude | `longitude` | no | `longitude` |
| geo area | no | yes | `geo_area` |
| distance | no | yes | `distance` |
| nearby relation | no | yes | `nearby_to` |

## Product / Application Mapping

| Logical field | schema.org property/type | Custom extension | Storage key |
|---|---|---:|---|
| product | `Product` | no | `schema_type=Product` |
| software app | `SoftwareApplication` | no | `schema_type=SoftwareApplication` |
| category | `category` | no | `category` |
| operating system | `operatingSystem` | no | `operating_system` |
| application category | `applicationCategory` | no | `application_category` |
| feature list | `featureList` | no | `feature_list` |
| offers/pricing | `offers` | no | `offers` |
| aggregate rating | `aggregateRating` | no | `aggregate_rating` |
| review | `review` | no | `reviews` |
| application sub type | partial | yes | `application_type` |

## Action Mapping

| Logical field | schema.org property/type | Custom extension | Storage key |
|---|---|---:|---|
| action type | `Action` and subtypes | no | `action_type` |
| object | `object` | no | `object` |
| result | `result` | no | `result` |
| instrument | `instrument` | no | `instrument` |
| participant | `participant` | no | `participants` |
| agent/actor | `agent` | no | `actor` |
| target | `target` | partial | `target` |
| start time | `startTime` | no | `start_time` |
| end time | `endTime` | no | `end_time` |
| location | `location` | no | `location` |
| action status | `actionStatus` | partial | `status` |
| event time | partial | yes | `event_time` |
| journey path | no | yes | `journey_path` |
| mode of transport | no | yes | `mode_of_transport` |
| non action flag | no | yes | `non_action` |
| non action type | no | yes | `non_action_type` |
| expected action | no | yes | `expected_action` |
| absence window | no | yes | `absence_window` |
| absence reason | no | yes | `absence_reason` |

## Media / Creative Work Mapping

| Logical field | schema.org property/type | Custom extension | Storage key |
|---|---|---:|---|
| movie | `Movie` | no | `schema_type=Movie` |
| music recording | `MusicRecording` | no | `schema_type=MusicRecording` |
| author | `author` | no | `author` |
| creator | `creator` | no | `creator` |
| publisher | `publisher` | no | `publisher` |
| date published | `datePublished` | no | `published_at` |
| date created | `dateCreated` | no | `created_at` |
| genre | `genre` | no | `genre` |
| duration | `duration` | no | `duration` |
| actor/cast | `actor` | no | `cast` |
| director | `director` | no | `director` |

## Source And Evidence Mapping

| Logical field | schema.org property/type | Custom extension | Storage key |
|---|---|---:|---|
| source url | `url` | no | `source_url` |
| source publisher | `publisher` | no | `source_publisher` |
| date published | `datePublished` | no | `published_at` |
| citation/reference | `citation` | no | `citations` |
| review item | `review` / `MediaReviewItem` | partial | `review_item` |
| source tier | no | yes | `source_tier` |
| source of information | no | yes | `source_of_information` |
| trust score | no | yes | `trust_score` |
| evidence class | no | yes | `evidence_type` |
| message source type | no | yes | `message_source_type` |
| speaker | no | yes | `speaker` |
| conversation id | no | yes | `conversation_id` |
| message id | no | yes | `message_id` |
| reported impact | no | yes | `reported_impact` |
| log source | no | yes | `log_source` |
| event id | no | yes | `event_id` |
| session id | no | yes | `session_id` |
| ip address | no | yes | `ip_address` |
| network | no | yes | `network` |
| request path | no | yes | `request_path` |
| status code | no | yes | `status_code` |
| user agent | no | yes | `user_agent` |
| device | no | yes | `device` |
| outcome | no | yes | `outcome` |
| ingested at | no | yes | `ingested_at` |

## Resolution And Ranking Mapping

| Logical field | schema.org property/type | Custom extension | Storage key |
|---|---|---:|---|
| same entity link | `sameAs` | partial | `same_as` |
| duplicate candidate | no | yes | `possible_duplicate_of` |
| resolution result | no | yes | `resolution` |
| confidence | no | yes | `confidence` |
| recommended action | no | yes | `recommended_action` |
| relevancy | no | yes | `relevancy` |
| recency | no | yes | `recency` |
| contextuality | no | yes | `contextuality` |
| correlation score | no | yes | `correlation_score` |
| co-occurrence score | no | yes | `co_occurrence_score` |

## Brand Mapping

| Logical field | schema.org property/type | Custom extension | Storage key |
|---|---|---:|---|
| brand | `brand` | no | `brand` |
| brand name | via `Brand` + `name` | partial | `brand_name` |
| brand type | no | yes | `brand_type` |
| brand positioning | no | yes | `brand_positioning` |
| brand voice | no | yes | `brand_voice` |
| brand tone | no | yes | `brand_tone` |
| brand trust signals | no | yes | `brand_trust_signals` |

## Topic / Skill / Industry Mapping

| Logical field | schema.org property/type | Custom extension | Storage key |
|---|---|---:|---|
| knows about / topics | `knowsAbout` | partial | `topics` |
| skills | no strong native field | yes | `skills` |
| skill level | no | yes | `skill_level` |
| sfia level | no | yes | `sfia_level` |
| industry | weak/native-adjacent | yes | `industries` |

## Important Notes

- Prefer native `schema.org` fields whenever they fit the meaning exactly.
- Use custom extensions for ranking, trust, resolution, traversal, deduplication, and analytics fields.
- Keep custom fields stable and documented for SurrealDB ingestion.
- Do not force every custom field into a fake schema.org mapping if the semantic fit is poor.
