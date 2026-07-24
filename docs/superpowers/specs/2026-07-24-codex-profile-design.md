# Portable Codex Profile Design

## Goal

Create a Git repository that lets a clean Codex environment recover Terry's work principles, verified workflows, reusable Skill inventory and safe configuration structure without copying credentials or machine state.

## Architecture

The repository separates human policy (`profile/`), capability inventories (`manifests/`), non-secret configuration templates (`config/`), portable self-authored Skills (`skills/`), and validation (`scripts/`). A bootstrap document tells a new Codex what to read and what it must configure locally.

## Security constraints

- No secrets, sessions, logs, caches, private endpoints or machine paths.
- Templates use placeholders only for values that must be supplied locally.
- The custom Xray Skill is reference-only until the new environment independently installs and verifies its local commands.

## Acceptance criteria

- A new user can identify what to read, what to install, and what must never be copied.
- The repository contains the current non-sensitive model and sandbox preferences.
- The repository contains the validated `xray-route` Skill in sanitized portable form.
- The audit script fails when common secret formats appear.

