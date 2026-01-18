**Source Hash:** `11848789b70dd7b623199d5664cd7ab0b4106eba59ec6441dc8d787d90647cc1`

# ClimateType

## Overview

## Constructor Descriptions
- `ClimateType(@Nonnull String name, @Nonnull ClimateColor color, @Nonnull ClimateColor island, @Nonnull ClimatePoint[] points, @Nonnull ClimateType[] children)`
  - Creates a `ClimateType` instance.

## Method Descriptions
- `toString()`: Add description.
  - Executes `toString` behavior.
- `name(@Nullable ClimateType parent, @Nonnull ClimateType type)`: Add description.
  - Executes `name` behavior.
- `walk(ClimateType type, Consumer<ClimateType> visitor)`: Add description.
  - Executes `walk` behavior.
- `walk(ClimateType[] types, Consumer<ClimateType> visitor)`: Add description.
  - Executes `walk` behavior.
- `color(int id, @Nonnull ClimateGraph climate)`: Add description.
  - Executes `color` behavior.
- `walkRecursive(ClimateType type, Consumer<ClimateType> visitor, int depth)`: Add description.
  - Executes `walkRecursive` behavior.

## Notes
- No additional notes.
