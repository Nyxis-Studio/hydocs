# PipeCaveNodeShape

## Overview
- Documentation for `PipeCaveNodeShape`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.cave.shape`.

## Constructors
- `PipeCaveNodeShape(CaveType caveType, @Nonnull Vector3d o, @Nonnull Vector3d v, double radius1, double radius2, double middleRadius)`
  - Creates a `PipeCaveNodeShape` instance.
- `PipeCaveNodeShape(caveType, origin, direction, radius1, radius2, radius3)`
  - Creates a `PipeCaveNodeShape` instance.

## Methods
- `getStart()`
  - Executes `getStart` behavior.
- `getEnd()`
  - Executes `getEnd` behavior.
- `getAnchor(@Nonnull Vector3d vector, double t, double tv, double th)`
  - Executes `getAnchor` behavior.
- `getBounds()`
  - Executes `getBounds` behavior.
- `getLowBoundX()`
  - Executes `getLowBoundX` behavior.
- `getLowBoundZ()`
  - Executes `getLowBoundZ` behavior.
- `getHighBoundX()`
  - Executes `getHighBoundX` behavior.
- `getHighBoundZ()`
  - Executes `getHighBoundZ` behavior.
- `getLowBoundY()`
  - Executes `getLowBoundY` behavior.
- `getHighBoundY()`
  - Executes `getHighBoundY` behavior.
- `getRadius1()`
  - Executes `getRadius1` behavior.
- `getRadius2()`
  - Executes `getRadius2` behavior.
- `shouldReplace(int seed, double x, double z, int y)`
  - Executes `shouldReplace` behavior.
- `projectPointOnNode(double px, double py, double pz)`
  - Executes `projectPointOnNode` behavior.
- `getRadiusAt(double t)`
  - Executes `getRadiusAt` behavior.
- `getFloorPosition(int seed, double x, double z)`
  - Executes `getFloorPosition` behavior.
- `getCeilingPosition(int seed, double x, double z)`
  - Executes `getCeilingPosition` behavior.
- `toString()`
  - Executes `toString` behavior.
- `generateCaveNodeShape(@Nonnull Random random, CaveType caveType, CaveNode parentNode, @Nonnull CaveNodeType.CaveNodeChildEntry childEntry, @Nonnull Vector3d origin, float yaw, float pitch)`
  - Executes `generateCaveNodeShape` behavior.

## Notes
- No additional notes.
