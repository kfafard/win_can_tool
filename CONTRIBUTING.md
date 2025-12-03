# 📘 **CONTRIBUTING.md**

# Contributing to **win_can_tool**

Thank you for your interest in contributing!
This project uses a fully automated release pipeline, so contributing is straightforward and low-maintenance — just follow the guidelines below.

---

# 🧱 Project Structure Basics

```
win_can_tool/
    gui.py
    cli.py
    bus.py
    engine.py
    profiles.py
    version.py   ← version auto-injected during release
```

* **Do NOT manually update version numbers.**
  These are generated automatically based on Git tags.

* All code must remain compatible with:

  * Python ≥ 3.10
  * PyInstaller
  * PyQt6
  * python-can

---

# 🧪 Development Setup

### 1. Clone the repository

```bash
git clone https://github.com/kfafard/win_can_tool.git
cd win_can_tool
```

### 2. Install in editable mode

This allows VSCode, PyInstaller, and Pylance to resolve imports correctly:

```bash
pip install -e .
```

### 3. Install development dependencies

```bash
pip install -r requirements.txt
```

Optional tools for contributors:

```bash
pip install black flake8 git-cliff
```

---

# 🧭 Code Style

This project uses **PEP8 + Black formatting**.
Please ensure your code is formatted before committing:

```bash
black .
```

---

# 🧪 Testing Changes Locally

Before committing, you can run:

### Run the GUI

```bash
python -m win_can_tool.gui
```

### Run the CLI

```bash
win-can-cli --help
```

### Build a local EXE (optional)

```bash
pyinstaller --onefile --windowed can_gui_launcher.py
```

---

# 📦 Dependency Policy

* Always prefer the **standard library** when possible.
* External dependencies must:

  * be cross-platform,
  * be PyInstaller-friendly,
  * have active maintenance.

---

# 🎉 **Release Process (Automated)**

Releases are **100% automated** using GitHub Actions.

## You do NOT manually:

❌ Edit version numbers
❌ Build PyPI packages
❌ Build Windows EXEs
❌ Write release notes
❌ Update CHANGELOG.md

All of these are automated.

---

# 🚀 How to Publish a New Release

### ✔ Step 1 — Commit your changes normally

```bash
git add .
git commit -m "feat: add new GNSS smoothing"
git push
```

### ✔ Step 2 — Create a semantic version tag

Example for version 1.4.0:

```bash
git tag v1.4.0
git push origin v1.4.0
```

### 🎯 This one command triggers everything:

## Automated Result:

| Task              | Automation                                |
| ----------------- | ----------------------------------------- |
| Version injected  | `pyproject.toml` + `version.py` updated   |
| Changelog updated | `CHANGELOG.md` rewritten via git-cliff    |
| PyPI publish      | Package built + uploaded                  |
| EXE build         | PyInstaller Windows EXE compiled          |
| GitHub Release    | Created with auto-generated notes         |
| Assets            | `win_can_tool.zip` uploaded automatically |

Everything is generated using your GitHub Actions workflows:

* `publish-pypi.yml`
* `release.yml`
* `changelog.yml`

---

# 📄 Commit Messages

This project supports **Conventional Commits** for clean changelogs.

Recommended prefixes:

| Type        | Meaning                         |
| ----------- | ------------------------------- |
| `feat:`     | New feature                     |
| `fix:`      | Bug fix                         |
| `docs:`     | Documentation                   |
| `refactor:` | Code restructuring              |
| `perf:`     | Performance improvement         |
| `style:`    | Formatting, missing commas, etc |
| `test:`     | Adding/repairing tests          |
| `ci:`       | GitHub Actions & pipelines      |
| `chore:`    | Misc cleanup                    |

Example:

```
feat: add configurable GNSS heading drift
fix: correct engine load calculation at 5 Hz
docs: update quick-start instructions
```

---

# 🛡 Pull Requests

Pull requests should:

* Keep scope focused
* Include a clear description
* Follow project code style
* Avoid adding non-portable or Windows-only behavior to core code

Maintainers will:

* Review PRs promptly
* Suggest improvements if needed
* Merge when ready

---

# 💬 Questions or Discussion?

Open an Issue at:

👉 [https://github.com/kfafard/win_can_tool/issues](https://github.com/kfafard/win_can_tool/issues)

Or reach out directly if something in the workflow is confusing.

---

# 🙏 Thank You

Your contributions help grow a high-quality, cross-platform CAN simulation and testing toolkit.
We appreciate your time, ideas, and improvements!
