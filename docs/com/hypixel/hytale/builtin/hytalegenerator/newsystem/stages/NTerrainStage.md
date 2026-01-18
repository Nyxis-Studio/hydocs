**Source Hash:** `f6ac1a01201b65bd6c021b9bd926dd7b5e5b5f326058bc1f7369214d9d1767cf`

# NTerrainStage

## Overview

## Constructor Descriptions
- `NTerrainStage(@Nonnull String stageName, @Nonnull NParametrizedBufferType biomeInputBufferType, @Nonnull NParametrizedBufferType biomeDistanceInputBufferType, @Nonnull NParametrizedBufferType materialOutputBufferType, int maxInterpolationRadius_voxelGrid, @Nonnull MaterialCache materialCache, @Nonnull WorkerIndexer workerIndexer)`
  - Creates a `NTerrainStage` instance.

## Method Descriptions
- `run(@Nonnull NStage.Context context)`: Add description.
  - Executes `run` behavior.
- `getInputTypesAndBounds_bufferGrid()`: Add description.
  - Executes `getInputTypesAndBounds_bufferGrid` behavior.
- `getOutputTypes()`: Add description.
  - Executes `getOutputTypes` behavior.
- `getName()`: Add description.
  - Executes `getName` behavior.
- `generateDensity(@Nonnull FloatContainer3d densityBuffer, @Nonnull NPixelBufferView<BiomeType> biomeSpace, @Nonnull NPixelBufferView<NBiomeDistanceStage.BiomeDistanceEntries> distanceSpace, @Nonnull WorkerIndexer.Id workerId)`: Add description.
  - Executes `generateDensity` behavior.
- `getOrGenerateDensity(@Nonnull Vector3i position_voxelGrid, @Nonnull FloatContainer3d densityBuffer, @Nonnull NPixelBufferView<BiomeType> biomeSpace, @Nonnull NPixelBufferView<NBiomeDistanceStage.BiomeDistanceEntries> distanceSpace, @Nonnull WorkerIndexer.Id workerId)`: Add description.
  - Executes `getOrGenerateDensity` behavior.
- `generateDensity(@Nonnull Vector3i position_voxelGrid, @Nonnull NPixelBufferView<BiomeType> biomeSpace, @Nonnull NPixelBufferView<NBiomeDistanceStage.BiomeDistanceEntries> distanceSpace, @Nonnull WorkerIndexer.Id workerId)`: Add description.
  - Executes `generateDensity` behavior.
- `generateMaterials(@Nonnull NPixelBufferView<BiomeType> biomeSpace, @Nonnull NPixelBufferView<NBiomeDistanceStage.BiomeDistanceEntries> distanceSpace, @Nonnull FloatContainer3d densityBuffer, @Nonnull NVoxelBufferView<Material> materialSpace, @Nonnull WorkerIndexer.Id workerId)`: Add description.
  - Executes `generateMaterials` behavior.
- `createWeights(@Nonnull NBiomeDistanceStage.BiomeDistanceEntries distances, @Nonnull BiomeType biomeAtOrigin, double interpolationRange)`: Add description.
  - Executes `createWeights` behavior.
- `areaUnderCircleCurve(double maxX)`: Add description.
  - Executes `areaUnderCircleCurve` behavior.
- `areaUnderCircleCurve(double minX, double maxX, double circleRadius)`: Add description.
  - Executes `areaUnderCircleCurve` behavior.

## Notes
- No additional notes.
