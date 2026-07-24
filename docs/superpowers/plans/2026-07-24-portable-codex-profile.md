# Portable Codex Profile Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a safe Git repository that transfers Terry's Codex work style and reusable capabilities to a clean environment.

**Architecture:** Separate operating principles, workflows, inventories, configuration templates and self-authored Skills. Keep secrets and machine state out of version control, and enforce an initial scan through a small audit script.

**Tech Stack:** Markdown, TOML template, YAML metadata, Bash, Git.

## Global Constraints

- Never include credentials, sessions, private endpoints, logs, caches or machine-specific state.
- New environments install Skills only after reviewing their dependencies and permissions.
- The `xray-route` Skill remains reference-only until its target machine has independently verified local Xray commands.

---

### Task 1: Establish the repository policy and initialization path

**Files:**
- Create: `README.md`
- Create: `docs/initialization.md`
- Create: `profile/working-principles.md`
- Create: `manifests/exclusions.md`

- [ ] Write the safe migration boundary and quick-start sequence.
- [ ] State the evidence-first, small-step, verifiable work style.
- [ ] List secrets and machine state that must never be migrated.
- [ ] Check that a clean reader can determine what to read before modifying a target environment.

### Task 2: Capture reusable operating knowledge

**Files:**
- Create: `profile/task-playbooks.md`
- Create: `profile/capability-map.md`
- Create: `manifests/skills.md`

- [ ] Document separate workflows for robotics, research, production release and remote maintenance.
- [ ] Map current capabilities to their validation style.
- [ ] Record Skills as optional, task-driven dependencies rather than blanket global installation.

### Task 3: Add portable configuration and custom Skill source

**Files:**
- Create: `config/codex-config.template.toml`
- Create: `skills/xray-route/README.md`
- Create: `skills/xray-route/SKILL.md`
- Create: `skills/xray-route/agents/openai.yaml`

- [ ] Preserve only non-sensitive model and sandbox preferences.
- [ ] Add a sanitized, target-machine-neutral `xray-route` Skill.
- [ ] Document its dependency on separately installed local commands.

### Task 4: Add and run repository safety checks

**Files:**
- Create: `scripts/audit.sh`
- Create: `.gitignore`

- [ ] Check required files.
- [ ] Scan tracked content for common token and private-key patterns.
- [ ] Run the audit and inspect Git status before the initial commit.

