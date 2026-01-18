# ClimateType

## Overview
- Documentation for `ClimateType`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.climate`.

## Constructors
- `ClimateType(@Nonnull String name, @Nonnull ClimateColor color, @Nonnull ClimateColor island, @Nonnull ClimatePoint[] points, @Nonnull ClimateType[] children)`
  - Creates a `ClimateType` instance.

## Methods
- `toString()`
  - Executes `toString` behavior.
- `name(@Nullable ClimateType parent, @Nonnull ClimateType type)`
  - Executes `name` behavior.
- `walk(ClimateType type, Consumer<ClimateType> visitor)`
  - Executes `walk` behavior.
- `walk(ClimateType[] types, Consumer<ClimateType> visitor)`
  - Executes `walk` behavior.
- `color(int id, @Nonnull ClimateGraph climate)`
  - Executes `color` behavior.
- `walkRecursive(ClimateType type, Consumer<ClimateType> visitor, int depth)`
  - Executes `walkRecursive` behavior.

## Notes
- No additional notes.
