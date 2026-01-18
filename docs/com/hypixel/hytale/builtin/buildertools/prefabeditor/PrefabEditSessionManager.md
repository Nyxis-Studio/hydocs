# PrefabEditSessionManager

## Overview
- Documentation for `PrefabEditSessionManager`.
- Declared as a class in `com.hypixel.hytale.builtin.buildertools.prefabeditor`.

## Constructors
- `PrefabEditSessionManager(@Nonnull JavaPlugin plugin)`
  - Creates a `PrefabEditSessionManager` instance.

## Methods
- `onPlayerReady(@Nonnull PlayerReadyEvent event)`
  - Executes `onPlayerReady` behavior.
- `givePrefabSelectorTool(@Nonnull Player playerComponent, @Nonnull PlayerRef playerRef)`
  - Executes `givePrefabSelectorTool` behavior.
- `onPlayerAddedToWorld(@Nonnull AddPlayerToWorldEvent event)`
  - Executes `onPlayerAddedToWorld` behavior.
- `updatePathOfLoadedPrefab(@Nonnull Path oldPath, @Nonnull Path newPath)`
  - Executes `updatePathOfLoadedPrefab` behavior.
- `isEditingAPrefab(@Nonnull UUID playerUUID)`
  - Executes `isEditingAPrefab` behavior.
- `getPrefabEditSession(@Nonnull UUID playerUUID)`
  - Executes `getPrefabEditSession` behavior.
- `getActiveEditSessions()`
  - Executes `getActiveEditSessions` behavior.
- `hasInProgressLoading(@Nonnull UUID playerUuid)`
  - Executes `hasInProgressLoading` behavior.
- `cancelLoading(@Nonnull UUID playerUuid)`
  - Executes `cancelLoading` behavior.
- `isLoadingCancelled(@Nonnull UUID playerUuid)`
  - Executes `isLoadingCancelled` behavior.
- `clearLoadingState(@Nonnull UUID playerUuid)`
  - Executes `clearLoadingState` behavior.
- `createEditSessionForNewPrefab(@Nonnull Ref<EntityStore> ref, @Nonnull Player editor, @Nonnull PrefabEditorCreationSettings settings, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `createEditSessionForNewPrefab` behavior.
- `loadPrefabAndCreateEditSession(@Nonnull Ref<EntityStore> ref, @Nonnull Player editor, @Nonnull PrefabEditorCreationSettings settings, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `loadPrefabAndCreateEditSession` behavior.
- `loadPrefabAndCreateEditSession(@Nonnull Ref<EntityStore> ref, @Nonnull Player editor, @Nonnull PrefabEditorCreationSettings settings, @Nonnull ComponentAccessor<EntityStore> componentAccessor, @Nullable Consumer<PrefabLoadingState> progressCallback)`
  - Executes `loadPrefabAndCreateEditSession` behavior.
- `notifyProgress(@Nullable Consumer<PrefabLoadingState> progressCallback, @Nonnull PrefabLoadingState loadingState)`
  - Executes `notifyProgress` behavior.
- `createEditSession(@Nonnull Ref<EntityStore> ref, @Nonnull PrefabEditorCreationContext context, boolean createNewPrefab, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `createEditSession` behavior.
- `createEditSession(@Nonnull Ref<EntityStore> ref, @Nonnull PrefabEditorCreationContext context, boolean createNewPrefab, @Nonnull ComponentAccessor<EntityStore> componentAccessor, @Nullable PrefabLoadingState loadingState, @Nullable Consumer<PrefabLoadingState> progressCallback)`
  - Executes `createEditSession` behavior.
- `getWorldCreatingFuture(@Nonnull PrefabEditorCreationContext context, @Nonnull WorldConfig config)`
  - Executes `getWorldCreatingFuture` behavior.
- `getWorldName(@Nonnull PrefabEditorCreationContext context)`
  - Executes `getWorldName` behavior.
- `getWeatherFromEnvironment(@Nullable String environmentId)`
  - Executes `getWeatherFromEnvironment` behavior.
- `getSavePath(@Nonnull PrefabEditorCreationContext context)`
  - Executes `getSavePath` behavior.
- `applyWorldGenWorldConfig(@Nonnull PrefabEditorCreationContext context, int yLevelToPastePrefabsAt, @Nonnull WorldConfig worldConfig)`
  - Executes `applyWorldGenWorldConfig` behavior.
- `getPrefabCreatingCompletableFuture(@Nonnull PrefabEditorCreationContext context, @Nonnull PrefabEditSession editSession, @Nonnull WorldConfig worldConfig)`
  - Executes `getPrefabCreatingCompletableFuture` behavior.
- `getPrefabLoadingCompletableFuture(@Nonnull PrefabEditorCreationContext context, @Nonnull PrefabEditSession editSession, @Nonnull WorldConfig worldConfig, @Nullable PrefabLoadingState loadingState, @Nullable Consumer<PrefabLoadingState> progressCallback, @Nonnull UUID playerUuid)`
  - Executes `getPrefabLoadingCompletableFuture` behavior.
- `calculateRowGroups(@Nonnull PrefabEditorCreationContext context, int prefabCount)`
  - Executes `calculateRowGroups` behavior.
- `getAmountOfBlocksBelowPrefab(int prefabHeight, int desiredYLevel)`
  - Executes `getAmountOfBlocksBelowPrefab` behavior.
- `exitEditSession(@Nonnull Ref<EntityStore> ref, @Nonnull World world, @Nonnull PlayerRef playerRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `exitEditSession` behavior.
- `cleanupCancelledSession(@Nonnull UUID playerUuid, @Nonnull String worldName, @Nullable Consumer<PrefabLoadingState> progressCallback)`
  - Executes `cleanupCancelledSession` behavior.
- `cleanupCancelledSession(@Nonnull UUID playerUuid, @Nonnull String worldName)`
  - Executes `cleanupCancelledSession` behavior.
- `getPrefabBuffer(@Nonnull CommandSender sender, @Nonnull Path path)`
  - Executes `getPrefabBuffer` behavior.

## Notes
- No additional notes.
