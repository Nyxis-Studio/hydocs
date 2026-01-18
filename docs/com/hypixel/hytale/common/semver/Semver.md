# Semver

## Overview
- Documentation for `Semver`.
- Declared as a class in `com.hypixel.hytale.common.semver`.

## Constructors
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

## Methods
- `getMajor()`
  - Executes `getMajor` behavior.
- `getMinor()`
  - Executes `getMinor` behavior.
- `getPatch()`
  - Executes `getPatch` behavior.
- `getPreRelease()`
  - Executes `getPreRelease` behavior.
- `getBuild()`
  - Executes `getBuild` behavior.
- `satisfies(@Nonnull SemverRange range)`
  - Executes `satisfies` behavior.
- `compareTo(@Nonnull Semver other)`
  - Executes `compareTo` behavior.
- `toString()`
  - Executes `toString` behavior.
- `fromString(String str)`
  - Executes `fromString` behavior.
- `fromString(String str, boolean strict)`
  - Executes `fromString` behavior.
- `validateBuild(@Nullable String build)`
  - Executes `validateBuild` behavior.
- `validatePreRelease(@Nullable String[] preRelease)`
  - Executes `validatePreRelease` behavior.

## Notes
- No additional notes.
