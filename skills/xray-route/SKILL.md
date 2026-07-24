---
name: xray-route
description: Manage local Xray DIRECT and PROXY domain rules through preinstalled, audited commands. Use only after confirming the target machine has a safe local Xray setup.
---

# Xray Route

Use the target machine's installed routing commands instead of editing Xray JSON directly.

## Map the request

- Add or remove a domain from DIRECT with `xray-direct`.
- Add or remove a domain from forced PROXY with `xray-proxy`.
- The unified command is `xray-route direct|proxy add|remove|list`.
- If the intended route is ambiguous, ask before changing anything.

## Execute safely

1. Accept only hostnames and the wildcard form explicitly supported by the local CLI.
2. Run the audited local CLI; it must validate its configuration before applying a change.
3. Treat idempotent results as success.
4. Verify changed membership with the matching `list` command.
5. Never print, commit, or request the Xray configuration, credentials, subscription links, or private endpoints.

## Routing semantics

- Forced PROXY takes precedence over DIRECT.
- Wildcard behavior and automatic maintenance are target-machine policy; inspect them before relying on them.
- Report only the outcome, effective route and validation failure, without leaking sensitive configuration.

