# xtest

A simple Python project demonstrating GitHub Actions build matrices with multiple flavors.

## Flavors

This project supports three build flavors:
- **Flavor A**: Default build flavor
- **Flavor B**: Extended build flavor
- **Flavor C**: Extended build flavor

## Build Script

The `build.py` script is a simple Python script that prints the flavor being built:

```bash
python build.py <flavor>
```

## GitHub Actions Workflows

### Build Workflow (Default)
- **Trigger**: Push or Pull Request to `main` branch
- **Builds**: Only Flavor A
- **File**: `.github/workflows/build.yml`

### Release Workflow
- **Trigger**: Release published or tag pushed (v*)
- **Builds**: All flavors (A, B, C)
- **File**: `.github/workflows/release.yml`

### Manual Build Workflow
- **Trigger**: Manual workflow dispatch
- **Builds**: All flavors (A, B, C)
- **File**: `.github/workflows/manual.yml`

## Artifacts

Each workflow run produces artifacts containing:
- The `build.py` script
- A `flavor.txt` file indicating which flavor was built