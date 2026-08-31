# Journal App

A habit-focused daily journal covering four areas: relationships, learning, money, and health.

## Setup

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

## Dependencies

- **Python 3.6+** (tested with Python 3.9.6)
- **Click 8.1+** - A Python library for creating beautiful command-line interfaces (CLI)

All dependencies are listed in `requirements.txt` and will be installed automatically with `pip install -r requirements.txt`.

## Usage

Add today's entry:
```bash
python -m journal.cli add
```

List recent entries:
```bash
python -m journal.cli list
python -m journal.cli list --limit 14
```

Your data is stored locally in `~/.journal/journal.db` (SQLite), separate from
the code repo, so it's never accidentally committed to git.

## Status

- [x] Phase 1: Data model
- [x] Phase 2: CLI v1 (add, list)
- [ ] Phase 3: Habit/streak tracking
- [ ] Phase 4: Tests + GitHub Actions CI
- [ ] Phase 5: Web view
- [ ] Phase 6: AI-powered weekly reflection
- [ ] Phase 7: Export + polish
