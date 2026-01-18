# NVoxelBufferView

## Overview
- Documentation for `NVoxelBufferView`.
- Declared as a class in `com.hypixel.hytale.builtin.hytalegenerator.newsystem.views`.

## Constructors
- `NVoxelBufferView(@Nonnull NBufferBundle.Access.View bufferAccess, @Nonnull Class<T> voxelType)`
  - Creates a `NVoxelBufferView` instance.

## Methods
- `copyFrom(@Nonnull NVoxelBufferView<T> source)`
  - Executes `copyFrom` behavior.
- `set(T content, int x, int y, int z)`
  - Executes `set` behavior.
- `set(T content, @Nonnull Vector3i position_voxelGrid)`
  - Executes `set` behavior.
- `set(T content)`
  - Executes `set` behavior.
- `setOrigin(int x, int y, int z)`
  - Executes `setOrigin` behavior.
- `getContent(int x, int y, int z)`
  - Executes `getContent` behavior.
- `getContent(@Nonnull Vector3i position_voxelGrid)`
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
- `forEach(VoxelConsumer<? super T> action)`
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
- `getBuffer_fromVoxelGrid(@Nonnull Vector3i position_voxelGrid)`
  - Executes `getBuffer_fromVoxelGrid` behavior.
- `getBuffer_fromBufferGrid(@Nonnull Vector3i position_bufferGrid)`
  - Executes `getBuffer_fromBufferGrid` behavior.

## Notes
- No additional notes.
