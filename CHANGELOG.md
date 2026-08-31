# Changelog

All notable public changes to the Termux Field Guide are documented here.

This project follows semantic versioning: PATCH for corrections, MINOR for new features/sections, and MAJOR for structural or compatibility-breaking changes.

## [1.1.0] — 2026-08-30

### Added

- Installable Progressive Web App (PWA) support.
- Web app manifest and 192px/512px application icons.
- Service-worker caching for core offline use after the first successful load.
- Online/offline status indicator.
- Install-prompt support on compatible browsers.
- Visible version and last-updated information in the hosted guide.
- Community update/submission workflow.
- Structured correction, compatibility, security-warning, and new-section submissions.
- Direct prefilled GitHub Issue handoff for community submissions.
- Local draft persistence for submission forms.
- Canonical `VERSION` file.

### Changed

- Improved mobile header behavior and prevented page-level horizontal overflow on narrow screens.
- GitHub Pages deployment now builds the enhanced PWA site into `_site` before deployment.
- Guide source navigation now includes Community Updates and renumbers Sources & Verification accordingly in the deployed PWA.
- README now documents PWA installation, contribution workflow, and semantic versioning.

### Fixed

- Header/search controls causing horizontal scrolling on narrow Android screens.
- Project documentation showing the old v1.0 release after the PWA update.

## [1.0.0] — 2026-08-29

### Added

- Initial public release.
- 32-section Android/Termux field manual.
- Environment map covering Termux, PRoot, ADB, Shizuku, remote Linux, and real Android root.
- Termux installation and package-management guidance.
- Git, GitHub, SSH, development, web-server, database, and automation workflows.
- Termux:API and official add-on guidance.
- Third-party companion app section.
- ADB and Wireless Debugging guidance.
- Shizuku setup and limitations.
- PRoot-Distro and Termux:X11 coverage.
- Phone workstation guidance.
- Modern rooting overview covering Magisk, KernelSU, and APatch.
- Bootloader, Verified Boot, partition, recovery, security, networking, backup, and troubleshooting sections.
- Searchable, print-friendly, single-file offline interface.
- Primary-source references and verification date.
