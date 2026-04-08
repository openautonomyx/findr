export type SearchRequest = {
  query: string;
  search_mode: string;
  depth_mode: string;
  filters: {
    location?: string;
    time?: string;
    source_tier?: number;
    schema_type?: string;
  };
};

export type FinderAuthContext = {
  userId: string;
  userName?: string;
  roles: string[];
  sharedSecret?: string;
};

export type FinderRuntimeConfig = {
  apiBase: string;
  appBase: string;
  auth: FinderAuthContext;
};

export type SearchResponse = {
  search_mode: string;
  schema_type: string;
  summary: string;
  schema_record: Record<string, unknown>;
  knowledge_graph: {
    nodes: Array<Record<string, unknown>>;
    edges: Array<Record<string, unknown>>;
  };
  sources: Array<{
    label: string;
    url: string;
    source_tier: number;
    trust_score: number;
  }>;
  trace: Record<string, unknown>;
};
