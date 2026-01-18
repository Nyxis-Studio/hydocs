# ObjectiveLocationAreaBox

## Overview
- Documentation for `ObjectiveLocationAreaBox`.
- Declared as a class in `com.hypixel.hytale.builtin.adventure.objectives.config.markerarea`.

## Constructors
- `ObjectiveLocationAreaBox(Box entryBox, Box exitBox)`
  - Creates a `ObjectiveLocationAreaBox` instance.
- `ObjectiveLocationAreaBox()`
  - Creates a `ObjectiveLocationAreaBox` instance.
- `ObjectiveLocationAreaBox(entry, exit)`
  - Creates a `ObjectiveLocationAreaBox` instance.

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
- `getRotatedArea(float yaw, float pitch)`
  - Executes `getRotatedArea` behavior.
- `computeAreaBoxes()`
  - Executes `computeAreaBoxes` behavior.
- `getPlayersInArea(@Nonnull SpatialResource<Ref<EntityStore>, EntityStore> spatialComponent, List<Ref<EntityStore>> results, @Nonnull Vector3d markerPosition, @Nonnull Box box)`
  - Executes `getPlayersInArea` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
