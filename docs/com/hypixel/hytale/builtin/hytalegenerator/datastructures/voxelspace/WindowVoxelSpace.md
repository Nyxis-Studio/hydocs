# WindowVoxelSpace

## Overview
- Documentation for `WindowVoxelSpace`.
- Declared as a class in `com.hypixel.hytale.builtin.hytalegenerator.datastructures.voxelspace`.

## Constructors
- `WindowVoxelSpace(@Nonnull VoxelSpace<T> voxelSpace)`
  - Creates a `WindowVoxelSpace` instance.

## Methods
- `setWindow(int minX, int minY, int minZ, int maxX, int maxY, int maxZ)`
  - Executes `setWindow` behavior.
- `getWrappedSchematic()`
  - Executes `getWrappedSchematic` behavior.
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
- `pasteFrom(@Nonnull VoxelSpace<T> source)`
  - Executes `pasteFrom` behavior.
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
- `sizeX()`
  - Executes `sizeX` behavior.
- `sizeY()`
  - Executes `sizeY` behavior.
- `sizeZ()`
  - Executes `sizeZ` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
