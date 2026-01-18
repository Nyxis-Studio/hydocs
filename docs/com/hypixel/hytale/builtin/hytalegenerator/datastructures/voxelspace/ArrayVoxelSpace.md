# ArrayVoxelSpace

## Overview
- Documentation for `ArrayVoxelSpace`.
- Declared as a class in `com.hypixel.hytale.builtin.hytalegenerator.datastructures.voxelspace`.

## Constructors
- `ArrayVoxelSpace(@Nonnull Bounds3i bounds)`
  - Creates a `ArrayVoxelSpace` instance.
- `ArrayVoxelSpace(@Nonnull String name, int sizeX, int sizeY, int sizeZ, int originX, int originY, int originZ)`
  - Creates a `ArrayVoxelSpace` instance.
- `ArrayVoxelSpace(int sizeX, int sizeY, int sizeZ)`
  - Creates a `ArrayVoxelSpace` instance.
- `ArrayVoxelSpace(@Nonnull VoxelSpace<T> voxelSpace)`
  - Creates a `ArrayVoxelSpace` instance.
- `ArrayVoxelSpace(this.name, this.sizeX, this.sizeY, this.sizeZ, this.origin.x, this.origin.y, this.origin.z)`
  - Creates a `ArrayVoxelSpace` instance.

## Methods
- `setFastResetTo(T e)`
  - Executes `setFastResetTo` behavior.
- `disableFastReset()`
  - Executes `disableFastReset` behavior.
- `hasFastReset()`
  - Executes `hasFastReset` behavior.
- `fastReset()`
  - Executes `fastReset` behavior.
- `sizeX()`
  - Executes `sizeX` behavior.
- `sizeY()`
  - Executes `sizeY` behavior.
- `sizeZ()`
  - Executes `sizeZ` behavior.
- `pasteFrom(@Nonnull VoxelSpace<T> source)`
  - Executes `pasteFrom` behavior.
- `set(T content, int x, int y, int z)`
  - Executes `set` behavior.
- `set(T content, @Nonnull Vector3i position)`
  - Executes `set` behavior.
- `set(T content)`
  - Executes `set` behavior.
- `setOrigin(int x, int y, int z)`
  - Executes `setOrigin` behavior.
- `getContent(int x, int y, int z)`
  - Executes `getContent` behavior.
- `getContent(@Nonnull Vector3i position)`
  - Executes `getContent` behavior.
- `replace(T replacement, int x, int y, int z, @Nonnull Predicate<T> mask)`
  - Executes `replace` behavior.
- `toArray()`
  - Executes `toArray` behavior.
- `getOriginX()`
  - Executes `getOriginX` behavior.
- `getOriginY()`
  - Executes `getOriginY` behavior.
- `getOriginZ()`
  - Executes `getOriginZ` behavior.
- `getName()`
  - Executes `getName` behavior.
- `isInsideSpace(int x, int y, int z)`
  - Executes `isInsideSpace` behavior.
- `isInsideSpace(@Nonnull Vector3i position)`
  - Executes `isInsideSpace` behavior.
- `forEach(@Nonnull VoxelConsumer<? super T> action)`
  - Executes `forEach` behavior.
- `minX()`
  - Executes `minX` behavior.
- `maxX()`
  - Executes `maxX` behavior.
- `minY()`
  - Executes `minY` behavior.
- `maxY()`
  - Executes `maxY` behavior.
- `minZ()`
  - Executes `minZ` behavior.
- `maxZ()`
  - Executes `maxZ` behavior.
- `clone()`
  - Executes `clone` behavior.
- `arrayIndex(int x, int y, int z)`
  - Executes `arrayIndex` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
