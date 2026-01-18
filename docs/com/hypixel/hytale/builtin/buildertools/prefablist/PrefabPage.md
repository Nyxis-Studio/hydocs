# PrefabPage

## Overview
- Documentation for `PrefabPage`.
- Declared as a class in `com.hypixel.hytale.builtin.buildertools.prefablist`.

## Constructors
- `PrefabPage(@Nonnull PlayerRef playerRef, Path defaultRoot, @Nonnull BuilderToolsPlugin.BuilderState builderState)`
  - Creates a `PrefabPage` instance.

## Methods
- `build(@Nonnull Ref<EntityStore> ref, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder, @Nonnull Store<EntityStore> store)`
  - Executes `build` behavior.
- `handleDataEvent(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull FileBrowserEventData data)`
  - Executes `handleDataEvent` behavior.
- `handleAssetsNavigation(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull String selectedPath, boolean isSearchResult)`
  - Executes `handleAssetsNavigation` behavior.
- `handleRegularNavigation(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull String selectedPath, boolean isSearchResult)`
  - Executes `handleRegularNavigation` behavior.
- `handlePrefabSelection(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull Path file, @Nonnull String displayPath)`
  - Executes `handlePrefabSelection` behavior.
- `buildCurrentPath(@Nonnull UICommandBuilder commandBuilder)`
  - Executes `buildCurrentPath` behavior.
- `getRootDisplayName(@Nonnull Path root)`
  - Executes `getRootDisplayName` behavior.
- `buildFileList(@Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder)`
  - Executes `buildFileList` behavior.
- `buildAssetsFileList(@Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder)`
  - Executes `buildAssetsFileList` behavior.
- `switchToPasteTool(@Nonnull Player playerComponent, @Nonnull PlayerRef playerRef)`
  - Executes `switchToPasteTool` behavior.

## Notes
- No additional notes.
