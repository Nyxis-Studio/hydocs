**Source Hash:** `46f192109fbc6d1877eaf8aa0d4e5bd5b3e1f7371f0f06f2a1894a1cefd62320`

# LocalSpawnControllerSystem

## Overview

## Constructor Descriptions
- `LocalSpawnControllerSystem(ComponentType<EntityStore, LocalSpawnController> spawnControllerComponentType, ComponentType<EntityStore, TransformComponent> transformComponentype, ComponentType<EntityStore, WeatherTracker> weatherTrackerComponentType, ComponentType<EntityStore, LocalSpawnBeacon> localSpawnBeaconComponentType, ComponentType<EntityStore, LegacySpawnBeaconEntity> spawnBeaconComponentType, ResourceType<EntityStore, LocalSpawnState> localSpawnStateResourceType, ResourceType<EntityStore, SpatialResource<Ref<EntityStore>, EntityStore>> beaconSpatialComponent)`
  - Creates a `LocalSpawnControllerSystem` instance.

## Method Descriptions
- `tick(float dt, int systemIndex, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `tick` behavior.
- `spawnLightLevelMatches(@Nonnull World world, int x, int y, int z, double sunlightFactor, @Nonnull BeaconSpawnWrapper wrapper, @Nonnull Object2ByteMap<LightType> averageValues)`: Add description.
  - Executes `spawnLightLevelMatches` behavior.
- `getCachedAverageLightValue(LightType lightType, @Nonnull World world, int x, int y, int z, double sunlightFactor, @Nonnull TriIntObjectDoubleToByteFunction<BlockChunk> valueCalculator, @Nonnull Object2ByteMap<LightType> averageValues)`: Add description.
  - Executes `getCachedAverageLightValue` behavior.

## Notes
- No additional notes.
