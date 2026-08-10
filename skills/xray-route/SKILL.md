---
name: xray-route
description: Use when the user asks to add, remove, list, or inspect local Xray DIRECT or forced-PROXY domain routing and audited xray-direct, xray-proxy, or xray-route commands are available.
---

# Xray Route

## Overview

Use the target machine's installed routing commands instead of editing Xray JSON directly.

## Quick reference

| Request | Managed command shape | Coverage |
|---|---|---|
| Exact DIRECT hostname | `xray-direct add|remove host.example` | Exact hostname |
| Explicit DIRECT wildcard | `xray-direct add|remove '*.example.org'` | Target-machine policy; quote the wildcard |
| Forced-PROXY domain family | `xray-proxy add|remove example.org` | Base domain and every subdomain |

The unified command is `xray-route direct|proxy add|remove|list`.

## Map the request

- Add or remove an exact hostname from DIRECT with `xray-direct`.
- A DIRECT wildcard is target-machine policy; pass it only when the user explicitly requests that supported form, and quote it to prevent shell expansion.
- To force a base domain and all of its subdomains through PROXY, add the bare base domain with `xray-proxy`. Normalize a request such as `*.example.org` to `example.org`; do not pass the wildcard to the PROXY command.
- If the intended route is ambiguous, ask before changing anything.

## Execute safely

1. Accept only hostnames and the wildcard form explicitly supported for DIRECT by the local CLI; reject schemes, paths, ports, IP addresses and other wildcard forms.
2. Run the audited local CLI; it must validate its configuration before applying a change.
3. Treat idempotent results as success.
4. Verify changed membership with the matching `list` command. For a PROXY family rule, confirm the exact bare domain is present.
5. If the managed command needs higher privileges, request controlled elevation for that command; never bypass it by editing the live configuration.
6. Never print, commit, or request the Xray configuration, credentials, subscription links, private endpoints or full routing logs.

## Routing semantics

- In the audited command suite, a bare forced-PROXY domain covers the base domain and every subdomain, and takes precedence over DIRECT.
- DIRECT wildcard behavior and automatic maintenance remain target-machine policy; inspect them before relying on them.
- Rule membership proves configured intent. When actual routing is material, inspect only target-scoped runtime evidence through the machine's approved telemetry.
- Report only the outcome, effective route and validation failure, without leaking sensitive configuration.

## Common mistakes

- Passing `*.example.org` to PROXY: normalize it to the bare base domain.
- Treating list membership as proof of actual traffic: use target-scoped runtime evidence when routing outcome matters.
- Editing live configuration after a permission failure: elevate only the audited management command.
