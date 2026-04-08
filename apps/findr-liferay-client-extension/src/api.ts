import type { SearchRequest, SearchResponse } from "./types";

const apiBase = (import.meta.env.VITE_FINDR_API_BASE as string | undefined) ?? "";

export async function runSearch(payload: SearchRequest): Promise<SearchResponse> {
  const response = await fetch(`${apiBase}/o/findr-api/search`, {
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
