# PondFillerProp

## Overview
- Documentation for `PondFillerProp`.
- Declared as a class in `com.hypixel.hytale.builtin.hytalegenerator.props.filler`.

## Constructors
- `PondFillerProp(@Nonnull Vector3i boundingMin, @Nonnull Vector3i boundingMax, @Nonnull MaterialSet solidSet, @Nonnull MaterialProvider<Material> filledMaterialProvider, @Nonnull Scanner scanner, @Nonnull Pattern pattern)`
  - Creates a `PondFillerProp` instance.

## Methods
- `scan(@Nonnull Vector3i position, @Nonnull VoxelSpace<Material> materialSpace, @Nonnull WorkerIndexer.Id id)`
  - Executes `scan` behavior.
- `renderFluidBlocks(@Nonnull Vector3i origin, @Nonnull VoxelSpace<Material> materialSpace)`
  - Executes `renderFluidBlocks` behavior.
- `place(@Nonnull Prop.Context context)`
  - Executes `place` behavior.
- `getContextDependency()`
  - Executes `getContextDependency` behavior.
- `getWriteBounds()`
  - Executes `getWriteBounds` behavior.
- `isTraversed(int maskValue)`
  - Executes `isTraversed` behavior.
- `isLeaks(int maskValue)`
  - Executes `isLeaks` behavior.
- `isSolid(int maskValue)`
  - Executes `isSolid` behavior.
- `isStacked(int maskValue)`
  - Executes `isStacked` behavior.

## Notes
- No additional notes.
