import { FormEvent, useEffect, useState } from "react";

import { getViewer, runSearch } from "./api";
import "./App.css";
import type { FinderRuntimeConfig, SearchResponse } from "./types";

const sampleQueries = [
  "Resolve Okta and its identity relationships",
  "Find public signals for a Bangalore software vendor",
  "Map Slack, Okta, and user account relationships",
  "Build a timeline of employment and funding events",
];

const capabilityCards = [
  {
    title: "Resolution",
    body: "Resolve people, companies, apps, places, and identity records into a structured profile.",
  },
  {
    title: "Evidence",
    body: "Rank sources by trust, recency, relevance, and context instead of flattening everything together.",
  },
  {
    title: "Graph",
    body: "Return linked entities, actions, sources, and timelines as graph-ready output for downstream systems.",
  },
  {
    title: "Operations",
    body: "Persist research into SurrealDB, index it in OpenSearch, and cache hot queries in Redis.",
  },
];

type AppProps = {
  config: FinderRuntimeConfig;
};

export function App({ config }: AppProps) {
  const [query, setQuery] = useState("");
  const [location, setLocation] = useState("");
  const [time, setTime] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<SearchResponse | null>(null);
  const [viewer, setViewer] = useState<string>(
    config.auth.userName || config.auth.userId || "anonymous",
  );

  async function loadViewer() {
    try {
      const response = await getViewer(config);
      if (!response.ok) {
        return;
      }
      const payload = (await response.json()) as {
        user_id: string;
        user_name?: string;
      };
      setViewer(payload.user_name || payload.user_id);
    } catch {
      // Keep the locally derived viewer when the API is unreachable.
    }
  }

  useEffect(() => {
    void loadViewer();
  }, []);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setLoading(true);
    setError(null);

    try {
      await loadViewer();
      const response = await runSearch(config, {
        query,
        search_mode: "standard_search",
        depth_mode: "fast pass",
        filters: {
          location: location || undefined,
          time: time || undefined,
        },
      });
      setResult(response);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Unknown search error");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="landing-shell">
      <section className="hero">
        <div className="hero-copy">
          <p className="eyebrow">AutonomyX Finder</p>
          <h1>Research, resolve, and connect the dots from a single investigation surface.</h1>
          <p className="hero-text">
            Finder unifies entity resolution, evidence-aware search, identity fabric mapping,
            source ranking, and graph-ready output for modern investigation workflows.
          </p>

          <div className="hero-meta">
            <div className="meta-chip">
              <span className="meta-label">Viewer</span>
              <strong>{viewer}</strong>
            </div>
            <div className="meta-chip">
              <span className="meta-label">Auth</span>
              <strong>{config.authMode}</strong>
            </div>
            <div className="meta-chip">
              <span className="meta-label">Route</span>
              <strong>{config.appBase}</strong>
            </div>
          </div>

          <div className="sample-list">
            {sampleQueries.map((sample) => (
              <button
                key={sample}
                className="sample-chip"
                onClick={() => setQuery(sample)}
                type="button"
              >
                {sample}
              </button>
            ))}
          </div>
        </div>

        <div className="search-panel">
          <div className="panel-header">
            <p className="panel-label">Investigation Query</p>
            <h2>Start from a subject, signal, or relationship.</h2>
          </div>

          <form className="search-form" onSubmit={handleSubmit}>
            <label className="field">
              <span>Query</span>
              <textarea
                value={query}
                onChange={(event) => setQuery(event.target.value)}
                placeholder="Find all public signals around a product, person, or identity relationship"
                required
                rows={4}
              />
            </label>

            <div className="field-grid">
              <label className="field">
                <span>Location</span>
                <input
                  value={location}
                  onChange={(event) => setLocation(event.target.value)}
                  placeholder="Bangalore"
                />
              </label>
              <label className="field">
                <span>Time</span>
                <input
                  value={time}
                  onChange={(event) => setTime(event.target.value)}
                  placeholder="last_90_days"
                />
              </label>
            </div>

            <button className="submit-button" disabled={loading} type="submit">
              {loading ? "Running search..." : "Run Finder"}
            </button>
          </form>

          {error ? <p className="error-banner">{error}</p> : null}
        </div>
      </section>

      <section className="capability-grid">
        {capabilityCards.map((card) => (
          <article key={card.title} className="capability-card">
            <p className="capability-title">{card.title}</p>
            <p>{card.body}</p>
          </article>
        ))}
      </section>

      <section className="architecture-strip">
        <div>
          <p className="strip-label">Frontend</p>
          <strong>React SPA</strong>
        </div>
        <div>
          <p className="strip-label">API</p>
          <strong>/api/v1</strong>
        </div>
        <div>
          <p className="strip-label">Data</p>
          <strong>SurrealDB + OpenSearch + Redis</strong>
        </div>
      </section>

      {result ? (
        <section className="results-section">
          <div className="results-header">
            <p className="eyebrow">Result</p>
            <h2>{result.summary}</h2>
          </div>

          <div className="results-grid">
            <article className="result-card">
              <h3>Schema Record</h3>
              <pre>{JSON.stringify(result.schema_record, null, 2)}</pre>
            </article>

            <article className="result-card">
              <h3>Sources</h3>
              <ul className="source-list">
                {result.sources.map((source) => (
                  <li key={source.url}>
                    <a href={source.url} rel="noreferrer" target="_blank">
                      {source.label}
                    </a>
                    <span>
                      tier {source.source_tier} • trust {source.trust_score}
                    </span>
                  </li>
                ))}
              </ul>
            </article>

            <article className="result-card result-card-wide">
              <h3>Knowledge Graph</h3>
              <pre>{JSON.stringify(result.knowledge_graph, null, 2)}</pre>
            </article>

            <article className="result-card result-card-wide">
              <h3>Trace</h3>
              <pre>{JSON.stringify(result.trace, null, 2)}</pre>
            </article>
          </div>
        </section>
      ) : (
        <section className="empty-state">
          <p className="eyebrow">Ready</p>
          <h2>No active investigation yet.</h2>
          <p>
            Use the query panel above to run a search and surface summary, source, graph, and
            trace output.
          </p>
        </section>
      )}
    </main>
  );
}
