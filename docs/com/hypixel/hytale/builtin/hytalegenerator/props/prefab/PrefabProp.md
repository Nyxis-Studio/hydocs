# PrefabProp

## Overview
- Documentation for `PrefabProp`.
- Declared as a class in `com.hypixel.hytale.builtin.hytalegenerator.props.prefab`.

## Constructors
- `PrefabProp(@Nonnull WeightedMap<List<PrefabBuffer>> prefabPool, @Nonnull Scanner scanner, @Nonnull Directionality directionality, @Nonnull MaterialCache materialCache, @Nonnull BlockMask materialMask, @Nonnull PrefabMoldingConfiguration prefabMoldingConfiguration, @Nullable Function<String, List<PrefabBuffer>> childPrefabLoader, @Nonnull SeedBox seedBox, boolean loadEntities)`
  - Creates a `PrefabProp` instance.
- `PrefabProp(weightedChildPrefabs, OriginScanner.getInstance()`
  - Creates a `PrefabProp` instance.

## Methods
- `getWriteRange(PrefabBuffer.PrefabBufferAccessor prefabAccess)`
  - Executes `getWriteRange` behavior.
- `scan(@Nonnull Vector3i position, @Nonnull VoxelSpace<Material> materialSpace, @Nonnull WorkerIndexer.Id id)`
  - Executes `scan` behavior.
- `place(@Nonnull Prop.Context context)`
  - Executes `place` behavior.
- `pickPrefab(Random rand)`
  - Executes `pickPrefab` behavior.
- `place(RotatedPosition position, @Nonnull VoxelSpace<Material> materialSpace, @Nonnull EntityContainer entityBuffer, @Nonnull WorkerIndexer.Id id)`
  - Executes `place` behavior.
- `getContextDependency()`
  - Executes `getContextDependency` behavior.
- `getWriteBounds()`
  - Executes `getWriteBounds` behavior.

## Notes
- No additional notes.
