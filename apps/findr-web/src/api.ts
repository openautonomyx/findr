import type { FinderRuntimeConfig, SearchRequest, SearchResponse } from "./types";

export async function getViewer(config: FinderRuntimeConfig): Promise<Response> {
  return fetch(`${config.apiBase}/o/findr-api/me`, {
    method: "GET",
    headers: buildAuthHeaders(config),
  });
}

export async function runSearch(
  config: FinderRuntimeConfig,
  payload: SearchRequest,
): Promise<SearchResponse> {
  const response = await fetch(`${config.apiBase}/o/findr-api/search`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...buildAuthHeaders(config),
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error(`Search failed with status ${response.status}`);
  }

  return response.json() as Promise<SearchResponse>;
}

function buildAuthHeaders(config: FinderRuntimeConfig): Record<string, string> {
  if (config.authMode !== "browserHeaders") {
    return {};
  }
  const headers: Record<string, string> = {};
  if (config.auth.userId) {
    headers["X-Findr-User-Id"] = config.auth.userId;
  }
  if (config.auth.userName) {
    headers["X-Findr-User-Name"] = config.auth.userName;
  }
  if (config.auth.roles.length > 0) {
    headers["X-Findr-Roles"] = config.auth.roles.join(",");
  }
  if (config.auth.sharedSecret) {
    headers["X-Findr-Shared-Secret"] = config.auth.sharedSecret;
  }
  return headers;
}
