**Source Hash:** `ced590da163dba1190151aeda1e49ef6675dc3fc5f0b839ba2efd670e6b905aa`

# NVoxelBufferView

## Overview

## Constructor Descriptions
- `NVoxelBufferView(@Nonnull NBufferBundle.Access.View bufferAccess, @Nonnull Class<T> voxelType)`
  - Creates a `NVoxelBufferView` instance.

## Method Descriptions
- `copyFrom(@Nonnull NVoxelBufferView<T> source)`: Add description.
  - Executes `copyFrom` behavior.
- `set(T content, int x, int y, int z)`: Add description.
  - Executes `set` behavior.
- `set(T content, @Nonnull Vector3i position_voxelGrid)`: Add description.
  - Executes `set` behavior.
- `set(T content)`: Add description.
  - Executes `set` behavior.
- `setOrigin(int x, int y, int z)`: Add description.
  - Executes `setOrigin` behavior.
- `getContent(int x, int y, int z)`: Add description.
  - Executes `getContent` behavior.
- `getContent(@Nonnull Vector3i position_voxelGrid)`: Add description.
  - Executes `getContent` behavior.
- `replace(T replacement, int x, int y, int z, @Nonnull Predicate<T> mask)`: Add description.
  - Executes `replace` behavior.
- `pasteFrom(@Nonnull VoxelSpace<T> source)`: Add description.
  - Executes `pasteFrom` behavior.
- `getOriginX()`: Add description.
  - Executes `getOriginX` behavior.
- `getOriginY()`: Add description.
  - Executes `getOriginY` behavior.
- `getOriginZ()`: Add description.
  - Executes `getOriginZ` behavior.
- `getName()`: Add description.
  - Executes `getName` behavior.
- `isInsideSpace(int x, int y, int z)`: Add description.
  - Executes `isInsideSpace` behavior.
- `isInsideSpace(@Nonnull Vector3i position)`: Add description.
  - Executes `isInsideSpace` behavior.
- `forEach(VoxelConsumer<? super T> action)`: Add description.
  - Executes `forEach` behavior.
- `minX()`: Add description.
  - Executes `minX` behavior.
- `maxX()`: Add description.
  - Executes `maxX` behavior.
- `minY()`: Add description.
  - Executes `minY` behavior.
- `maxY()`: Add description.
  - Executes `maxY` behavior.
- `minZ()`: Add description.
  - Executes `minZ` behavior.
- `maxZ()`: Add description.
  - Executes `maxZ` behavior.
- `sizeX()`: Add description.
  - Executes `sizeX` behavior.
- `sizeY()`: Add description.
  - Executes `sizeY` behavior.
- `sizeZ()`: Add description.
  - Executes `sizeZ` behavior.
- `getBuffer_fromVoxelGrid(@Nonnull Vector3i position_voxelGrid)`: Add description.
  - Executes `getBuffer_fromVoxelGrid` behavior.
- `getBuffer_fromBufferGrid(@Nonnull Vector3i position_bufferGrid)`: Add description.
  - Executes `getBuffer_fromBufferGrid` behavior.

## Notes
- No additional notes.
