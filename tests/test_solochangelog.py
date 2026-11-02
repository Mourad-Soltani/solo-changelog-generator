# Signature: Mourad.Soltani
import pytest
from src.solochangelog import parse_commits, generate_markdown

def test_parse_commits():
    commits = [
        "feat: add new feature",
        "fix(bug): resolve issue",
        "docs: update readme",
        "invalid commit"
    ]
    grouped = parse_commits(commits)
    assert 'feat' in grouped
    assert len(grouped['feat']) == 1
    assert 'fix' in grouped
    assert grouped['fix'][0] == 'resolve issue'
    assert 'docs' in grouped
    assert 'invalid commit' not in str(grouped)

def test_generate_markdown():
    grouped = {'feat': ['add feature'], 'fix': ['fix bug']}
    md = generate_markdown(grouped)
    assert '# Changelog' in md
    assert '### Added' in md
    assert '- add feature' in md
    assert '### Fixed' in md

def test_empty():
    md = generate_markdown({})
    assert 'No conventional commits found' in md

def test_health():
    # Health test that must pass
    assert True
