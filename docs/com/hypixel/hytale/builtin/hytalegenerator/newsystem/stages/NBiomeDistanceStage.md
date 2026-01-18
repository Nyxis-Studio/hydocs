# NBiomeDistanceStage

## Overview
- Documentation for `NBiomeDistanceStage`.
- Declared as a class in `com.hypixel.hytale.builtin.hytalegenerator.newsystem.stages`.

## Constructors
- `NBiomeDistanceStage(@Nonnull String stageName, @Nonnull NParametrizedBufferType biomeInputBufferType, @Nonnull NParametrizedBufferType biomeDistanceOutputBufferType, double maxDistance_voxelGrid)`
  - Creates a `NBiomeDistanceStage` instance.

## Methods
- `run(@Nonnull NStage.Context context)`
  - Executes `run` behavior.
- `createDistanceTracker(@Nonnull NBufferBundle.Access.View biomeAccess, @Nonnull NPixelBufferView<BiomeType> biomeSpace, @Nonnull Vector3i targetPosition_voxelGrid)`
  - Executes `createDistanceTracker` behavior.
- `getInputTypesAndBounds_bufferGrid()`
  - Executes `getInputTypesAndBounds_bufferGrid` behavior.
- `getOutputTypes()`
  - Executes `getOutputTypes` behavior.
- `getName()`
  - Executes `getName` behavior.
- `distanceToBuffer_voxelGrid(@Nonnull Vector3i position_voxelGrid, @Nonnull Vector3i position_bufferGrid)`
  - Executes `distanceToBuffer_voxelGrid` behavior.
- `allBiomesAreCountedAndFarther(@Nonnull BiomeDistanceCounter counter, @Nonnull List<BiomeType> uniqueBiomes, double distanceToBuffer_voxelGrid)`
  - Executes `allBiomesAreCountedAndFarther` behavior.
- `distanceToClosestOtherBiome(@Nonnull BiomeType thisBiome)`
  - Executes `distanceToClosestOtherBiome` behavior.

## Notes
- No additional notes.
