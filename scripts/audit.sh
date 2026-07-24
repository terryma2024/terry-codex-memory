#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root_dir"

echo "Repository: $root_dir"
echo "Checking required documentation..."
for file in README.md profile/working-principles.md profile/task-playbooks.md manifests/skills.md manifests/exclusions.md docs/initialization.md; do
  test -f "$file" || { echo "Missing: $file" >&2; exit 1; }
done

echo "Checking for obvious secret material..."
if grep -RInE --exclude-dir=.git --exclude=audit.sh '(-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----|AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{30,}|xox[baprs]-[A-Za-z0-9-]{20,})' .; then
  echo "Potential secret detected. Remove it before commit." >&2
  exit 1
fi

echo "Checking local tooling..."
for command in git rg; do
  command -v "$command" >/dev/null && echo "Found: $command" || echo "Optional command missing: $command"
done

echo "Audit passed: repository structure is present and no obvious secret pattern was found."

