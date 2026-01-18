**Source Hash:** `2c77c5c1c49c305084e5b310be0fc39e6997551932d71461e12e4a9e4621ee9d`

# PrefabProp

## Overview

## Constructor Descriptions
- `PrefabProp(@Nonnull WeightedMap<List<PrefabBuffer>> prefabPool, @Nonnull Scanner scanner, @Nonnull Directionality directionality, @Nonnull MaterialCache materialCache, @Nonnull BlockMask materialMask, @Nonnull PrefabMoldingConfiguration prefabMoldingConfiguration, @Nullable Function<String, List<PrefabBuffer>> childPrefabLoader, @Nonnull SeedBox seedBox, boolean loadEntities)`
  - Creates a `PrefabProp` instance.
- `PrefabProp(weightedChildPrefabs, OriginScanner.getInstance()`
  - Creates a `PrefabProp` instance.

## Method Descriptions
- `getWriteRange(PrefabBuffer.PrefabBufferAccessor prefabAccess)`: Add description.
  - Executes `getWriteRange` behavior.
- `scan(@Nonnull Vector3i position, @Nonnull VoxelSpace<Material> materialSpace, @Nonnull WorkerIndexer.Id id)`: Add description.
  - Executes `scan` behavior.
- `place(@Nonnull Prop.Context context)`: Add description.
  - Executes `place` behavior.
- `pickPrefab(Random rand)`: Add description.
  - Executes `pickPrefab` behavior.
- `place(RotatedPosition position, @Nonnull VoxelSpace<Material> materialSpace, @Nonnull EntityContainer entityBuffer, @Nonnull WorkerIndexer.Id id)`: Add description.
  - Executes `place` behavior.
- `getContextDependency()`: Add description.
  - Executes `getContextDependency` behavior.
- `getWriteBounds()`: Add description.
  - Executes `getWriteBounds` behavior.

## Notes
- No additional notes.
