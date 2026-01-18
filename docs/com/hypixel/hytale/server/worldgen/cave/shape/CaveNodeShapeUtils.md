**Source Hash:** `4fc5f315753f79c638152dba61f864a96c4b68d7021934be248524de76d3041b`

# CaveNodeShapeUtils

## Overview

## Constructor Descriptions
- `none()`: No documented methods.

## Method Descriptions
- `getBoxAnchor(@Nonnull Vector3d vector, @Nonnull IWorldBounds bounds, double tx, double ty, double tz)`: Add description.
  - Executes `getBoxAnchor` behavior.
- `getLineAnchor(@Nonnull Vector3d vector, @Nonnull Vector3d o, @Nonnull Vector3d v, double t)`: Add description.
  - Executes `getLineAnchor` behavior.
- `getSphereAnchor(@Nonnull Vector3d vector, @Nonnull Vector3d origin, double rx, double ry, double rz, double tx, double ty, double tz)`: Add description.
  - Executes `getSphereAnchor` behavior.
- `getPipeAnchor(@Nonnull Vector3d vector, @Nonnull Vector3d o, @Nonnull Vector3d v, double rx, double ry, double rz, double t, double tv, double th)`: Add description.
  - Executes `getPipeAnchor` behavior.
- `getOffset(@Nullable CaveNode parent, @Nonnull CaveNodeType.CaveNodeChildEntry childEntry)`: Add description.
  - Executes `getOffset` behavior.
- `getEndRadius(@Nullable CaveNode node, @Nonnull IDoubleRange range, Random random)`: Add description.
  - Executes `getEndRadius` behavior.
- `getEndWidth(@Nullable CaveNode node, @Nonnull IDoubleRange range, Random random)`: Add description.
  - Executes `getEndWidth` behavior.
- `getEndHeight(@Nullable CaveNode node, @Nonnull IDoubleRange range, Random random)`: Add description.
  - Executes `getEndHeight` behavior.
- `getEndRadius(@Nonnull CaveNodeShape shape, @Nonnull BiDoubleToDoubleFunction widthHeightSelector)`: Add description.
  - Executes `getEndRadius` behavior.
- `getFillingBlock(@Nonnull CaveType cave, @Nonnull CaveNodeType node, int y, @Nonnull Random random)`: Add description.
  - Executes `getFillingBlock` behavior.
- `getCoverHeight(int lowest, int lowestPossible, int highest, int highestPossible, boolean heightLimited, @Nonnull CaveNodeType.CaveNodeCoverEntry cover, @Nonnull CaveNodeType.CaveNodeCoverEntry.Entry entry)`: Add description.
  - Executes `getCoverHeight` behavior.
- `isCoverMatchingParent(int cx, int cz, int y, @Nonnull ChunkGeneratorExecution execution, @Nonnull CaveNodeType.CaveNodeCoverEntry cover)`: Add description.
  - Executes `isCoverMatchingParent` behavior.
- `invalidateCover(int x, int y, int z, CaveNodeType.CaveNodeCoverType type, @Nonnull ChunkGeneratorExecution execution, @Nonnull BlockTypeAssetMap<String, BlockType> blockTypeMap)`: Add description.
  - Executes `invalidateCover` behavior.
- `getRadialProjection(@Nonnull Vector3d vector, double x, double y, double z, double rx, double ry, double rz, double tx, double ty, double tz)`: Add description.
  - Executes `getRadialProjection` behavior.

## Notes
- No additional notes.
