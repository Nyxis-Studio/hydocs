**Source Hash:** `6b25280ffcaae62eeb25593b25989b6e24237c3d5b256644a0716e13ff096c6c`

# DistortedCaveNodeShape

## Overview

## Constructor Descriptions
- `DistortedCaveNodeShape(CaveType caveType, DistortedShape shape, ShapeDistortion distortion)`
  - Creates a `DistortedCaveNodeShape` instance.
- `DistortedCaveNodeShape(caveType, shape, this.distortion)`
  - Creates a `DistortedCaveNodeShape` instance.

## Method Descriptions
- `getShape()`: Add description.
  - Executes `getShape` behavior.
- `getStart()`: Add description.
  - Executes `getStart` behavior.
- `getEnd()`: Add description.
  - Executes `getEnd` behavior.
- `getAnchor(Vector3d vector, double tx, double ty, double tz)`: Add description.
  - Executes `getAnchor` behavior.
- `getBounds()`: Add description.
  - Executes `getBounds` behavior.
- `hasGeometry()`: Add description.
  - Executes `hasGeometry` behavior.
- `shouldReplace(int seed, double x, double z, int y)`: Add description.
  - Executes `shouldReplace` behavior.
- `getFloorPosition(int seed, double x, double z)`: Add description.
  - Executes `getFloorPosition` behavior.
- `getCeilingPosition(int seed, double x, double z)`: Add description.
  - Executes `getCeilingPosition` behavior.
- `populateChunk(int seed, @Nonnull ChunkGeneratorExecution execution, @Nonnull Cave cave, @Nonnull CaveNode node, @Nonnull Random random)`: Add description.
  - Executes `populateChunk` behavior.
- `getFloor(int seed, double x, double z, double centerY, double height, int minY)`: Add description.
  - Executes `getFloor` behavior.
- `getCeiling(int seed, double x, double z, double centerY, double height, int maxY)`: Add description.
  - Executes `getCeiling` behavior.
- `generateCaveNodeShape(Random random, CaveType caveType, @Nullable CaveNode parentNode, @Nonnull CaveNodeType.CaveNodeChildEntry childEntry, @Nonnull Vector3d position, float yaw, float pitch)`: Add description.
  - Executes `generateCaveNodeShape` behavior.
- `getOrigin(@Nonnull Vector3d origin, @Nullable CaveNode parentNode, @Nonnull CaveNodeType.CaveNodeChildEntry childEntry)`: Add description.
  - Executes `getOrigin` behavior.
- `getLength(@Nullable IDoubleRange lengthRange, Random random)`: Add description.
  - Executes `getLength` behavior.
- `getDirection(double yaw, double pitch, double length)`: Add description.
  - Executes `getDirection` behavior.
- `getStartWidth(boolean inheritParentRadius, @Nullable CaveNode parentNode, @Nonnull IDoubleRange fallback, Random random)`: Add description.
  - Executes `getStartWidth` behavior.
- `getStartHeight(boolean inheritParentRadius, @Nullable CaveNode parentNode, @Nonnull IDoubleRange fallback, Random random)`: Add description.
  - Executes `getStartHeight` behavior.
- `getMiddleRadius(double start, double end, @Nullable IDoubleRange range, Random random)`: Add description.
  - Executes `getMiddleRadius` behavior.

## Notes
- No additional notes.
