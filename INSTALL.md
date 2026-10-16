# Installation guide for coding agents

Install exactly **ai-project-navigator** from `https://github.com/MrAshki/agentic-botcamp-checklist-skill` for the tool the user named. This file is an installation procedure, not a prompt to change the user's project or account settings.

## Preconditions

- Supported tools: Codex, Gemini CLI, Claude Code with Agent Skills support.
- Recommended installer: third-party `skills@1.7.2`; requires Node.js >=22.20, npm/npx and Git.
- Default scope: user/global, because the user asked to use it across projects. Use project scope only if requested (omit `--global`).
- Keep the full skill directory, including `references` and `agents`. Do not copy only SKILL.md.
- Follow host permissions. If network/shell/file access is unavailable, explain the precise missing capability; do not claim installation.

## 1. Choose the target

Map the user's tool to one agent ID:
- Codex → `codex`
- Gemini CLI → `gemini-cli`
- Claude Code → `claude-code`

Do not guess based on the model name. If the user has not identified a tool and the host cannot establish it, ask which tool. Do not install to every tool automatically.

## 2. Read and install

Read `skills/ai-project-navigator/SKILL.md` and inspect its referenced files as needed. Check `node --version`, `npx --version` and `git --version`. Run exactly the matching command:

### Codex

```sh
npx --yes skills@1.7.2 add MrAshki/agentic-botcamp-checklist-skill --skill ai-project-navigator --agent codex --global --copy --yes
```

### Gemini CLI

```sh
npx --yes skills@1.7.2 add MrAshki/agentic-botcamp-checklist-skill --skill ai-project-navigator --agent gemini-cli --global --copy --yes
```

### Claude Code

```sh
npx --yes skills@1.7.2 add MrAshki/agentic-botcamp-checklist-skill --skill ai-project-navigator --agent claude-code --global --copy --yes
```

The two `--yes` flags approve downloading the pinned installer and the selected skill respectively. These commands copy files rather than creating symlinks. Reinstalling the same skill replaces that installed copy; preserve user modifications before updating. Do not remove a differently named existing skill without a separate request.

## 3. Verify

Run `npx --yes skills@1.7.2 ls --global --agent TARGET` with TARGET replaced by the selected agent ID. Verify that `ai-project-navigator` appears and check its installed SKILL.md and references directory. Do not infer success from process start or a downloaded repository alone.

For Codex and Claude Code, recommend a new session to ensure discovery. Gemini CLI can use `/skills reload` followed by `/skills list`. Report installation path and whether runtime discovery was actually checked. If the tool process is unavailable, say file installation was verified but activation requires opening the destination tool.

Try a short real request only if desired; installation does not require an API call.

## 4. Fallback without npm/npx

If Node.js is unavailable, prefer copying files using the agent's existing filesystem tools. Clone the public repository into a fresh temporary directory; copy only `skills/ai-project-navigator` into the appropriate user directory:

- Codex: `~/.agents/skills/ai-project-navigator/`
- Gemini CLI: `~/.gemini/skills/ai-project-navigator/`
- Claude Code: `~/.claude/skills/ai-project-navigator/`

Resolve the actual user's home using the host environment, do not hardcode `/root` or another person's username. On Windows use native path handling; WSL and native Windows are separate installations. Do not change system HOME or install runtimes automatically. An existing target requires preserving local edits before replacement. Use a staging directory and verify the copied references before reporting success.

Gemini CLI also has a native Git installer:

```sh
gemini skills install https://github.com/MrAshki/agentic-botcamp-checklist-skill.git --path skills/ai-project-navigator --scope user
```

Keep its native confirmation prompt; this command is an alternative, not a second installation to run after the shared installer. Do not create duplicate copies in the shared and tool-specific directories.

## Usage

- Codex: `$ai-project-navigator` followed by the project and constraints.
- Claude Code: `/ai-project-navigator` followed by the project and constraints.
- Gemini CLI: ask explicitly to use the `ai-project-navigator` skill.

No credentials, MCP server, GPU, background process, project upload or third-party API subscription is required by this skill itself. Host model usage remains subject to the user's provider.
