# Liferay Auth Proxy

Use a same-origin proxy for production so the browser does not carry the Finder shared secret directly.

## Recommended Flow

```text
Browser
  -> /web/findr
  -> Liferay page renders client extension
  -> Browser calls /o/findr-api/*
  -> trusted proxy injects Finder headers
  -> Finder API validates headers and shared secret
```

## Runtime Config on the Page

Expose non-secret runtime config on the page:

```html
<script>
  window.Liferay = window.Liferay || {};
  window.Liferay.FINDR_CONFIG = {
    apiBase: "https://www.openautonomyx.com",
    appBase: "/web/findr",
    authMode: "proxy",
    roles: ["findr-analyst"]
  };
</script>
```

Do not place a long-lived shared secret in this object for production.

## Trusted Proxy Example

Example reverse proxy behavior:

- read the authenticated Liferay session or upstream identity
- map portal roles to Finder roles
- inject:
  - `X-Findr-User-Id`
  - `X-Findr-User-Name`
  - `X-Findr-Roles`
  - `X-Findr-Shared-Secret`

Example nginx-style sketch:

```nginx
location /o/findr-api/ {
    proxy_pass http://findr-api:8000/o/findr-api/;
    proxy_set_header X-Findr-User-Id $upstream_http_x_liferay_user_id;
    proxy_set_header X-Findr-User-Name $upstream_http_x_liferay_user_name;
    proxy_set_header X-Findr-Roles $upstream_http_x_liferay_roles;
    proxy_set_header X-Findr-Shared-Secret ${FINDR_TRUSTED_SHARED_SECRET};
}
```

The exact Liferay identity extraction varies by your environment. The important part is that the proxy injects trusted Finder headers server-side.

## API Settings

Set these in production:

```dotenv
AUTH_REQUIRED=true
TRUSTED_SHARED_SECRET=replace-with-real-secret
```

## Local Testing Mode

If you need the browser to send headers directly during local testing, use:

```dotenv
VITE_FINDR_AUTH_MODE=browserHeaders
VITE_FINDR_SHARED_SECRET=local-test-secret
```

That mode is for development or controlled integration tests only.
