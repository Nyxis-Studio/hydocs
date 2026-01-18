# CaveNodeType

## Overview
- Documentation for `CaveNodeType`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.cave`.

## Constructors
- `CaveNodeType(@Nonnull String name, @Nullable CavePrefabContainer prefabContainer, @Nonnull IWeightedMap<BlockFluidEntry> fillings, @Nonnull CaveNodeShapeEnum.CaveNodeShapeGenerator shapeGenerator, @Nonnull ICoordinateCondition heightCondition, @Nullable IDoubleRange childrenCountBounds, @Nonnull CaveNodeCoverEntry[] covers, int priority, int environment)`
  - Creates a `CaveNodeType` instance.

## Methods
- `getName()`
  - Executes `getName` behavior.
- `getPrefabContainer()`
  - Executes `getPrefabContainer` behavior.
- `setChildren(@Nonnull CaveNodeChildEntry[] children)`
  - Executes `setChildren` behavior.
- `getHeightCondition()`
  - Executes `getHeightCondition` behavior.
- `getChildrenCountBounds()`
  - Executes `getChildrenCountBounds` behavior.
- `getFilling(@Nonnull Random random)`
  - Executes `getFilling` behavior.
- `generateCaveNodeShape(Random random, CaveType caveType, CaveNode parentNode, CaveNodeChildEntry childEntry, Vector3d origin, float yaw, float pitch)`
  - Executes `generateCaveNodeShape` behavior.
- `getCovers()`
  - Executes `getCovers` behavior.
- `getChildren()`
  - Executes `getChildren` behavior.
- `getPriority()`
  - Executes `getPriority` behavior.
- `hasEnvironment()`
  - Executes `hasEnvironment` behavior.
- `getEnvironment()`
  - Executes `getEnvironment` behavior.
- `get(Random random)`
  - Executes `get` behavior.
- `getMapCondition()`
  - Executes `getMapCondition` behavior.
- `getDensityCondition()`
  - Executes `getDensityCondition` behavior.
- `getParentCondition()`
  - Executes `getParentCondition` behavior.
- `getType()`
  - Executes `getType` behavior.
- `getOffset()`
  - Executes `getOffset` behavior.
- `getEntry()`
  - Executes `getEntry` behavior.
- `toString()`
  - Executes `toString` behavior.
- `getTypes()`
  - Executes `getTypes` behavior.
- `getAnchor()`
  - Executes `getAnchor` behavior.
- `getRotation(@Nonnull Random random)`
  - Executes `getRotation` behavior.
- `getChildrenLimit()`
  - Executes `getChildrenLimit` behavior.
- `getRepeat()`
  - Executes `getRepeat` behavior.
- `getPitchModifier()`
  - Executes `getPitchModifier` behavior.
- `getYawModifier()`
  - Executes `getYawModifier` behavior.
- `getChance()`
  - Executes `getChance` behavior.
- `getYawMode()`
  - Executes `getYawMode` behavior.
- `calc(float var1, Random var2)`
  - Executes `calc` behavior.

## Notes
- No additional notes.
