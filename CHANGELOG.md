# Changelog

All notable changes to this project will be documented in this file.

This project follows:
- [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
- [Semantic Versioning](https://semver.org/)

Changelog entries are automatically generated from commit history using **git-cliff** based on enforced commit conventions.

---

## [Unreleased]

### Added
- *(Planned features for v1.2.28 go here)*

### Changed
- *(Planned behavior changes for v1.2.28 go here)*

### Fixed
- *(Planned bug fixes for v1.2.28 go here)*

---

## [v1.2.27] - 2025-12-08

### Added
- Raw CAN message editor dialog (add, edit, delete).
- JSON-based profile save and load support.
- Live GNSS position simulation with motion-based updates.
- Engine, fuel, and coolant live simulation controls.
- Windows EXE build via GitHub Actions CI pipeline.
- Automatic version injection into builds from Git tags.
- Event Log panel to track runtime simulator activity.
- Dark/light GUI assets bundled into Windows EXE.
- Commit message template and enforced formatting (`.gitmessage`).

### Changed
- Refactored CAN simulation engine structure.
- Standardized CAN message period handling.
- Improved profile switching safety during active simulation.
- Improved message table layout and column resizing behavior.
- Improved Windows EXE build reliability and reproducibility.
- GitHub Actions workflow split into:
  - PyPI build & publish
  - Windows EXE build
  - Changelog generation
  - GitHub Release automation

### Fixed
- Incorrect GNSS live value refresh while simulator was running.
- Raw message persistence bugs in JSON profile files.
- Simulator failing to shutdown CAN bus cleanly after Stop.
- Profile reload not updating live value controls correctly.
- Period spinboxes not syncing properly with message model.
- Multiple PyInstaller backend import failures for CAN adapters.

---

## [v1.2.26] - 2025-12-02

### Added
- Initial PYPI packaging pipeline.
- Initial Windows EXE generation via PyInstaller.
- GNSS PGN stubs for GPS-based simulation.
- Tractor base simulation profile.

### Fixed
- Multiple startup crashes from missing CAN imports.
- Incorrect PGN payload formatting.
- Broken message enable/disable behavior.

---

## [v1.2.25] - 2025-11-23

### Added
- Initial GUI-based CAN Simulator interface.
- Base CAN transmit engine.
- Profile-based message builder system.

---

## [v1.2.0] - 2025-10-01

### Added
- Initial public release of `win_can_tool`.
