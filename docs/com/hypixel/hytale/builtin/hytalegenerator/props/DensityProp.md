# DensityProp

## Overview
- Documentation for `DensityProp`.
- Declared as a class in `com.hypixel.hytale.builtin.hytalegenerator.props`.

## Constructors
- `DensityProp(@Nonnull Vector3i range, @Nonnull Density density, @Nonnull MaterialProvider<Material> materialProvider, @Nonnull Scanner scanner, @Nonnull Pattern pattern, @Nonnull BlockMask placementMask, @Nonnull Material defaultMaterial)`
  - Creates a `DensityProp` instance.

## Methods
- `scan(@Nonnull Vector3i position, @Nonnull VoxelSpace<Material> materialSpace, @Nonnull WorkerIndexer.Id id)`
  - Executes `scan` behavior.
- `place(@Nonnull Prop.Context context)`
  - Executes `place` behavior.
- `place(Vector3i position, @Nonnull VoxelSpace<Material> materialSpace, @Nonnull WorkerIndexer.Id id)`
  - Executes `place` behavior.
- `getContextDependency()`
  - Executes `getContextDependency` behavior.
- `getWriteBounds()`
  - Executes `getWriteBounds` behavior.

## Notes
- No additional notes.
