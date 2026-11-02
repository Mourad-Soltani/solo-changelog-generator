# Solo Changelog Generator

A minimal, shippable micro-tool for solo developers to generate Keep a Changelog style markdown from conventional git commits.

**Signature: Mourad.Soltani**

## Features
- Parses git log for conventional commits (feat, fix, docs, etc.)
- Groups by type and outputs markdown
- Health checks via pytest
- Zero external dependencies beyond Python stdlib + git

## Installation
```bash
pip install -e .
```

## Usage
```bash
python -m solochangelog generate --since v1.0.0
```

## Tests
```bash
pytest tests/
```

Built for solo product engineers. Realistic micro-SaaS starter.

License: MIT
