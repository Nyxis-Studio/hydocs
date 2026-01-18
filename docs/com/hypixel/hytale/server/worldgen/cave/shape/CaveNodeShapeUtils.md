# CaveNodeShapeUtils

## Overview
- Documentation for `CaveNodeShapeUtils`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.cave.shape`.

## Constructors
- None.

## Methods
- `getBoxAnchor(@Nonnull Vector3d vector, @Nonnull IWorldBounds bounds, double tx, double ty, double tz)`
  - Executes `getBoxAnchor` behavior.
- `getLineAnchor(@Nonnull Vector3d vector, @Nonnull Vector3d o, @Nonnull Vector3d v, double t)`
  - Executes `getLineAnchor` behavior.
- `getSphereAnchor(@Nonnull Vector3d vector, @Nonnull Vector3d origin, double rx, double ry, double rz, double tx, double ty, double tz)`
  - Executes `getSphereAnchor` behavior.
- `getPipeAnchor(@Nonnull Vector3d vector, @Nonnull Vector3d o, @Nonnull Vector3d v, double rx, double ry, double rz, double t, double tv, double th)`
  - Executes `getPipeAnchor` behavior.
- `getOffset(@Nullable CaveNode parent, @Nonnull CaveNodeType.CaveNodeChildEntry childEntry)`
  - Executes `getOffset` behavior.
- `getEndRadius(@Nullable CaveNode node, @Nonnull IDoubleRange range, Random random)`
  - Executes `getEndRadius` behavior.
- `getEndWidth(@Nullable CaveNode node, @Nonnull IDoubleRange range, Random random)`
  - Executes `getEndWidth` behavior.
- `getEndHeight(@Nullable CaveNode node, @Nonnull IDoubleRange range, Random random)`
  - Executes `getEndHeight` behavior.
- `getEndRadius(@Nonnull CaveNodeShape shape, @Nonnull BiDoubleToDoubleFunction widthHeightSelector)`
  - Executes `getEndRadius` behavior.
- `getFillingBlock(@Nonnull CaveType cave, @Nonnull CaveNodeType node, int y, @Nonnull Random random)`
  - Executes `getFillingBlock` behavior.
- `getCoverHeight(int lowest, int lowestPossible, int highest, int highestPossible, boolean heightLimited, @Nonnull CaveNodeType.CaveNodeCoverEntry cover, @Nonnull CaveNodeType.CaveNodeCoverEntry.Entry entry)`
  - Executes `getCoverHeight` behavior.
- `isCoverMatchingParent(int cx, int cz, int y, @Nonnull ChunkGeneratorExecution execution, @Nonnull CaveNodeType.CaveNodeCoverEntry cover)`
  - Executes `isCoverMatchingParent` behavior.
- `invalidateCover(int x, int y, int z, CaveNodeType.CaveNodeCoverType type, @Nonnull ChunkGeneratorExecution execution, @Nonnull BlockTypeAssetMap<String, BlockType> blockTypeMap)`
  - Executes `invalidateCover` behavior.
- `getRadialProjection(@Nonnull Vector3d vector, double x, double y, double z, double rx, double ry, double rz, double tx, double ty, double tz)`
  - Executes `getRadialProjection` behavior.

## Notes
- No additional notes.
