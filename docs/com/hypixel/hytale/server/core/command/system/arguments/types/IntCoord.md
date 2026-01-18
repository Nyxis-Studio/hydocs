# IntCoord

## Overview
- Documentation for `IntCoord`.
- Declared as a class in `com.hypixel.hytale.server.core.command.system.arguments.types`.

## Constructors
- `IntCoord(int value, boolean height, boolean relative, boolean chunk)`
  - Creates a `IntCoord` instance.
- `IntCoord(0, true, relative, chunk)`
  - Creates a `IntCoord` instance.
- `IntCoord(0, height, true, chunk)`
  - Creates a `IntCoord` instance.
- `IntCoord(0, height, relative, true)`
  - Creates a `IntCoord` instance.
- `IntCoord(Integer.parseInt(rest)`
  - Creates a `IntCoord` instance.

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
- `resolveXZ(int base)`
  - Executes `resolveXZ` behavior.
- `resolveYAtWorldCoords(int base, @Nonnull ChunkStore chunkStore, int x, int z)`
  - Executes `resolveYAtWorldCoords` behavior.
- `resolve(int base)`
  - Executes `resolve` behavior.
- `parse(@Nonnull String str)`
  - Executes `parse` behavior.

## Notes
- No additional notes.
