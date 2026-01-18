# PrefabEditorLoadSettingsPage

## Overview
- Documentation for `PrefabEditorLoadSettingsPage`.
- Declared as a class in `com.hypixel.hytale.builtin.buildertools.prefabeditor.ui`.

## Constructors
- `PrefabEditorLoadSettingsPage(@Nonnull PlayerRef playerRef)`
  - Creates a `PrefabEditorLoadSettingsPage` instance.

## Methods
- `build(@Nonnull Ref<EntityStore> ref, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder, @Nonnull Store<EntityStore> store)`
  - Executes `build` behavior.
- `handleDataEvent(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull PageData data)`
  - Executes `handleDataEvent` behavior.
- `onLoadingProgress(@Nonnull PrefabLoadingState state)`
  - Executes `onLoadingProgress` behavior.
- `onLoadingFailed(@Nonnull Message errorMessage)`
  - Executes `onLoadingFailed` behavior.
- `onShutdownProgress(@Nonnull PrefabLoadingState state)`
  - Executes `onShutdownProgress` behavior.
- `handleAssetsNavigation(@Nonnull String fileName)`
  - Executes `handleAssetsNavigation` behavior.
- `handleRegularNavigation(@Nonnull String fileName)`
  - Executes `handleRegularNavigation` behavior.
- `getCurrentBrowserPath()`
  - Executes `getCurrentBrowserPath` behavior.
- `buildBrowserList(@Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder)`
  - Executes `buildBrowserList` behavior.
- `buildAssetsBrowserList(@Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder)`
  - Executes `buildAssetsBrowserList` behavior.
- `buildRegularBrowserList(@Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder)`
  - Executes `buildRegularBrowserList` behavior.
- `buildBrowserRootEntries()`
  - Executes `buildBrowserRootEntries` behavior.
- `findActualRootPath(@Nonnull String pathStr)`
  - Executes `findActualRootPath` behavior.
- `findAssetPackForPath(@Nonnull String pathStr)`
  - Executes `findAssetPackForPath` behavior.
- `getRootDirectoryForPath(@Nonnull String pathStr)`
  - Executes `getRootDirectoryForPath` behavior.
- `isAllowedBrowserRoot(@Nonnull String pathStr)`
  - Executes `isAllowedBrowserRoot` behavior.
- `getRootDisplayPath(@Nonnull Path root)`
  - Executes `getRootDisplayPath` behavior.
- `toCreationSettings()`
  - Executes `toCreationSettings` behavior.

## Notes
- No additional notes.
