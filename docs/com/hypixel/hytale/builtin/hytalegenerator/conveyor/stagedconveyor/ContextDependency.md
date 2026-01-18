# ContextDependency

## Overview
- Documentation for `ContextDependency`.
- Declared as a class in `com.hypixel.hytale.builtin.hytalegenerator.conveyor.stagedconveyor`.

## Constructors
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

## Methods
- `getTotalPropBounds_voxelGrid()`
  - Executes `getTotalPropBounds_voxelGrid` behavior.
- `update()`
  - Executes `update` behavior.
- `stackOver(@Nonnull ContextDependency other)`
  - Executes `stackOver` behavior.
- `getReadRange()`
  - Executes `getReadRange` behavior.
- `getWriteRange()`
  - Executes `getWriteRange` behavior.
- `getTrashRange()`
  - Executes `getTrashRange` behavior.
- `getExternalDependencyRange()`
  - Executes `getExternalDependencyRange` behavior.
- `getPositioningRange()`
  - Executes `getPositioningRange` behavior.
- `getRequiredPadOf(@Nonnull List<ContextDependency> dependencies)`
  - Executes `getRequiredPadOf` behavior.
- `cloneMap(@Nonnull Map<Integer, ContextDependency> map)`
  - Executes `cloneMap` behavior.
- `stackMaps(@Nonnull Map<Integer, ContextDependency> under, @Nonnull Map<Integer, ContextDependency> over)`
  - Executes `stackMaps` behavior.
- `mostOf(@Nonnull List<ContextDependency> dependencies)`
  - Executes `mostOf` behavior.
- `mostOf(@Nonnull ContextDependency a, @Nonnull ContextDependency b)`
  - Executes `mostOf` behavior.
- `clone()`
  - Executes `clone` behavior.

## Notes
- No additional notes.
