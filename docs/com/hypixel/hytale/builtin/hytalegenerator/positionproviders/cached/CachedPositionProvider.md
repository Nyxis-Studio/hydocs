# CachedPositionProvider

## Overview
- Documentation for `CachedPositionProvider`.
- Declared as a class in `com.hypixel.hytale.builtin.hytalegenerator.positionproviders.cached`.

## Constructors
- `CachedPositionProvider(@Nonnull PositionProvider positionProvider, int sectionSize, int cacheSize, boolean useInternalThreadData, int threadCount)`
  - Creates a `CachedPositionProvider` instance.

## Methods
- `positionsIn(@Nonnull PositionProvider.Context context)`
  - Executes `positionsIn` behavior.
- `get(@Nonnull PositionProvider.Context context)`
  - Executes `get` behavior.
- `sectionAddress(@Nonnull Vector3d pointer)`
  - Executes `sectionAddress` behavior.
- `sectionMin(@Nonnull Vector3i sectionAddress)`
  - Executes `sectionMin` behavior.
- `toSectionAddress(double position)`
  - Executes `toSectionAddress` behavior.
- `sectionFloor(int voxelAddress)`
  - Executes `sectionFloor` behavior.

## Notes
- No additional notes.
