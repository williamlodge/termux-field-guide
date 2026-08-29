# Termux Field Guide

**Android Power User Manual — 2026 Edition**

A practical, single-file, offline-first field manual for turning an Android phone into a capable Linux workstation with Termux.

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
- Modern Android rooting
- Bootloaders, AVB, partitions, Magisk, KernelSU, and APatch
- Networking, automation, security, backup, and troubleshooting
- Command cheat sheets and primary-source references

## Read the guide

**Live site:** https://williamlodge.github.io/termux-field-guide/

Or open `index.html` directly in any modern browser — it is designed to work offline.

You can also serve it locally:

```bash
python -m http.server 8080
```

Then open `http://127.0.0.1:8080`.

## Version

**v1.0 — August 29, 2026**

The guide identifies sections verified against current upstream documentation and includes its source list in the document.

## Independent project notice

Termux Field Guide is an independent educational project. It is not an official Termux publication and is not affiliated with or endorsed by the Termux project. Product and project names belong to their respective owners.

## Safety

Some sections cover ADB, bootloader unlocking, flashing, root, and other privileged operations. Read commands before running them, confirm exact device and firmware compatibility, and maintain a recovery path.

## Author

Created and maintained by **William Lodge**.

## License

The written guide and original presentation are licensed under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**. See `LICENSE`.

Third-party project names, trademarks, code, documentation references, and linked material remain the property of their respective owners.
