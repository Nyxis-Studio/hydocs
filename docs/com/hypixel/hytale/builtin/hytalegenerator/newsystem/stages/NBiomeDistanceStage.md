**Source Hash:** `c6505f02d99a6a4eda1a191499e9e16d08f0c9a97cbdde0a9f76594f5253c014`

# NBiomeDistanceStage

## Overview

## Constructor Descriptions
- `NBiomeDistanceStage(@Nonnull String stageName, @Nonnull NParametrizedBufferType biomeInputBufferType, @Nonnull NParametrizedBufferType biomeDistanceOutputBufferType, double maxDistance_voxelGrid)`
  - Creates a `NBiomeDistanceStage` instance.

## Method Descriptions
- `run(@Nonnull NStage.Context context)`: Add description.
  - Executes `run` behavior.
- `createDistanceTracker(@Nonnull NBufferBundle.Access.View biomeAccess, @Nonnull NPixelBufferView<BiomeType> biomeSpace, @Nonnull Vector3i targetPosition_voxelGrid)`: Add description.
  - Executes `createDistanceTracker` behavior.
- `getInputTypesAndBounds_bufferGrid()`: Add description.
  - Executes `getInputTypesAndBounds_bufferGrid` behavior.
- `getOutputTypes()`: Add description.
  - Executes `getOutputTypes` behavior.
- `getName()`: Add description.
  - Executes `getName` behavior.
- `distanceToBuffer_voxelGrid(@Nonnull Vector3i position_voxelGrid, @Nonnull Vector3i position_bufferGrid)`: Add description.
  - Executes `distanceToBuffer_voxelGrid` behavior.
- `allBiomesAreCountedAndFarther(@Nonnull BiomeDistanceCounter counter, @Nonnull List<BiomeType> uniqueBiomes, double distanceToBuffer_voxelGrid)`: Add description.
  - Executes `allBiomesAreCountedAndFarther` behavior.
- `distanceToClosestOtherBiome(@Nonnull BiomeType thisBiome)`: Add description.
  - Executes `distanceToClosestOtherBiome` behavior.

## Notes
- No additional notes.
