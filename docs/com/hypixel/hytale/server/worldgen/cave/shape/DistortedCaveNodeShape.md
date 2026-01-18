# DistortedCaveNodeShape

## Overview
- Documentation for `DistortedCaveNodeShape`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.cave.shape`.

## Constructors
- `DistortedCaveNodeShape(CaveType caveType, DistortedShape shape, ShapeDistortion distortion)`
  - Creates a `DistortedCaveNodeShape` instance.
- `DistortedCaveNodeShape(caveType, shape, this.distortion)`
  - Creates a `DistortedCaveNodeShape` instance.

## Methods
- `getShape()`
  - Executes `getShape` behavior.
- `getStart()`
  - Executes `getStart` behavior.
- `getEnd()`
  - Executes `getEnd` behavior.
- `getAnchor(Vector3d vector, double tx, double ty, double tz)`
  - Executes `getAnchor` behavior.
- `getBounds()`
  - Executes `getBounds` behavior.
- `hasGeometry()`
  - Executes `hasGeometry` behavior.
- `shouldReplace(int seed, double x, double z, int y)`
  - Executes `shouldReplace` behavior.
- `getFloorPosition(int seed, double x, double z)`
  - Executes `getFloorPosition` behavior.
- `getCeilingPosition(int seed, double x, double z)`
  - Executes `getCeilingPosition` behavior.
- `populateChunk(int seed, @Nonnull ChunkGeneratorExecution execution, @Nonnull Cave cave, @Nonnull CaveNode node, @Nonnull Random random)`
  - Executes `populateChunk` behavior.
- `getFloor(int seed, double x, double z, double centerY, double height, int minY)`
  - Executes `getFloor` behavior.
- `getCeiling(int seed, double x, double z, double centerY, double height, int maxY)`
  - Executes `getCeiling` behavior.
- `generateCaveNodeShape(Random random, CaveType caveType, @Nullable CaveNode parentNode, @Nonnull CaveNodeType.CaveNodeChildEntry childEntry, @Nonnull Vector3d position, float yaw, float pitch)`
  - Executes `generateCaveNodeShape` behavior.
- `getOrigin(@Nonnull Vector3d origin, @Nullable CaveNode parentNode, @Nonnull CaveNodeType.CaveNodeChildEntry childEntry)`
  - Executes `getOrigin` behavior.
- `getLength(@Nullable IDoubleRange lengthRange, Random random)`
  - Executes `getLength` behavior.
- `getDirection(double yaw, double pitch, double length)`
  - Executes `getDirection` behavior.
- `getStartWidth(boolean inheritParentRadius, @Nullable CaveNode parentNode, @Nonnull IDoubleRange fallback, Random random)`
  - Executes `getStartWidth` behavior.
- `getStartHeight(boolean inheritParentRadius, @Nullable CaveNode parentNode, @Nonnull IDoubleRange fallback, Random random)`
  - Executes `getStartHeight` behavior.
- `getMiddleRadius(double start, double end, @Nullable IDoubleRange range, Random random)`
  - Executes `getMiddleRadius` behavior.

## Notes
- No additional notes.
