# SemverRange

## Overview
- Documentation for `SemverRange`.
- Declared as a class in `com.hypixel.hytale.common.semver`.

## Constructors
- `SemverRange(new SemverSatisfies[0], true)`
  - Creates a `SemverRange` instance.
- `SemverRange(SemverSatisfies[] comparators, boolean and)`
  - Creates a `SemverRange` instance.
- `SemverRange(new SemverSatisfies[]{new SemverComparator(SemverComparator.ComparisonType.GTE, Semver.fromString(range[0], strict)`
  - Creates a `SemverRange` instance.
- `SemverRange(new SemverSatisfies[]{new SemverComparator(SemverComparator.ComparisonType.GTE, semver)`
  - Creates a `SemverRange` instance.
- `SemverRange(comparatorsAnd, true)`
  - Creates a `SemverRange` instance.
- `SemverRange(comparators, false)`
  - Creates a `SemverRange` instance.

## Methods
- `satisfies(Semver semver)`
  - Executes `satisfies` behavior.
- `toString()`
  - Executes `toString` behavior.
- `fromString(String str)`
  - Executes `fromString` behavior.
- `fromString(String str, boolean strict)`
  - Executes `fromString` behavior.

## Notes
- No additional notes.
