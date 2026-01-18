# RespawnPointPage

## Overview
- Documentation for `RespawnPointPage`.
- Declared as a class in `com.hypixel.hytale.builtin.beds.respawn`.

## Constructors
- `RespawnPointPage(@Nonnull PlayerRef playerRef, InteractionType interactionType)`
  - Creates a `RespawnPointPage` instance.

## Methods
- `build(@Nonnull Ref<EntityStore> var1, @Nonnull UICommandBuilder var2, @Nonnull UIEventBuilder var3, @Nonnull Store<EntityStore> var4)`
  - Executes `build` behavior.
- `setRespawnPointForPlayer(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull Vector3i blockPosition, @Nonnull RespawnBlock respawnBlock, @Nonnull String respawnPointName, PlayerRespawnPointData ... respawnPointsToRemove)`
  - Executes `setRespawnPointForPlayer` behavior.
- `handleRespawnPointsToRemove(@Nonnull PlayerRespawnPointData[] respawnPoints, @Nullable PlayerRespawnPointData[] respawnPointsToRemove, @Nonnull World world)`
  - Executes `handleRespawnPointsToRemove` behavior.
- `displayError(@Nonnull Message errorMessage)`
  - Executes `displayError` behavior.
- `getAction()`
  - Executes `getAction` behavior.
- `getIndex()`
  - Executes `getIndex` behavior.
- `getRespawnPointName()`
  - Executes `getRespawnPointName` behavior.

## Notes
- No additional notes.
