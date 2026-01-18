# ObjectiveLocationAreaRadius

## Overview
- Documentation for `ObjectiveLocationAreaRadius`.
- Declared as a class in `com.hypixel.hytale.builtin.adventure.objectives.config.markerarea`.

## Constructors
- `ObjectiveLocationAreaRadius(int entryRadius, int exitRadius)`
  - Creates a `ObjectiveLocationAreaRadius` instance.
- `ObjectiveLocationAreaRadius()`
  - Creates a `ObjectiveLocationAreaRadius` instance.

## Methods
- `getEntryArea()`
  - Executes `getEntryArea` behavior.
- `getExitArea()`
  - Executes `getExitArea` behavior.
- `getPlayersInEntryArea(@Nonnull SpatialResource<Ref<EntityStore>, EntityStore> spatialComponent, @Nonnull List<Ref<EntityStore>> results, @Nonnull Vector3d markerPosition)`
  - Executes `getPlayersInEntryArea` behavior.
- `getPlayersInExitArea(@Nonnull SpatialResource<Ref<EntityStore>, EntityStore> spatialComponent, @Nonnull List<Ref<EntityStore>> results, @Nonnull Vector3d markerPosition)`
  - Executes `getPlayersInExitArea` behavior.
- `hasPlayerInExitArea(@Nonnull SpatialResource<Ref<EntityStore>, EntityStore> spatialComponent, @Nonnull ComponentType<EntityStore, PlayerRef> playerRefComponentType, @Nonnull Vector3d markerPosition, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `hasPlayerInExitArea` behavior.
- `isPlayerInEntryArea(@Nonnull Vector3d playerPosition, @Nonnull Vector3d markerPosition)`
  - Executes `isPlayerInEntryArea` behavior.
- `computeAreaBoxes()`
  - Executes `computeAreaBoxes` behavior.
- `getPlayersInArea(@Nonnull SpatialResource<Ref<EntityStore>, EntityStore> spatialComponent, @Nonnull List<Ref<EntityStore>> results, @Nonnull Vector3d markerPosition, int radius)`
  - Executes `getPlayersInArea` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
