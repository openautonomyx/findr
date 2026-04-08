import { FormEvent, useEffect, useState } from "react";

import { getViewer, runSearch } from "./api";
import type { FinderRuntimeConfig, SearchResponse } from "./types";

const initialFilters = {
  location: "",
  time: "",
};

type AppProps = {
  config: FinderRuntimeConfig;
};

export function App({ config }: AppProps) {
  const [query, setQuery] = useState("");
  const [location, setLocation] = useState(initialFilters.location);
  const [time, setTime] = useState(initialFilters.time);
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
    <main style={{ fontFamily: "sans-serif", margin: "0 auto", maxWidth: 960, padding: 24 }}>
      <h1>AutonomyX Finder</h1>
      <p>Investigate entities, enrich evidence, and render graph-ready answers.</p>
      <p style={{ color: "#555", marginTop: 8 }}>
        Viewer: <strong>{viewer}</strong>
      </p>

      <form onSubmit={handleSubmit} style={{ display: "grid", gap: 12, marginTop: 24 }}>
        <input
          value={query}
          onChange={(event) => setQuery(event.target.value)}
          placeholder="Search query"
          required
        />
        <input
          value={location}
          onChange={(event) => setLocation(event.target.value)}
          placeholder="Location filter"
        />
        <input
          value={time}
          onChange={(event) => setTime(event.target.value)}
          placeholder="Time filter"
        />
        <button disabled={loading} type="submit">
          {loading ? "Searching..." : "Search"}
        </button>
      </form>

      {error ? <p style={{ color: "crimson" }}>{error}</p> : null}

      {result ? (
        <section style={{ marginTop: 32 }}>
          <h2>Summary</h2>
          <p>{result.summary}</p>

          <h3>Schema Record</h3>
          <pre>{JSON.stringify(result.schema_record, null, 2)}</pre>

          <h3>Sources</h3>
          <ul>
            {result.sources.map((source) => (
              <li key={source.url}>
                <a href={source.url} rel="noreferrer" target="_blank">
                  {source.label}
                </a>{" "}
                tier {source.source_tier} trust {source.trust_score}
              </li>
            ))}
          </ul>

          <h3>Knowledge Graph</h3>
          <pre>{JSON.stringify(result.knowledge_graph, null, 2)}</pre>

          <h3>Trace</h3>
          <pre>{JSON.stringify(result.trace, null, 2)}</pre>
        </section>
      ) : null}
    </main>
  );
}
