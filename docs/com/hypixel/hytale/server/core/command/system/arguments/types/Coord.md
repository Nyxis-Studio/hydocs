# Coord

## Overview
- Documentation for `Coord`.
- Declared as a class in `com.hypixel.hytale.server.core.command.system.arguments.types`.

## Constructors
- `Coord(double value, boolean height, boolean relative, boolean chunk)`
  - Creates a `Coord` instance.
- `Coord(0.0, true, relative, chunk)`
  - Creates a `Coord` instance.
- `Coord(0.0, height, true, chunk)`
  - Creates a `Coord` instance.
- `Coord(0.0, height, relative, true)`
  - Creates a `Coord` instance.
- `Coord(Double.parseDouble(rest)`
  - Creates a `Coord` instance.

## Methods
- `getValue()`
  - Executes `getValue` behavior.
- `isNotBase()`
  - Executes `isNotBase` behavior.
- `isHeight()`
  - Executes `isHeight` behavior.
- `isRelative()`
  - Executes `isRelative` behavior.
- `isChunk()`
  - Executes `isChunk` behavior.
- `resolveXZ(double base)`
  - Executes `resolveXZ` behavior.
- `resolveYAtWorldCoords(double base, @Nonnull World world, double x, double z)`
  - Executes `resolveYAtWorldCoords` behavior.
- `resolve(double base)`
  - Executes `resolve` behavior.
- `parse(@Nonnull String str)`
  - Executes `parse` behavior.

## Notes
- No additional notes.
