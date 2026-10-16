#!/usr/bin/env python3
"""Validate the portable skill, attribution, reference links and checklist IDs."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
skill = root / 'skills' / 'ai-project-navigator'
manifest = (skill / 'SKILL.md').read_text(encoding='utf-8')
assert manifest.startswith('---\nname: ai-project-navigator\n'), 'Invalid skill name/frontmatter'
assert '\ndescription: ' in manifest.split('---', 2)[1], 'Missing description'
ids = []
for path in skill.rglob('*.md'):
    text = path.read_text(encoding='utf-8')
    for target in re.findall(r'\]\(([^)]+)\)', text):
        if not target.startswith(('https://', 'http://', '#')):
            assert (path.parent / target).is_file(), f'Broken link: {path.name}: {target}'
    if re.match(r'0[1-8]-', path.name):
        ids.extend(re.findall(r'^- \[ \] (C\d+-\d+) \|', text, re.M))
assert len(ids) == len(set(ids)) == 159, 'Checklist count or IDs changed'
assert 'رضا شکرزاد' in (skill / 'references/provenance.md').read_text(encoding='utf-8')
assert len(manifest.splitlines()) < 500, 'Skill too long'
assert 'در پاسخ عادی آن‌ها را چاپ نکن' in manifest, 'User-facing source rule is missing'
assert (skill / 'references/course-topic-map.md').is_file(), 'Course topic map is missing'
package_text = '\n'.join(
    path.read_text(encoding='utf-8', errors='replace')
    for path in root.rglob('*')
    if path.is_file() and '.git' not in path.parts
    and path.name != 'agentic-checklist-source.bundle'
)
for pattern in (r'AKIA[0-9A-Z]{16}', r'ghp_[A-Za-z0-9]{30,}',
                r'sk-[A-Za-z0-9_-]{20,}', r'C:\\Users\\[^\\\s]+'):
    assert not re.search(pattern, package_text), f'Possible secret or personal path: {pattern}'
print('PASS: portable manifest, internal references, 159 unique checklist items and attribution')
