# Findr

Find anything, anywhere on the web. AI-powered search engine.

## Features

- **Universal Search** - Search across all web content
- **Semantic Matching** - Understands intent, not just keywords
- **Real-time Results** - Live web indexing
- **Filters** - By date, source, type, language

## API

```
GET /api/v1/search?q=query
```

## Quick Start

```bash
curl "https://api.openautonomyx.com/api/v1/search?q=AI+agents"
```

## Response

```json
{
  "results": [
    { "title": "AI Agents Guide", "url": "...", "snippet": "...", "score": 0.95 }
  ],
  "total": 1543
}
```

---

**Repository:** [openautonomyx/findr](https://github.com/openautonomyx/findr)