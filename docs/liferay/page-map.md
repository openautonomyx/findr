# Liferay Page Map

Target base path:

```text
https://www.openautonomyx.com/web/findr
```

## Primary Pages

### `/web/findr`

Purpose:

- product overview
- primary search entry
- recent investigations
- docs and download links

Primary widgets:

- hero/search bar
- search mode picker
- featured use cases
- release/download panel
- recent alerts summary

### `/web/findr/search`

Purpose:

- submit search, resolution, enrichment, or investigation queries

Primary widgets:

- query input
- mode selector
- filters
- evidence/source controls
- fast vs deep research selector

### `/web/findr/results/{jobId}`

Purpose:

- render result summary and machine-readable output

Primary widgets:

- narrative answer
- schema record
- knowledge graph
- sources and trust indicators
- traces
- export actions

### `/web/findr/cases`

Purpose:

- saved investigations
- reviewer workflow
- case status tracking

Primary widgets:

- case list
- filters by status and owner
- case detail side panel

### `/web/findr/cases/{caseId}`

Purpose:

- investigation review and collaboration

Primary widgets:

- case summary
- evidence table
- graph/timeline tabs
- notes
- decision and approval actions

### `/web/findr/alerts`

Purpose:

- review critical findings and propagation status

Primary widgets:

- alert feed
- severity filters
- webhook/API delivery status
- escalation details

### `/web/findr/admin`

Purpose:

- operational and policy controls

Primary widgets:

- source policy management
- taxonomy settings
- alert threshold settings
- API key / integration settings
- role and permission mapping

## Recommended Liferay Implementation

Use a Liferay client extension or custom module with:

- React frontend
- role-aware route rendering
- API calls to `/o/findr-api`

Recommended roles:

- `findr-user`
- `findr-analyst`
- `findr-reviewer`
- `findr-admin`
