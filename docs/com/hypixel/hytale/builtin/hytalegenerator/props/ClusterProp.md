# ClusterProp

## Overview
- Documentation for `ClusterProp`.
- Declared as a class in `com.hypixel.hytale.builtin.hytalegenerator.props`.

## Constructors
- `ClusterProp(int range, @Nonnull Double2DoubleFunction weightCurve, int seed, @Nonnull WeightedMap<Prop> propWeightedMap, @Nonnull Pattern pattern, @Nonnull Scanner scanner)`
  - Creates a `ClusterProp` instance.

## Methods
- `scan(@Nonnull Vector3i position, @Nonnull VoxelSpace<Material> materialSpace, @Nonnull WorkerIndexer.Id id)`
  - Executes `scan` behavior.
- `place(@Nonnull Prop.Context context)`
  - Executes `place` behavior.
- `place(@Nonnull Vector3i position, @Nonnull VoxelSpace<Material> materialSpace, @Nonnull EntityContainer entityBuffer, @Nonnull WorkerIndexer.Id id, double distanceFromBiomeEdge)`
  - Executes `place` behavior.
- `getContextDependency()`
  - Executes `getContextDependency` behavior.
- `getWriteBounds()`
  - Executes `getWriteBounds` behavior.

## Notes
- No additional notes.
