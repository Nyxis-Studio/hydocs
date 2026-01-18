**Source Hash:** `fdf1518d61963eb775b93c4e24256ede491586ecf05e0d416055e72ac8c8f285`

# ContextDependency

## Overview

## Constructor Descriptions
- `ContextDependency(new Vector3i()`
  - Creates a `ContextDependency` instance.
- `ContextDependency(@Nonnull Vector3i readRange, @Nonnull Vector3i writeRange)`
  - Creates a `ContextDependency` instance.
- `ContextDependency()`
  - Creates a `ContextDependency` instance.
- `ContextDependency(totalRead, totalWrite)`
  - Creates a `ContextDependency` instance.
- `ContextDependency(read, write)`
  - Creates a `ContextDependency` instance.
- `ContextDependency(this.readRange, this.writeRange)`
  - Creates a `ContextDependency` instance.

## Method Descriptions
- `getTotalPropBounds_voxelGrid()`: Add description.
  - Executes `getTotalPropBounds_voxelGrid` behavior.
- `update()`: Add description.
  - Executes `update` behavior.
- `stackOver(@Nonnull ContextDependency other)`: Add description.
  - Executes `stackOver` behavior.
- `getReadRange()`: Add description.
  - Executes `getReadRange` behavior.
- `getWriteRange()`: Add description.
  - Executes `getWriteRange` behavior.
- `getTrashRange()`: Add description.
  - Executes `getTrashRange` behavior.
- `getExternalDependencyRange()`: Add description.
  - Executes `getExternalDependencyRange` behavior.
- `getPositioningRange()`: Add description.
  - Executes `getPositioningRange` behavior.
- `getRequiredPadOf(@Nonnull List<ContextDependency> dependencies)`: Add description.
  - Executes `getRequiredPadOf` behavior.
- `cloneMap(@Nonnull Map<Integer, ContextDependency> map)`: Add description.
  - Executes `cloneMap` behavior.
- `stackMaps(@Nonnull Map<Integer, ContextDependency> under, @Nonnull Map<Integer, ContextDependency> over)`: Add description.
  - Executes `stackMaps` behavior.
- `mostOf(@Nonnull List<ContextDependency> dependencies)`: Add description.
  - Executes `mostOf` behavior.
- `mostOf(@Nonnull ContextDependency a, @Nonnull ContextDependency b)`: Add description.
  - Executes `mostOf` behavior.
- `clone()`: Add description.
  - Executes `clone` behavior.

## Notes
- No additional notes.
