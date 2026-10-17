# Validation and installation tests

## What is checked

`python scripts/validate.py` checks the skill name/frontmatter, internal reference links, the 159 unique checklist IDs, source attribution and instruction length.

`python scripts/smoke_install.py` runs the actual pinned `skills@1.7.2` CLI in a new temporary project for each target:

1. Install only `ai-project-navigator` with `--copy` for `codex`, `gemini-cli` or `claude-code`.
2. Compare the SHA-256 of every installed file with the source checkout. Normalize CRLF to LF for text files so the test is portable across Git checkouts; compare other files byte for byte.
3. Verify that the CLI lists the skill for the selected target.
4. Reinstall and check the manifest again.
5. Remove this skill from the isolated project and verify removal.
6. Keep a different sentinel skill unchanged through install, reinstall and removal.

The test does not use global scope or change the tester's home directory. To repeat using the published repository rather than local files:

```sh
python scripts/smoke_install.py --source https://github.com/MrAshki/agentic-botcamp-checklist-skill.git
```

The source checkout must match the published revision, since file hashes are compared. Network access to npm and GitHub is required. The third-party installer's optional telemetry is disabled for these tests.

## Previous observed result on 2026-10-16

The isolated Linux installation, full-file comparison, list, reinstall and removal checks passed for all three targets. See [machine-readable result](install-local-linux.json). That saved result predates the unrelated-skill preservation check added later, so it does not prove that new check passed.

## Current local result on 2026-10-17

The isolated Windows test passed for Codex, Gemini CLI and Claude Code with the local repository as source. It verified all 22 installed skill files, listing, reinstall, removal and preservation of a different sentinel skill. See [machine-readable result](install-local-windows.json).

The same test then passed with the published GitHub repository as source. See [remote machine-readable result](install-github-windows.json).

GitHub-hosted workflow results were not checked in this local run. No authenticated live model session in Gemini CLI or Claude Code was tested.

After the GitHub installation, an ephemeral fresh Codex session loaded the installed `SKILL.md` from the user skills directory and answered the Persian news-classification test prompt. It returned a four-stage CPU-oriented path, eight completion-marked start items, and explicitly deferred RAG, agents, large-model fine-tuning and production infrastructure. This is one live Codex behavior check, not a test of the other three release scenarios or the other provider CLIs.

## Limits

Filesystem installation and CLI discovery are tested. A live model session in the destination Codex, Gemini CLI or Claude Code application is a separate check, requiring that tool to be installed and authenticated. These tests do not make paid model calls or claim that every version of those tools behaves identically.

Local development validation is on Linux. The GitHub Actions workflow runs the same installation tests on Linux, Windows and macOS; its live status is the authority for those environments, not the presence of the workflow file.

The documented global paths are based on the official provider documentation and installer behavior; the smoke tests use isolated project scope to avoid modifying a user's installed skills. In the pinned CLI, universal agents can share `.agents/skills`, including Gemini installations. Don't create duplicate copies manually in both the shared and provider-specific paths.

## Installer issue found

The pinned installer's `remove ... --agent gemini-cli` reported success but left the shared project copy behind in one isolated test. The smoke test and README therefore use removal of the named skill without an agent filter. This removes it across targets in the selected scope, so the README states that behavior explicitly.

## Skill behavior scenarios

Three prompts were independently exercised before the first publication:

- Tabular customer-churn prediction, 2,000 labeled rows, no GPU or budget, ten days to a class demo: short CPU path and a tailored checklist; no code generated.
- Vague request for AI in a shop: three focused questions and a provisional path; no premature fixed architecture.
- Comparison of four pretrained Persian speech models on 20 files from two speakers: evaluation and privacy checklist without requiring training.

A constraint interpretation issue in the third response was corrected in the instructions: keeping audio private must not silently turn into an offline-only dashboard requirement. Deadline feasibility must not be guaranteed. These instruction fixes passed structural validation; no new behavioral run of those two specific sentences is claimed.

The four release scenarios are also reviewed textually against `SKILL.md`, `selection-rules.md`, `interpretation.md` and the output contract:

- Labeled tabular ML, no GPU and low budget routes to a simple CPU baseline, not deep learning or an agent.
- A vague idea permits at most ten route-changing questions in one turn, while requiring the smallest useful set before a final checklist.
- Pretrained speech-model comparison routes to a fixed evaluation set and does not require training.
- RAG with private source data and a public demo separates private source handling from publishable outputs; privacy alone does not force an offline demo.

Textual review is not an independent live-model run. Record a new live run separately, with its raw prompt and output, before claiming behavioral execution for these four scenarios.

These scenario checks demonstrate limited observed behavior, not measured effectiveness across a classroom. For future evaluations, preserve the raw input and output, record unnecessary questions and irrelevant checklist items, and revise routing rules from observed failures.
