# Contributing Guide

Welcome!  
This document explains how to work inside the project, coding style expectations, branching, and how to submit changes.

---

# 🧱 Architecture Overview

## Modules
**bus.py**  
Handles creation of CAN interfaces (virtual CAN, ValueCAN4).  
All interfaces must implement a common `send_message()` method.

**engine.py**  
Schedules and repeats CAN messages using QTimer.  
Also responsible for converting GUI inputs into CAN frames.

**profiles.py**  
Contains message profile builders.  
Each profile returns a structured set of message templates the GUI can load.

**gui.py**  
Main PyQt6 interface.  
Handles:
- selecting interfaces  
- loading profiles  
- starting/stopping message scheduling  
- live updating the UI  
- displaying logs  

**cli.py**  
Future CLI entrypoint for automated bench tests.

**version.py**  
Auto-updated during CI pipeline.

---

# 🛠 Development Setup

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the GUI:
```bash
python -m win_can_tool.gui
```

Run tests (future):
```bash
pytest
```

---

# 🌿 Branching Model

We use a simple Git flow:

- **main** → stable, tagged releases only  
- **feature/*** → new work  
- **fix/*** → bug fixes  
- **docs/*** → documentation updates  

Example:
```
git checkout -b feature/add-new-profile
```

When finished:

```
git push -u origin feature/add-new-profile
```

Submit a pull request.

---

# 🧪 Testing Profiles

Profiles live in `profiles.py` as Python functions that return:

```python
List[CanMessageTemplate]
```

Each `CanMessageTemplate` contains:
- `pgn`
- `priority`
- `source`
- data bytes  
- default frequency

Ensure:
- frequencies make sense for real equipment
- PGN/SPN definitions match J1939 or OEM docs
- DLC matches message size

---

# 🔧 Windows Packaging (PyInstaller)

Local build:
```powershell
py -3.12 -m PyInstaller --onefile --windowed `
  --name win_can_tool `
  --icon win_can_tool.ico `
  can_gui_launcher.py
```

Artifacts appear in:
```
dist/win_can_tool.exe
```

---

# 🚀 Release Pipeline

GitHub Actions performs:

1. Version injection
2. PyPI build + upload
3. Windows EXE build
4. CHANGELOG generation via git-cliff
5. GitHub release with artifacts

Tag a new version:
```bash
git tag v1.2.8
git push --tags
```

---

Happy hacking!
