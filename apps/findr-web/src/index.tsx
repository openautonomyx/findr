import React from "react";
import ReactDOM from "react-dom/client";

import { App } from "./App";
import type { FinderRuntimeConfig } from "./types";

function deriveRuntimeConfig(): FinderRuntimeConfig {
  const urlParams = new URLSearchParams(window.location.search);

  return {
    apiBase:
      (import.meta.env.VITE_FINDR_API_BASE as string | undefined) ||
      window.location.origin,
    appBase:
      (import.meta.env.VITE_FINDR_APP_BASE as string | undefined) || "/",
    authMode:
      (import.meta.env.VITE_FINDR_AUTH_MODE as "proxy" | "browserHeaders" | undefined) ||
      "proxy",
    auth: {
      userId:
        urlParams.get("user") ||
        localStorage.getItem("findr:user_id") ||
        "anonymous",
      userName:
        urlParams.get("name") ||
        localStorage.getItem("findr:user_name") ||
        undefined,
      roles: (localStorage.getItem("findr:roles") || "findr-user")
        .split(",")
        .map((role) => role.trim())
        .filter(Boolean),
      sharedSecret:
        (import.meta.env.VITE_FINDR_SHARED_SECRET as string | undefined) ||
        undefined,
    },
  };
}

const root = document.getElementById("root");
if (root) {
  ReactDOM.createRoot(root).render(
    <React.StrictMode>
      <App config={deriveRuntimeConfig()} />
    </React.StrictMode>,
  );
}
