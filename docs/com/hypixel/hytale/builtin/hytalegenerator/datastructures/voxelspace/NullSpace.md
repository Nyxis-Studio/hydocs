# NullSpace

## Overview
- Documentation for `NullSpace`.
- Declared as a class in `com.hypixel.hytale.builtin.hytalegenerator.datastructures.voxelspace`.

## Constructors
- `NullSpace()`
  - Creates a `NullSpace` instance.

## Methods
- `instance()`
  - Executes `instance` behavior.
- `instance(@Nonnull Class<V> clazz)`
  - Executes `instance` behavior.
- `set(V content, int x, int y, int z)`
  - Executes `set` behavior.
- `set(V content, @Nonnull Vector3i position)`
  - Executes `set` behavior.
- `set(V content)`
  - Executes `set` behavior.
- `setOrigin(int x, int y, int z)`
  - Executes `setOrigin` behavior.
- `getContent(int x, int y, int z)`
  - Executes `getContent` behavior.
- `getContent(@Nonnull Vector3i position)`
  - Executes `getContent` behavior.
- `replace(V replacement, int x, int y, int z, @Nonnull Predicate<V> mask)`
  - Executes `replace` behavior.
- `pasteFrom(@Nonnull VoxelSpace<V> source)`
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
- `forEach(VoxelConsumer<? super V> action)`
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

## Notes
- No additional notes.
