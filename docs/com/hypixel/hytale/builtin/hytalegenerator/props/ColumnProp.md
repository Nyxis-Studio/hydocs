# ColumnProp

## Overview
- Documentation for `ColumnProp`.
- Declared as a class in `com.hypixel.hytale.builtin.hytalegenerator.props`.

## Constructors
- `ColumnProp(@Nonnull List<Integer> propYPositions, @Nonnull List<Material> blocks, @Nonnull BlockMask blockMask, @Nonnull Scanner scanner, @Nonnull Directionality directionality, @Nonnull MaterialCache materialCache)`
  - Creates a `ColumnProp` instance.

## Methods
- `scan(@Nonnull Vector3i position, @Nonnull VoxelSpace<Material> materialSpace, @Nonnull WorkerIndexer.Id id)`
  - Executes `scan` behavior.
- `place(@Nonnull Prop.Context context)`
  - Executes `place` behavior.
- `place(@Nonnull RotatedPosition position, @Nonnull VoxelSpace<Material> materialSpace)`
  - Executes `place` behavior.
- `getContextDependency()`
  - Executes `getContextDependency` behavior.
- `getWriteBounds()`
  - Executes `getWriteBounds` behavior.

## Notes
- No additional notes.
