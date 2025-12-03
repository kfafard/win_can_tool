# Development Deep Dive

This document goes deeper into internal architecture, design patterns, data flows, and extension points.

---

# 🧩 Core Components

## bus.py — CAN Interface Abstraction

Implements:
- Virtual CAN (`python-can` internal loopback)
- ValueCAN4 (via Python CAN + ICS driver)

All bus implementations must expose:

```python
send_message(msg)
open()
close()
```

A CAN frame is always structured using:

```python
engine.build_can_frame(template, override_bytes)
```

---

# engine.py — Message Engine

The engine handles the core logic:

### 1. **Message Template Expansion**
A template contains:
- CAN ID
- DLC
- byte pattern (hex list)
- frequency in Hz

### 2. **Timers**
Each message gets a `QTimer`:
```python
timer.setInterval(int(1000 / frequency))
timer.timeout.connect(lambda: self._send(template))
```

### 3. **Overriding Byte Updates**
GUI modifications propagate immediately:
```python
template.bytes = gui_bytes
```

### 4. **Bus Independence**
Engine never cares what interface is used — only calls `.send_message()`.

---

# gui.py — Application UI

Built using PyQt6.

### Responsibilities:
- Load profiles (`QComboBox`)
- Create/edit message entries (`QTableWidget`)
- Handle interface selection
- Start/stop engine timers
- Real-time log updates
- Icons + assets

### Asset Paths
Handles PyInstaller using:

```python
if hasattr(sys, "_MEIPASS"):
    asset_path = Path(sys._MEIPASS) / "assets"
else:
    asset_path = Path(__file__).parent.parent / "assets"
```

---

# profiles.py — Profile Definitions

Profile builders are simple Python functions:

```python
def PROFILE_BUILDERS():
    return {
        "Example": build_example_profile
    }
```

A profile returns:
```python
[
    CanMessageTemplate(
        pgn=65262,
        priority=3,
        source=0x23,
        data=[0x00, 0xFF, 0x00, 0x10, 0xAA, 0xBB, 0xCC, 0xDD],
        freq=10
    ),
    ...
]
```

You can add:
- GNSS messages
- Engine data
- Hydraulics data
- Transmission data
- Misc OEM packets

---

# 🔌 CAN Bus Flow

```
GUI → Engine → Bus → CAN Device → External Listener
```

---

# 🧱 Future Expansion Points

## Planned:
- CLI standalone tool
- Replay logs
- Parameterized message generators
- Scripting API
- Add more CAN hardware interfaces
- Save/load user message sets

---

# 🤖 CI/CD Breakdown

## Build steps:
### PyPI:
- Replace version
- Build wheel + sdist
- Upload securely

### EXE:
- Install pyinstaller
- Build using launcher script
- Upload artifact

### Changelog:
- git-cliff Docker container ensures deterministic output

### GitHub Release:
- Attach EXE, wheel, sdist, CHANGELOG

---

# 🗂 File Layout

```
win_can_tool/
  bus.py
  engine.py
  profiles.py
  gui.py
  cli.py
  version.py
assets/
  gui_dark.png
  gui_light.png
win_can_tool.ico
```

---

# 🧵 Threading Model

The GUI runs in the Qt main thread.  
Message sending runs through QTimers — *not* threads.

This ensures:
- stable operation
- no race conditions
- flexible scaling

---

# 🏁 End

This doc covers the full internals of the project.  
Use it when extending core code, adding profiles, or modifying architecture.
