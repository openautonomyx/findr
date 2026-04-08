import type { SearchRequest, SearchResponse } from "./types";

export async function runSearch(payload: SearchRequest): Promise<SearchResponse> {
  const response = await fetch("/o/findr-api/search", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error(`Search failed with status ${response.status}`);
  }

  return response.json() as Promise<SearchResponse>;
}
