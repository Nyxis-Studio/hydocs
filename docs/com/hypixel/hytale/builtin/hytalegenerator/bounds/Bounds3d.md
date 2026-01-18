# Bounds3d

## Overview
- Documentation for `Bounds3d`.
- Declared as a class in `com.hypixel.hytale.builtin.hytalegenerator.bounds`.

## Constructors
- `Bounds3d()`
  - Creates a `Bounds3d` instance.
- `Bounds3d(@Nonnull Vector3d min, @Nonnull Vector3d max)`
  - Creates a `Bounds3d` instance.
- `Bounds3d(this.min.clone()`
  - Creates a `Bounds3d` instance.

## Methods
- `contains(@Nonnull Vector3d position)`
  - Executes `contains` behavior.
- `contains(@Nonnull Bounds3d other)`
  - Executes `contains` behavior.
- `intersects(@Nonnull Bounds3d other)`
  - Executes `intersects` behavior.
- `isZeroVolume()`
  - Executes `isZeroVolume` behavior.
- `getSize()`
  - Executes `getSize` behavior.
- `assign(@Nonnull Bounds3d other)`
  - Executes `assign` behavior.
- `assign(@Nonnull Vector3d min, @Nonnull Vector3d max)`
  - Executes `assign` behavior.
- `offset(@Nonnull Vector3d vector)`
  - Executes `offset` behavior.
- `intersect(@Nonnull Bounds3d other)`
  - Executes `intersect` behavior.
- `encompass(@Nonnull Bounds3d other)`
  - Executes `encompass` behavior.
- `encompass(@Nonnull Vector3d position)`
  - Executes `encompass` behavior.
- `stack(@Nonnull Bounds3d other)`
  - Executes `stack` behavior.
- `flipOnOriginPoint()`
  - Executes `flipOnOriginPoint` behavior.
- `flipOnOriginVoxel()`
  - Executes `flipOnOriginVoxel` behavior.
- `clone()`
  - Executes `clone` behavior.
- `isCorrect()`
  - Executes `isCorrect` behavior.
- `correct()`
  - Executes `correct` behavior.

## Notes
- No additional notes.
