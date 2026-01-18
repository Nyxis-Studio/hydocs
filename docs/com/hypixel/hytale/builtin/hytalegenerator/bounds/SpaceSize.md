# SpaceSize

## Overview
- Documentation for `SpaceSize`.
- Declared as a class in `com.hypixel.hytale.builtin.hytalegenerator.bounds`.

## Constructors
- `SpaceSize(@Nonnull Vector3i minInclusive, @Nonnull Vector3i maxExclusive)`
  - Creates a `SpaceSize` instance.
- `SpaceSize(@Nonnull Vector3i voxel)`
  - Creates a `SpaceSize` instance.
- `SpaceSize()`
  - Creates a `SpaceSize` instance.
- `SpaceSize(this.minInclusive, this.maxExclusive)`
  - Creates a `SpaceSize` instance.
- `SpaceSize(Vector3i.min(a.minInclusive, b.minInclusive)`
  - Creates a `SpaceSize` instance.
- `SpaceSize(stackedMin, stackedMax)`
  - Creates a `SpaceSize` instance.
- `SpaceSize(new Vector3i()`
  - Creates a `SpaceSize` instance.

## Methods
- `moveBy(@Nonnull Vector3i delta)`
  - Executes `moveBy` behavior.
- `getMinInclusive()`
  - Executes `getMinInclusive` behavior.
- `getMaxExclusive()`
  - Executes `getMaxExclusive` behavior.
- `getMaxInclusive()`
  - Executes `getMaxInclusive` behavior.
- `getRange()`
  - Executes `getRange` behavior.
- `clone()`
  - Executes `clone` behavior.
- `merge(@Nonnull SpaceSize a, @Nonnull SpaceSize b)`
  - Executes `merge` behavior.
- `stack(@Nonnull SpaceSize a, @Nonnull SpaceSize b)`
  - Executes `stack` behavior.
- `empty()`
  - Executes `empty` behavior.

## Notes
- No additional notes.
