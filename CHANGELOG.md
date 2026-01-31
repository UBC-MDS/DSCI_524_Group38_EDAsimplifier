# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- GitHub Actions workflow for documentation preview (#74)
- Codecov badge in README (#74)

### Changed
- Version scheme configuration in Hatch (#74)
- Renamed `build.yml` to `ci.yml` (#74)
- Renamed `deploy.yml` to `cd.yml` (#74)
- Renamed `quartodoc.yml` to `docs-publish.yml` (#74)
- Updated README for docs-publish workflow and CI/CD badges (#76)
- CI workflow now runs coverage test (#74)
- Documentation output directory changed from `docs` to `_site` (#74)
- Updated dependencies in `environment.yml` (#78)
- Added all authors and emails in `pyproject.toml` (#73)

## [1.0.1] - 2026-01-25

### Added
- Examples for the last two functions in `simplify.py`
- `environment.yml` with pinned dependencies
- Links to API reference and TestPyPI in README
- Build and deploy badges in README
- Extra index for dependencies when using pip to install
- GitHub Actions CI/CD workflow
- GitHub Actions quartodoc workflow
- Matrix to automated tests
- Four additional unit tests in `test_numeric`
- Ruff and Black to development dependencies

### Changed
- Dynamic versioning in pyproject.toml
- Updated CI/CD workflow and quartodoc configuration
- README: detailed instructions, URL, badge cleanup

### Fixed
- README instruction for installing

### Removed
- Templated `.github/workflows/test.yml`
- Unused dependencies

## [1.0.0] - 2026-01-17

### Added
- Implimentation for `dataset_overview`, `numeric`, `categorical_plot`, and `all_distributions`
- Unit test files and integration tests for the above functions
- Dependencies: Altair, pytest, numpy
- Pyproject and README updates for running tests
- Documentation and README updates

## [0.0.1] - 2026-01-10

### Added
- Initial project structure
- `simplify.py` with all function and module docstrings
- README with function details, contributors, and copyright
- CONTRIBUTING.md with contributing guidelines
- Code of Conduct
- Copyright and license information
