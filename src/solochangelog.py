# Signature: Mourad.Soltani
"""
Solo Changelog Generator - minimal CLI for conventional commits to Keep a Changelog.
"""
import argparse
import subprocess
import re
from collections import defaultdict
from typing import Dict, List

CONVENTIONAL_RE = re.compile(r'^(feat|fix|docs|style|refactor|perf|test|chore|build|ci)(\(.+\))?: (.+)$')

def get_git_log(since: str = None) -> List[str]:
    cmd = ['git', 'log', '--pretty=format:%s']
    if since:
        cmd.append(f'{since}..HEAD')
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return [line.strip() for line in result.stdout.splitlines() if line.strip()]
    except subprocess.CalledProcessError:
        return []

def parse_commits(commits: List[str]) -> Dict[str, List[str]]:
    grouped = defaultdict(list)
    for commit in commits:
        match = CONVENTIONAL_RE.match(commit)
        if match:
            ctype = match.group(1)
            desc = match.group(3)
            grouped[ctype].append(desc)
    return dict(grouped)

def generate_markdown(grouped: Dict[str, List[str]]) -> str:
    md = "# Changelog\n\n## [Unreleased]\n\n"
    type_map = {
        'feat': 'Added',
        'fix': 'Fixed',
        'docs': 'Documentation',
        'style': 'Style',
        'refactor': 'Refactored',
        'perf': 'Performance',
        'test': 'Tests',
        'chore': 'Chore',
        'build': 'Build',
        'ci': 'CI'
    }
    for ctype, descs in grouped.items():
        section = type_map.get(ctype, ctype.capitalize())
        md += f"### {section}\n\n"
        for desc in descs:
            md += f"- {desc}\n"
        md += "\n"
    if not grouped:
        md += "No conventional commits found.\n"
    return md

def main():
    parser = argparse.ArgumentParser(description="Solo Changelog Generator by Mourad.Soltani")
    parser.add_argument('generate', nargs='?', help='Generate changelog')
    parser.add_argument('--since', type=str, default=None, help='Since tag or commit')
    args = parser.parse_args()
    commits = get_git_log(args.since)
    grouped = parse_commits(commits)
    print(generate_markdown(grouped))

if __name__ == '__main__':
    main()
