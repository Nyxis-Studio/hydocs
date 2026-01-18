**Source Hash:** `b3afd0672ff06548a877e396759a8ded3af464d7e89fcfe3b150499250f0c0a0`

# Semver

## Overview

## Constructor Descriptions
- `Semver(long major, long minor, long patch)`
  - Creates a `Semver` instance.
- `Semver(long major, long minor, long patch, String[] preRelease, String build)`
  - Creates a `Semver` instance.
- `Semver(major, 0L, 0L, preRelease, build)`
  - Creates a `Semver` instance.
- `Semver(major, minor, 0L, preRelease, build)`
  - Creates a `Semver` instance.
- `Semver(major, minor, patch, preRelease, build)`
  - Creates a `Semver` instance.

## Method Descriptions
- `getMajor()`: Add description.
  - Executes `getMajor` behavior.
- `getMinor()`: Add description.
  - Executes `getMinor` behavior.
- `getPatch()`: Add description.
  - Executes `getPatch` behavior.
- `getPreRelease()`: Add description.
  - Executes `getPreRelease` behavior.
- `getBuild()`: Add description.
  - Executes `getBuild` behavior.
- `satisfies(@Nonnull SemverRange range)`: Add description.
  - Executes `satisfies` behavior.
- `compareTo(@Nonnull Semver other)`: Add description.
  - Executes `compareTo` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.
- `fromString(String str)`: Add description.
  - Executes `fromString` behavior.
- `fromString(String str, boolean strict)`: Add description.
  - Executes `fromString` behavior.
- `validateBuild(@Nullable String build)`: Add description.
  - Executes `validateBuild` behavior.
- `validatePreRelease(@Nullable String[] preRelease)`: Add description.
  - Executes `validatePreRelease` behavior.

## Notes
- No additional notes.
