# Termux Field Guide

**Android Power User Manual — 2026 Edition**  
**Current version: v1.1.0 — August 30, 2026**

A practical, mobile-first, offline-capable field manual for turning an Android phone into a capable Linux workstation with Termux, while clearly separating stock Android, ADB, Shizuku, PRoot, remote Linux, and real root workflows.

## Live guide

**https://williamlodge.github.io/termux-field-guide/**

The hosted guide is an installable PWA. After the first successful load, its core files are cached for offline use.

## What it covers

- Installing Termux correctly
- Storage, packages, shells, keyboard workflow, and tmux
- Git and GitHub
- SSH and remote server administration
- Python, Node.js, PHP, compilers, and local web development
- SQLite and production-database guidance
- Termux:API and official add-ons
- Third-party companion apps
- ADB and Wireless Debugging
- Shizuku
- PRoot-Distro
- Termux:X11 and GUI Linux
- Phone-as-workstation setups
- Modern Android rooting and why root became less necessary
- Bootloaders, AVB, partitions, Magisk, KernelSU, and APatch
- Networking, automation, security, backup, and troubleshooting
- Command cheat sheets and primary-source references
- Community corrections and user submissions through GitHub Issues

## PWA features

- Installable on supported Android browsers
- Offline service-worker cache
- Mobile-safe header and responsive layout
- Searchable guide sections
- Copy buttons for command blocks
- Online/offline status
- Version and last-updated metadata
- Community submission builder with direct GitHub Issue handoff

## Versioning

This project uses semantic versioning:

- **PATCH** (`1.1.1`) — corrections, broken links, small compatibility fixes
- **MINOR** (`1.2.0`) — new sections, tools, PWA features, meaningful workflow additions
- **MAJOR** (`2.0.0`) — structural rewrites or major compatibility/safety changes

The canonical current version is also stored in the `VERSION` file and documented in `CHANGELOG.md`.

### Current release

**v1.1.0 — August 30, 2026**

Added the installable PWA layer, offline cache, app icons, mobile-header overflow fix, visible version/last-updated metadata, and a community submission workflow that can prepare and open GitHub Issues.

### Previous release

**v1.0.0 — August 29, 2026** — initial public release.

## Run locally

You can open `index.html` directly for the core guide, or serve the repository locally:

```bash
python -m http.server 8080
```

Then open `http://127.0.0.1:8080`.

For full PWA/service-worker behavior, use HTTPS or localhost.

## Contributing

Corrections, compatibility reports, new tools, command updates, security warnings, and new-section ideas are welcome. Use the guide's **Community Updates** form or open a GitHub Issue. Prefer primary sources and include exact device/build details when a workflow is hardware- or firmware-specific.

See `CONTRIBUTING.md` for contribution guidance.

## Independent project notice

Termux Field Guide is an independent educational project. It is not an official Termux publication and is not affiliated with or endorsed by the Termux project. Product and project names belong to their respective owners.

## Safety

Some sections cover ADB, bootloader unlocking, flashing, root, and other privileged operations. Read commands before running them, confirm exact device and firmware compatibility, preserve matching stock firmware, and maintain a recovery path.

## Author

Created and maintained by **William Lodge**.

If this guide saved you time, consider [buying me a coffee](https://buymeacoffee.com/williamlodge).

## License

The written guide and original presentation are licensed under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**. See `LICENSE`.

Third-party project names, trademarks, code, documentation references, and linked material remain the property of their respective owners.
