# CHANGELOG

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `constants.py` to hold constants regarding import/export into quickbooks
- Added CLI command `qb_import` which runs `qb_import.cli:main`

### Fixed

- Fixed #1 inside the invoice_app.py due to wrong module name

### Changed

- Moved functions from root directory and into source folder
- Removed `gr_import.py` and moved into cli.py

### Removed

[Unreleased]: https://github.com/metrized-inc/project/compare/v0.1.0...HEAD
