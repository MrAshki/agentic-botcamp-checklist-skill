# Validation and installation tests

## What is checked

`python scripts/validate.py` checks the skill name/frontmatter, internal reference links, the 159 unique checklist IDs, source attribution and instruction length.

`python scripts/smoke_install.py` runs the actual pinned `skills@1.7.2` CLI in a new temporary project for each target:

1. Install only `ai-project-navigator` with `--copy` for `codex`, `gemini-cli` or `claude-code`.
2. Compare the SHA-256 of every installed file with the source checkout.
3. Verify that the CLI lists the skill for the selected target.
4. Reinstall and check the manifest again.
5. Remove this skill from the isolated project and verify removal.

The test does not use global scope or change the tester's home directory. To repeat using the published repository rather than local files:

```sh
python scripts/smoke_install.py --source https://github.com/MrAshki/agentic-botcamp-checklist-skill.git
```

The source checkout must match the published revision, since file hashes are compared. Network access to npm and GitHub is required. The third-party installer's optional telemetry is disabled for these tests.

## Observed result on 2026-10-16

The isolated Linux installation, full-file comparison, list, reinstall and removal checks passed for all three targets. See [machine-readable result](install-local-linux.json).

Remote installation and GitHub-hosted workflow results have not been verified: publication was blocked by GitHub write access. Those checks should run after the repository is populated. No authenticated live model session in the three provider CLIs was tested.

## Limits

Filesystem installation and CLI discovery are tested. A live model session in the destination Codex, Gemini CLI or Claude Code application is a separate check, requiring that tool to be installed and authenticated. These tests do not make paid model calls or claim that every version of those tools behaves identically.

Local development validation is on Linux. The GitHub Actions workflow runs the same installation tests on Linux, Windows and macOS; its live status is the authority for those environments, not the presence of the workflow file.

The documented global paths are based on the official provider documentation and installer behavior; the smoke tests use isolated project scope to avoid modifying a user's installed skills. In the pinned CLI, universal agents can share `.agents/skills`, including Gemini installations. Don't create duplicate copies manually in both the shared and provider-specific paths.

## Installer issue found

The pinned installer's `remove ... --agent gemini-cli` reported success but left the shared project copy behind in one isolated test. The smoke test and README therefore use removal of the named skill without an agent filter. This removes it across targets in the selected scope, so the README states that behavior explicitly.

## Skill behavior scenarios

The navigator was independently exercised on three prompts before publishing:

- Tabular customer-churn prediction, 2,000 labeled rows, no GPU or budget, ten days to a class demo: short CPU path and a tailored checklist; no code generated.
- Vague request for AI in a shop: three focused questions and a provisional path; no premature fixed architecture.
- Comparison of four pretrained Persian speech models on 20 files from two speakers: evaluation and privacy checklist without requiring training.

A constraint interpretation issue in the third response was corrected in the instructions: keeping audio private must not silently turn into an offline-only dashboard requirement. Deadline feasibility must not be guaranteed. These instruction fixes passed structural validation; no new behavioral run of those two specific sentences is claimed.

These scenario checks demonstrate limited observed behavior, not measured effectiveness across a classroom. For future evaluations, preserve the raw input and output, record unnecessary questions and irrelevant checklist items, and revise routing rules from observed failures.
