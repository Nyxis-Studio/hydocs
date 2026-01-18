**Source Hash:** `9888890005961dfff4b9268cf48581f5bd7e41877017028d9ed20c0c33d5f8b8`

# PrefabEditSessionManager

## Overview

## Constructor Descriptions
- `PrefabEditSessionManager(@Nonnull JavaPlugin plugin)`
  - Creates a `PrefabEditSessionManager` instance.

## Method Descriptions
- `onPlayerReady(@Nonnull PlayerReadyEvent event)`: Add description.
  - Executes `onPlayerReady` behavior.
- `givePrefabSelectorTool(@Nonnull Player playerComponent, @Nonnull PlayerRef playerRef)`: Add description.
  - Executes `givePrefabSelectorTool` behavior.
- `onPlayerAddedToWorld(@Nonnull AddPlayerToWorldEvent event)`: Add description.
  - Executes `onPlayerAddedToWorld` behavior.
- `updatePathOfLoadedPrefab(@Nonnull Path oldPath, @Nonnull Path newPath)`: Add description.
  - Executes `updatePathOfLoadedPrefab` behavior.
- `isEditingAPrefab(@Nonnull UUID playerUUID)`: Add description.
  - Executes `isEditingAPrefab` behavior.
- `getPrefabEditSession(@Nonnull UUID playerUUID)`: Add description.
  - Executes `getPrefabEditSession` behavior.
- `getActiveEditSessions()`: Add description.
  - Executes `getActiveEditSessions` behavior.
- `hasInProgressLoading(@Nonnull UUID playerUuid)`: Add description.
  - Executes `hasInProgressLoading` behavior.
- `cancelLoading(@Nonnull UUID playerUuid)`: Add description.
  - Executes `cancelLoading` behavior.
- `isLoadingCancelled(@Nonnull UUID playerUuid)`: Add description.
  - Executes `isLoadingCancelled` behavior.
- `clearLoadingState(@Nonnull UUID playerUuid)`: Add description.
  - Executes `clearLoadingState` behavior.
- `createEditSessionForNewPrefab(@Nonnull Ref<EntityStore> ref, @Nonnull Player editor, @Nonnull PrefabEditorCreationSettings settings, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `createEditSessionForNewPrefab` behavior.
- `loadPrefabAndCreateEditSession(@Nonnull Ref<EntityStore> ref, @Nonnull Player editor, @Nonnull PrefabEditorCreationSettings settings, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `loadPrefabAndCreateEditSession` behavior.
- `loadPrefabAndCreateEditSession(@Nonnull Ref<EntityStore> ref, @Nonnull Player editor, @Nonnull PrefabEditorCreationSettings settings, @Nonnull ComponentAccessor<EntityStore> componentAccessor, @Nullable Consumer<PrefabLoadingState> progressCallback)`: Add description.
  - Executes `loadPrefabAndCreateEditSession` behavior.
- `notifyProgress(@Nullable Consumer<PrefabLoadingState> progressCallback, @Nonnull PrefabLoadingState loadingState)`: Add description.
  - Executes `notifyProgress` behavior.
- `createEditSession(@Nonnull Ref<EntityStore> ref, @Nonnull PrefabEditorCreationContext context, boolean createNewPrefab, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `createEditSession` behavior.
- `createEditSession(@Nonnull Ref<EntityStore> ref, @Nonnull PrefabEditorCreationContext context, boolean createNewPrefab, @Nonnull ComponentAccessor<EntityStore> componentAccessor, @Nullable PrefabLoadingState loadingState, @Nullable Consumer<PrefabLoadingState> progressCallback)`: Add description.
  - Executes `createEditSession` behavior.
- `getWorldCreatingFuture(@Nonnull PrefabEditorCreationContext context, @Nonnull WorldConfig config)`: Add description.
  - Executes `getWorldCreatingFuture` behavior.
- `getWorldName(@Nonnull PrefabEditorCreationContext context)`: Add description.
  - Executes `getWorldName` behavior.
- `getWeatherFromEnvironment(@Nullable String environmentId)`: Add description.
  - Executes `getWeatherFromEnvironment` behavior.
- `getSavePath(@Nonnull PrefabEditorCreationContext context)`: Add description.
  - Executes `getSavePath` behavior.
- `applyWorldGenWorldConfig(@Nonnull PrefabEditorCreationContext context, int yLevelToPastePrefabsAt, @Nonnull WorldConfig worldConfig)`: Add description.
  - Executes `applyWorldGenWorldConfig` behavior.
- `getPrefabCreatingCompletableFuture(@Nonnull PrefabEditorCreationContext context, @Nonnull PrefabEditSession editSession, @Nonnull WorldConfig worldConfig)`: Add description.
  - Executes `getPrefabCreatingCompletableFuture` behavior.
- `getPrefabLoadingCompletableFuture(@Nonnull PrefabEditorCreationContext context, @Nonnull PrefabEditSession editSession, @Nonnull WorldConfig worldConfig, @Nullable PrefabLoadingState loadingState, @Nullable Consumer<PrefabLoadingState> progressCallback, @Nonnull UUID playerUuid)`: Add description.
  - Executes `getPrefabLoadingCompletableFuture` behavior.
- `calculateRowGroups(@Nonnull PrefabEditorCreationContext context, int prefabCount)`: Add description.
  - Executes `calculateRowGroups` behavior.
- `getAmountOfBlocksBelowPrefab(int prefabHeight, int desiredYLevel)`: Add description.
  - Executes `getAmountOfBlocksBelowPrefab` behavior.
- `exitEditSession(@Nonnull Ref<EntityStore> ref, @Nonnull World world, @Nonnull PlayerRef playerRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `exitEditSession` behavior.
- `cleanupCancelledSession(@Nonnull UUID playerUuid, @Nonnull String worldName, @Nullable Consumer<PrefabLoadingState> progressCallback)`: Add description.
  - Executes `cleanupCancelledSession` behavior.
- `cleanupCancelledSession(@Nonnull UUID playerUuid, @Nonnull String worldName)`: Add description.
  - Executes `cleanupCancelledSession` behavior.
- `getPrefabBuffer(@Nonnull CommandSender sender, @Nonnull Path path)`: Add description.
  - Executes `getPrefabBuffer` behavior.

## Notes
- No additional notes.
