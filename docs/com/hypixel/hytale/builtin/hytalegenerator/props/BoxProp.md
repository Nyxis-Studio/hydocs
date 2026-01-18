# BoxProp

## Overview
- Documentation for `BoxProp`.
- Declared as a class in `com.hypixel.hytale.builtin.hytalegenerator.props`.

## Constructors
- `BoxProp(Vector3i range, @Nonnull Material material, @Nonnull Scanner scanner, @Nonnull Pattern pattern)`
  - Creates a `BoxProp` instance.

## Methods
- `scan(@Nonnull Vector3i position, @Nonnull VoxelSpace<Material> materialSpace, @Nonnull WorkerIndexer.Id id)`
  - Executes `scan` behavior.
- `place(@Nonnull Prop.Context context)`
  - Executes `place` behavior.
- `place(@Nonnull Vector3i position, @Nonnull VoxelSpace<Material> materialSpace)`
  - Executes `place` behavior.
- `getContextDependency()`
  - Executes `getContextDependency` behavior.
- `getWriteBounds()`
  - Executes `getWriteBounds` behavior.

## Notes
- No additional notes.
