# uv — Python Package Manager

`uv` is a fast, modern replacement for `pip` + `venv`. It handles virtual environments automatically.

## Install

```bash
brew install uv
```

## Starting a new project

```bash
uv init my-project
cd my-project
```

This creates:
```
my-project/
├── .venv/          # virtual environment (auto-created)
├── pyproject.toml  # project metadata + dependencies
└── main.py
```

## Adding dependencies

```bash
uv add pygame        # installs and adds to pyproject.toml
uv add pygame==2.5   # pin a specific version
uv remove pygame     # remove a package
```

## Running code

```bash
uv run main.py       # runs inside the venv automatically, no activate needed
```

## Syncing dependencies (when returning to a project)

```bash
uv sync              # installs everything in pyproject.toml
```

## Key difference from pip + venv

With `pip` you had to:
1. Create venv manually
2. Activate it
3. Then pip install

With `uv` you just `uv add` and `uv run` — it manages the venv for you in the background.

## Equivalent commands

| Old way | uv |
|---------|----|
| `python3 -m venv .venv` | automatic |
| `source .venv/bin/activate` | not needed |
| `pip install pygame` | `uv add pygame` |
| `pip install -r requirements.txt` | `uv sync` |
| `python main.py` | `uv run main.py` |
