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

## GitHub Actions Workflow

A single workflow file (`.github/workflows/build.yml`) handles all build scenarios:

- **Default Build** (Push/PR to `main`): Builds only Flavor A
- **Release Build** (Release published or tag `v*`): Builds all flavors (A, B, C)
- **Manual Build** (Workflow dispatch): Builds all flavors (A, B, C)

The workflow dynamically adjusts the build matrix based on the trigger event.

## Artifacts

Each workflow run produces artifacts containing:
- The `build.py` script
- A `flavor.txt` file indicating which flavor was built