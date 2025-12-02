# CAN Simulator

A cross-platform CAN (Controller Area Network) message generator with both a GUI and CLI.

This tool is useful for:
- Testing CAN-based devices
- Developing CAN parsers
- Prototyping embedded systems
- Generating repeatable CAN traffic
- Teaching or debugging CAN messaging behavior

The simulator provides:
- Customizable CAN messages
- Support for extended (29-bit) and standard (11-bit) IDs
- J1939-style and NMEA-style demo messages
- Live-editable values (speed, heading, GNSS position, temperatures, etc.)
- User-defined raw CAN frames
- Start/Stop message scheduler
- JSON save/load support for profiles
- Multiple CAN backends (`virtual`, `socketcan`, Kvaser, PCAN, neoVI, etc.)

---

## Features

### ✔ GUI Mode
- Real-time editing of GNSS and engine-like values
- Add, edit, or delete raw CAN frames
- Enable/disable individual messages
- Switch between multiple predefined message profiles
- Save/load full simulator configurations
- Event log with timestamps

### ✔ CLI Mode

```bash
py -m can_sim.cli --interface virtual --channel vcan0 --profile "GNSS only"
````

Useful for:

* Automated testing
* Headless environments
* Generating consistent CAN traffic

---

## Installation

```bash
pip install PyQt6 python-can
```

Optional extras:

```bash
pip install filelock
```

---

## Running the GUI

```bash
py -m can_sim.gui
```

## Running the CLI

```bash
py -m can_sim.cli --interface virtual --channel vcan0
```

Common CAN backends:

```
--interface kvaser
--interface pcan
--interface socketcan
--interface virtual
--interface neovi
```

---

## Project Structure

```
can_sim/
    bus.py              # CAN bus interface wrapper
    cli.py              # Command-line entrypoint
    engine.py           # Background scheduler and message timing engine
    gui.py              # PyQt GUI interface
    profiles.py         # Demo message profiles and encoders
```

---

## Roadmap (future versions)

* Modular GUI (split into components)
* Multi-frame (fast-packet) NMEA messages
* J1939 transport protocol (TP.CM/TP.DT)
* Real-time charts/visualization widgets
* Multi-channel CAN output
* Profile editor UI
* Plugin system for custom message generators

---

## License

MIT
