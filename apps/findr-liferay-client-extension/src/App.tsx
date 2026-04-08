import { FormEvent, useState } from "react";

import { runSearch } from "./api";
import type { SearchResponse } from "./types";

const initialFilters = {
  location: "",
  time: "",
};

export function App() {
  const [query, setQuery] = useState("");
  const [location, setLocation] = useState(initialFilters.location);
  const [time, setTime] = useState(initialFilters.time);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<SearchResponse | null>(null);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const response = await runSearch({
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
