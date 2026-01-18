# NTerrainStage

## Overview
- Documentation for `NTerrainStage`.
- Declared as a class in `com.hypixel.hytale.builtin.hytalegenerator.newsystem.stages`.

## Constructors
- `NTerrainStage(@Nonnull String stageName, @Nonnull NParametrizedBufferType biomeInputBufferType, @Nonnull NParametrizedBufferType biomeDistanceInputBufferType, @Nonnull NParametrizedBufferType materialOutputBufferType, int maxInterpolationRadius_voxelGrid, @Nonnull MaterialCache materialCache, @Nonnull WorkerIndexer workerIndexer)`
  - Creates a `NTerrainStage` instance.

## Methods
- `run(@Nonnull NStage.Context context)`
  - Executes `run` behavior.
- `getInputTypesAndBounds_bufferGrid()`
  - Executes `getInputTypesAndBounds_bufferGrid` behavior.
- `getOutputTypes()`
  - Executes `getOutputTypes` behavior.
- `getName()`
  - Executes `getName` behavior.
- `generateDensity(@Nonnull FloatContainer3d densityBuffer, @Nonnull NPixelBufferView<BiomeType> biomeSpace, @Nonnull NPixelBufferView<NBiomeDistanceStage.BiomeDistanceEntries> distanceSpace, @Nonnull WorkerIndexer.Id workerId)`
  - Executes `generateDensity` behavior.
- `getOrGenerateDensity(@Nonnull Vector3i position_voxelGrid, @Nonnull FloatContainer3d densityBuffer, @Nonnull NPixelBufferView<BiomeType> biomeSpace, @Nonnull NPixelBufferView<NBiomeDistanceStage.BiomeDistanceEntries> distanceSpace, @Nonnull WorkerIndexer.Id workerId)`
  - Executes `getOrGenerateDensity` behavior.
- `generateDensity(@Nonnull Vector3i position_voxelGrid, @Nonnull NPixelBufferView<BiomeType> biomeSpace, @Nonnull NPixelBufferView<NBiomeDistanceStage.BiomeDistanceEntries> distanceSpace, @Nonnull WorkerIndexer.Id workerId)`
  - Executes `generateDensity` behavior.
- `generateMaterials(@Nonnull NPixelBufferView<BiomeType> biomeSpace, @Nonnull NPixelBufferView<NBiomeDistanceStage.BiomeDistanceEntries> distanceSpace, @Nonnull FloatContainer3d densityBuffer, @Nonnull NVoxelBufferView<Material> materialSpace, @Nonnull WorkerIndexer.Id workerId)`
  - Executes `generateMaterials` behavior.
- `createWeights(@Nonnull NBiomeDistanceStage.BiomeDistanceEntries distances, @Nonnull BiomeType biomeAtOrigin, double interpolationRange)`
  - Executes `createWeights` behavior.
- `areaUnderCircleCurve(double maxX)`
  - Executes `areaUnderCircleCurve` behavior.
- `areaUnderCircleCurve(double minX, double maxX, double circleRadius)`
  - Executes `areaUnderCircleCurve` behavior.

## Notes
- No additional notes.
