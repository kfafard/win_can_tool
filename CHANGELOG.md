# Changelog

All notable changes to this project will be documented in this file.

The format is based on **Keep a Changelog**, and this project follows **Semantic Versioning (SemVer)**.

---

## [Unreleased]

### Added
- (Automatically generated during the next release)

### Changed
- (Automatically generated during the next release)

### Fixed
- (Automatically generated during the next release)

---

## [v1.2.27] - 2025-12-08

### Added
- Full hardware support for **ValueCAN4** and **Kvaser Leaf** CAN interfaces.
- GUI-based **raw CAN message editor** with:
  - Add / edit / delete support
  - Extended and standard ID handling
  - Editable periods and payloads
- **Moving GNSS position simulation** with live UI updates.
- **Profile save/load system** using JSON, including:
  - Live GNSS values
  - Message enable states
  - Raw message persistence
- **Automated GitHub Actions Release Pipeline**:
  - Tag-based releases (`v*.*.*`)
  - PyPI publishing
  - Windows EXE build via PyInstaller
  - GitHub Release creation with attached artifacts
- Automatic version injection into:
  - `pyproject.toml`
  - `win_can_tool/version.py`
- Auto-generated GitHub release artifacts.
- CAN backend auto-detection via `python-can`.
- About dialog showing **version and author** from package metadata.

### Changed
- Windows EXE output naming now follows tag version:
  - Example: `win_can_tool-v1.2.27.exe`
- CI release logic now fully centralized in GitHub Actions.
- Changelog generation now handled by **git-cliff** during releases.
- Internal CAN interface handling generalized for multiple backends.
- GNSS motion origin reset on each simulator start.

### Fixed
- PyInstaller crashes caused by missing ICS modules.
- Hidden-import issues for multiple CAN backends.
- EXE artifact mismatches in CI.
- CI failures caused by stale `.spec` files.
- Live GNSS values not updating when motion was enabled.
- CAN engine start/stop state cleanup issues.

### Known Issues
- Windows EXE icon does not embed consistently in CI builds.
- Windows SmartScreen warning appears due to unsigned binaries.
- EXE icon embedding varies by Windows cache behavior.

---

## [v1.2.26] - 2025-12-05

### Added
- Initial GitHub Actions release workflow.
- Basic PyInstaller Windows EXE generation.
- Early ValueCAN4 support.
- Initial raw message simulation support.

### Changed
- Internal simulator engine refactoring.
- Profile system groundwork.

### Fixed
- CAN send timing inaccuracies.
- Early python-can backend detection bugs.

---

## [v1.2.25] - 2025-11-30

### Added
- Initial public simulator GUI.
- GNSS, speed, engine load, and fuel simulation.
- CAN message table with enable/disable controls.

### Fixed
- UI crashes related to missing profile defaults.

---

## [v1.2.0] - 2025-11-10

### Added
- First structured release of **win_can_tool**.
- Multi-message CAN simulation engine.
- Qt-based GUI frontend.
- Profile-based message presets.

---
