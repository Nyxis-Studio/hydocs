**Source Hash:** `cc01a0e63fbbed776455877f4bf5567d17db830f5c8c251a82aeac5913f2a88b`

# BooleanVoxelSpace

## Overview

## Constructor Descriptions
- `BooleanVoxelSpace(int sizeX, int sizeY, int sizeZ, int originX, int originY, int originZ, boolean alignedOriginZ)`
  - Creates a `BooleanVoxelSpace` instance.
- `BooleanVoxelSpace(int sizeX, int sizeY, int sizeZ, int originX, int originY, int originZ)`
  - Creates a `BooleanVoxelSpace` instance.
- `BooleanVoxelSpace(int sizeX, int sizeY, int sizeZ)`
  - Creates a `BooleanVoxelSpace` instance.
- `BooleanVoxelSpace(int sizeX, int sizeY, int sizeZ, boolean forceAlignOriginZ)`
  - Creates a `BooleanVoxelSpace` instance.
- `BooleanVoxelSpace(this.sizeX, this.sizeY, this.sizeZ, this.origin.x, this.origin.y, this.origin.z)`
  - Creates a `BooleanVoxelSpace` instance.

## Method Descriptions
- `sizeX()`: Add description.
  - Executes `sizeX` behavior.
- `sizeY()`: Add description.
  - Executes `sizeY` behavior.
- `sizeZ()`: Add description.
  - Executes `sizeZ` behavior.
- `pasteFrom(@Nonnull VoxelSpace<Boolean> source)`: Add description.
  - Executes `pasteFrom` behavior.
- `primaryAddressIndex(int x, int y)`: Add description.
  - Executes `primaryAddressIndex` behavior.
- `secondaryAddressIndex(int z)`: Add description.
  - Executes `secondaryAddressIndex` behavior.
- `setBit(int bits, int index, boolean value)`: Add description.
  - Executes `setBit` behavior.
- `getBit(int bits, int index)`: Add description.
  - Executes `getBit` behavior.
- `set(@Nullable Boolean value, int x, int y, int z)`: Add description.
  - Executes `set` behavior.
- `set(Boolean content, @Nonnull Vector3i position)`: Add description.
  - Executes `set` behavior.
- `getContent(int x, int y, int z)`: Add description.
  - Executes `getContent` behavior.
- `getContent(@Nonnull Vector3i position)`: Add description.
  - Executes `getContent` behavior.
- `globalJ(int globalZ)`: Add description.
  - Executes `globalJ` behavior.
- `localJ(int globalJ)`: Add description.
  - Executes `localJ` behavior.
- `deepCopyFrom(@Nonnull BooleanVoxelSpace other)`: Add description.
  - Executes `deepCopyFrom` behavior.
- `set(Boolean content)`: Add description.
  - Executes `set` behavior.
- `setOrigin(int x, int y, int z)`: Add description.
  - Executes `setOrigin` behavior.
- `replace(Boolean replacement, int x, int y, int z, @Nonnull Predicate<Boolean> mask)`: Add description.
  - Executes `replace` behavior.
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
- `forEach(@Nonnull VoxelConsumer<? super Boolean> action)`: Add description.
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
- `clone()`: Add description.
  - Executes `clone` behavior.
- `arrayIndex(int x, int y, int z)`: Add description.
  - Executes `arrayIndex` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.
- `isAlignedOriginZ(int z)`: Add description.
  - Executes `isAlignedOriginZ` behavior.
- `getAlignedZ(int z)`: Add description.
  - Executes `getAlignedZ` behavior.

## Notes
- No additional notes.
