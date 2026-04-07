DEFINE TABLE thing SCHEMALESS;
DEFINE TABLE action SCHEMALESS;
DEFINE TABLE source SCHEMALESS;
DEFINE TABLE relation SCHEMALESS;

DEFINE INDEX idx_thing_name ON TABLE thing COLUMNS name;
DEFINE INDEX idx_thing_schema_type ON TABLE thing COLUMNS schema_type;
DEFINE INDEX idx_source_url ON TABLE source COLUMNS url UNIQUE;
DEFINE INDEX idx_relation_type ON TABLE relation COLUMNS type;
DEFINE INDEX idx_action_time ON TABLE action COLUMNS time;

-- Example inserts
-- CREATE thing:example CONTENT {
--   schema_type: "Organization",
--   name: "Example",
--   industries: ["software"]
-- };
--
-- CREATE relation:example CONTENT {
--   from: thing:example,
--   type: "integrates_with",
--   to: thing:slack,
--   confidence: "high"
-- };
