# LocalSpawnControllerSystem

## Overview
- Documentation for `LocalSpawnControllerSystem`.
- Declared as a class in `com.hypixel.hytale.server.spawning.local`.

## Constructors
- `LocalSpawnControllerSystem(ComponentType<EntityStore, LocalSpawnController> spawnControllerComponentType, ComponentType<EntityStore, TransformComponent> transformComponentype, ComponentType<EntityStore, WeatherTracker> weatherTrackerComponentType, ComponentType<EntityStore, LocalSpawnBeacon> localSpawnBeaconComponentType, ComponentType<EntityStore, LegacySpawnBeaconEntity> spawnBeaconComponentType, ResourceType<EntityStore, LocalSpawnState> localSpawnStateResourceType, ResourceType<EntityStore, SpatialResource<Ref<EntityStore>, EntityStore>> beaconSpatialComponent)`
  - Creates a `LocalSpawnControllerSystem` instance.

## Methods
- `tick(float dt, int systemIndex, @Nonnull Store<EntityStore> store)`
  - Executes `tick` behavior.
- `spawnLightLevelMatches(@Nonnull World world, int x, int y, int z, double sunlightFactor, @Nonnull BeaconSpawnWrapper wrapper, @Nonnull Object2ByteMap<LightType> averageValues)`
  - Executes `spawnLightLevelMatches` behavior.
- `getCachedAverageLightValue(LightType lightType, @Nonnull World world, int x, int y, int z, double sunlightFactor, @Nonnull TriIntObjectDoubleToByteFunction<BlockChunk> valueCalculator, @Nonnull Object2ByteMap<LightType> averageValues)`
  - Executes `getCachedAverageLightValue` behavior.

## Notes
- No additional notes.
