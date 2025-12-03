# 🛠 **DEVELOPMENT.md**

### *Internal Architecture & Development Guide for win_can_tool*

This document provides deeper technical details for contributors who want to understand, maintain, or extend the internal architecture of **win_can_tool**.

If you're only looking to publish releases or install the project, check `README.md` or `CONTRIBUTING.md`.

---

# 📦 Project Structure

```
win_can_tool/
│
├── bus.py              # CAN interface abstraction
├── cli.py              # Command-line launcher
├── engine.py           # Message generator / engine thread
├── gui.py              # PyQt6 GUI
├── profiles.py         # Built-in message profiles & simulation data
├── version.py          # Auto-injected version file
│
├── __init__.py
└── __pycache__/
```

---

# ⚙ Core Architecture

The application is built around **four primary components**:

---

## 1️⃣ `bus.py` — CAN Bus Abstraction Layer

This module wraps multiple CAN device backends using `python-can`, providing a consistent interface for:

* **NeoVI / ValueCAN (neovi)**
* **Kvaser**
* **PEAK PCAN**
* **SocketCAN (Linux virtual can0/vcan0)**
* **python-can virtual interface**

### Key functions:

#### `open_bus(interface, channel, bitrate)`

Returns a fully configured python-can `Bus` object.

This allows the GUI and CLI to remain backend-agnostic.

#### `bus.shutdown()`

Gracefully closes the CAN device.

---

## 2️⃣ `engine.py` — Message Generation Engine

The engine is a **threaded CAN frame scheduler**.

### Responsibilities:

* timing each message
* periodic sending
* respecting delays
* marking raw vs profile messages
* dynamic payload generation

### Core object:

#### `CanMessageTemplate`

Contains:

* arbitration ID
* extended/standard flag
* period (ms)
* DLC
* a `payload_func(now)` callback
* enabled flag
* optional raw_data

### Example dynamic payload function:

```python
def payload_func(now):
    return bytes([int(now) % 255] * 8)
```

The engine evaluates this function every time the message is due.

---

## 3️⃣ `profiles.py` — Built-In Simulation Profiles

Profiles define reusable collections of message templates.

Each profile is a function:

```python
def build_default_profile() -> list[CanMessageTemplate]
```

All available profiles are stored in:

```python
PROFILE_BUILDERS = {
    "Default": build_default_profile,
    "GNSS Motion": build_gnss_profile,
}
```

Profiles can contain:

* Engine data
* Fuel data
* GNSS + movement simulation
* Generic J1939 messages
* Custom raw messages

### Live simulation values:

```
LAT_DEG
LON_DEG
COG_DEG
SOG_MS
ENGINE_LOAD_PCT
...
```

The GUI modifies these via spinboxes.

---

## 4️⃣ `gui.py` — PyQt GUI Application

Contains:

### Key UI modules:

* **Profile selector**
* **Live editing panel (GNSS, engine values, etc.)**
* **Message table** (shows name, ID, period, enabled)
* **Raw message add/edit/delete**
* **Event log**
* **Start/stop controls**
* **Help → About dialog**

### Runtime behavior:

* On Start:

  * opens CAN bus
  * resets GNSS motion origin
  * starts engine thread
  * disables editing controls

* While running:

  * GNSS position updates live via QTimer at 5 Hz
  * GUI reflects new lat/lon without triggering callbacks

* On Stop:

  * engine stops
  * bus shuts down
  * controls re-enable

---

# 🧬 Message Flow Overview

```
GUI/CLI
   │
   ├── loads a profile from profiles.py
   │
   ├── modifies messages (user edits, raw messages)
   │
   ▼
engine.set_messages(list[CanMessageTemplate])
   │
   ▼
Engine Thread:
   - Compute time until next message
   - Call payload_func(now)
   - Send frame via python-can Bus
```

Raw messages bypass dynamic logic and use static bytes.

---

# 🌍 GNSS Motion System

Profiles may use:

```
compute_moving_lat_lon(now: float) -> (lat, lon)
```

This simulates continuous movement based on:

* origin timestamp
* current heading (COG_DEG)
* speed over ground (SOG_MS)

The GUI syncs spinboxes to GNSS simulation but blocks signals to avoid feedback loops.

---

# 🔧 Extending the System

### Adding a new built-in profile:

1. Create a function in `profiles.py`
2. Add it to `PROFILE_BUILDERS`
3. It appears automatically in the GUI dropdown

---

### Adding a new live-editable parameter:

1. Add global variable in `profiles.py`
2. Add spinbox in `gui.py`
3. Add valueChanged callback
4. Add to JSON saver/loader mapping

---

### Adding a new CAN backend:

Modify:

```python
open_bus() in bus.py
```

---

# 🖨 How Version Injection Works

During CI, when a tag like `v1.2.3` is pushed:

```
win_can_tool/version.py
```

is rewritten automatically to:

```python
__version__ = "1.2.3"
```

This value is used by:

* GUI window title
* About dialog
* CLI `--version`
* PyPI metadata
* GitHub release notes
* EXE metadata (optional)

You **never** manually edit this file.

---

# 🐍 PyInstaller Build Notes

PyInstaller is run on Windows in GitHub Actions:

```
pyinstaller --onefile --windowed can_gui_launcher.py
```

Important considerations:

* always import modules normally
* avoid relative filesystem paths
* embed icons via `--icon win_can_tool.ico`
* `version.py` must exist before PyInstaller runs

---

# 📁 File Added by CI Workflows

### During release automation, the following files get rewritten:

| File                      | Purpose                  |
| ------------------------- | ------------------------ |
| `win_can_tool/version.py` | version injection        |
| `CHANGELOG.md`            | auto-generated changelog |
| GitHub Release notes      | automatically created    |
| `dist/win_can_tool.zip`   | EXE release bundle       |

---

# 🚀 Future Development Ideas

* Add multi-frame J1939 transport protocol simulation
* Add NMEA2000 PGN builder
* Add parameter groups editor (GUI)
* Add CSV → CAN replay
* Add CAN sniffing display panel (incoming frames)
* Add scripting support for custom payloads

---

# 🙋 Need Help?

Open an issue:

👉 [https://github.com/kfafard/win_can_tool/issues](https://github.com/kfafard/win_can_tool/issues)
