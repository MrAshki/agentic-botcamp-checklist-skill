#!/usr/bin/env python3
"""Exercise the real skills CLI in isolated project directories (never user scope)."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
NAME = 'ai-project-navigator'
VERSION = '1.7.2'


def run(args, cwd):
    env = dict(os.environ, DO_NOT_TRACK='1', DISABLE_TELEMETRY='1')
    result = subprocess.run(args, cwd=cwd, env=env, capture_output=True, text=True,
                            encoding='utf-8', errors='replace', timeout=180)
    if result.returncode:
        raise RuntimeError(result.stdout + result.stderr)
    return result.stdout


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', default=str(ROOT), help='Local checkout or remote repository URL')
    args = parser.parse_args()
    npx = shutil.which('npx.cmd' if os.name == 'nt' else 'npx')
    if not npx:
        raise SystemExit('Install Node.js LTS (with npm/npx) and Git first.')
    source = ROOT / 'skills' / NAME
    expected = {p.relative_to(source): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in source.rglob('*') if p.is_file()}
    base = [npx, '--yes', f'skills@{VERSION}']
    results = []
    for agent, folder in [('codex', '.agents'), ('gemini-cli', '.agents'), ('claude-code', '.claude')]:
        with tempfile.TemporaryDirectory(prefix=f'navigator-{agent}-') as tmp:
            cmd = base + ['add', args.source, '--skill', NAME, '--agent', agent, '--copy', '--yes']
            run(cmd, tmp)
            target = Path(tmp) / folder / 'skills' / NAME
            actual = {p.relative_to(target): hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in target.rglob('*') if p.is_file()}
            if actual != expected:
                raise RuntimeError(f'{agent}: installed files differ from source')
            listed = json.loads(run(base + ['ls', '--agent', agent, '--json'], tmp))
            if NAME not in json.dumps(listed):
                raise RuntimeError(f'{agent}: skill missing from list')
            # Reinstall verifies the documented update path without touching user files.
            run(cmd, tmp)
            if (target / 'SKILL.md').read_bytes() != (source / 'SKILL.md').read_bytes():
                raise RuntimeError(f'{agent}: reinstall mismatch')
            run(base + ['remove', NAME, '--yes'], tmp)
            if (target / 'SKILL.md').exists():
                raise RuntimeError(f'{agent}: uninstall did not remove skill')
            results.append({'agent': agent, 'install': 'pass', 'files': len(actual),
                            'list': 'pass', 'reinstall': 'pass', 'remove': 'pass'})
    print(json.dumps({'installer': f'skills@{VERSION}', 'scope': 'isolated project',
                      'source': 'remote' if args.source.startswith('https://') else 'local',
                      'results': results}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
