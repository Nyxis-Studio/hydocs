# HexMeshNoise

## Overview
- Documentation for `HexMeshNoise`.
- Declared as a class in `com.hypixel.hytale.procedurallib.logic`.

## Constructors
- `HexMeshNoise(IIntCondition density, double thickness, CellJitter jitter, boolean linesX, boolean linesY, boolean linesZ)`
  - Creates a `HexMeshNoise` instance.

## Methods
- `get(int seed, int offsetSeed, double x, double y)`
  - Executes `get` behavior.
- `get(int seed, int offsetSeed, double x, double y, double z)`
  - Executes `get` behavior.
- `checkConnections(int offsetSeed, double x, double y, int cx, int cy, double nearest)`
  - Executes `checkConnections` behavior.
- `checkDiagonalConnections(int offsetSeed, double x, double y, int cx, int cy, double nearest)`
  - Executes `checkDiagonalConnections` behavior.
- `dist2Cell(int offsetSeed, double x, double y, double adx, double ady, double ax, double ay, int cx, int cy)`
  - Executes `dist2Cell` behavior.

## Notes
- No additional notes.
