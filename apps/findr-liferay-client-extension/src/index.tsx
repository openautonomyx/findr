import React from "react";
import ReactDOM from "react-dom/client";

import { App } from "./App";
import type { FinderRuntimeConfig } from "./types";

declare global {
  interface Window {
    Liferay?: {
      ThemeDisplay?: {
        getUserId?: () => string;
        getUserName?: () => string;
      };
      FINDR_CONFIG?: Partial<{
        apiBase: string;
        appBase: string;
        authMode: "proxy" | "browserHeaders";
        sharedSecret: string;
        roles: string[];
      }>;
    };
  }
}

class FindrWebElement extends HTMLElement {
  connectedCallback() {
    const mountNode = document.createElement("div");
    this.appendChild(mountNode);

    const config = deriveRuntimeConfig(this);

    ReactDOM.createRoot(mountNode).render(
      <React.StrictMode>
        <App config={config} />
      </React.StrictMode>,
    );
  }
}

function deriveRuntimeConfig(element: HTMLElement): FinderRuntimeConfig {
  const globalConfig = window.Liferay?.FINDR_CONFIG ?? {};
  const themeDisplay = window.Liferay?.ThemeDisplay;
  const datasetRoles = element.dataset.roles?.split(",").map((role) => role.trim()).filter(Boolean);
  const globalRoles = globalConfig.roles?.filter(Boolean);

  return {
    apiBase:
      element.dataset.apiBase ||
      globalConfig.apiBase ||
      (import.meta.env.VITE_FINDR_API_BASE as string | undefined) ||
      "",
    appBase:
      element.dataset.appBase ||
      globalConfig.appBase ||
      (import.meta.env.VITE_FINDR_APP_BASE as string | undefined) ||
      "/web/findr",
    authMode:
      (element.dataset.authMode as "proxy" | "browserHeaders" | undefined) ||
      globalConfig.authMode ||
      ((import.meta.env.VITE_FINDR_AUTH_MODE as "proxy" | "browserHeaders" | undefined) ??
        "proxy"),
    auth: {
      userId:
        element.dataset.userId ||
        themeDisplay?.getUserId?.() ||
        "anonymous",
      userName:
        element.dataset.userName ||
        themeDisplay?.getUserName?.() ||
        undefined,
      roles:
        datasetRoles ||
        globalRoles ||
        ["findr-user"],
      sharedSecret:
        element.dataset.sharedSecret ||
        globalConfig.sharedSecret ||
        (import.meta.env.VITE_FINDR_SHARED_SECRET as string | undefined) ||
        undefined,
    },
  };
}

if (!customElements.get("findr-web")) {
  customElements.define("findr-web", FindrWebElement);
}

const root = document.getElementById("root");
if (root) {
  root.innerHTML = "<findr-web></findr-web>";
}
