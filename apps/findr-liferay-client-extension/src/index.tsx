import React from "react";
import ReactDOM from "react-dom/client";

import { App } from "./App";

class FindrWebElement extends HTMLElement {
  connectedCallback() {
    const mountNode = document.createElement("div");
    this.appendChild(mountNode);
    ReactDOM.createRoot(mountNode).render(
      <React.StrictMode>
        <App />
      </React.StrictMode>,
    );
  }
}

if (!customElements.get("findr-web")) {
  customElements.define("findr-web", FindrWebElement);
}

const root = document.getElementById("root");
if (root) {
  root.innerHTML = "<findr-web></findr-web>";
}
