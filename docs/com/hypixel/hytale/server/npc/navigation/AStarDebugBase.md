# AStarDebugBase

## Overview
- Documentation for `AStarDebugBase`.
- Declared as a class in `com.hypixel.hytale.server.npc.navigation`.

## Constructors
- `AStarDebugBase(AStarBase base, @Nonnull HytaleLogger logger)`
  - Creates a `AStarDebugBase` instance.

## Methods
- `dumpOpens(MotionController controller)`
  - Executes `dumpOpens` behavior.
- `dumpPath()`
  - Executes `dumpPath` behavior.
- `dumpMap(boolean drawPath, MotionController controller)`
  - Executes `dumpMap` behavior.
- `dumpMap(@Nullable AStarNode pathNode, boolean isFinalPath, MotionController controller)`
  - Executes `dumpMap` behavior.
- `plot(long positionIndex, char character, @Nonnull StringBuilder[] map, int minX, int minZ)`
  - Executes `plot` behavior.
- `drawMapFinish(StringBuilder[] map, int minX, int minZ)`
  - Executes `drawMapFinish` behavior.
- `getDumpMapRegionZ(int def)`
  - Executes `getDumpMapRegionZ` behavior.
- `getDumpMapRegionX(int def)`
  - Executes `getDumpMapRegionX` behavior.
- `getExtraLogString(MotionController controller)`
  - Executes `getExtraLogString` behavior.

## Notes
- No additional notes.
