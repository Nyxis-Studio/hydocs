# AssetSpecificFunctionality

## Overview
- Documentation for `AssetSpecificFunctionality`.
- Declared as a class in `com.hypixel.hytale.builtin.asseteditor`.

## Constructors
- None.

## Methods
- `setup()`
  - Executes `setup` behavior.
- `tryGetPlayer(@Nonnull EditorClient editorClient)`
  - Executes `tryGetPlayer` behavior.
- `onModelAssetLoaded(@Nonnull LoadedAssetsEvent<String, ModelAsset, ?> event)`
  - Executes `onModelAssetLoaded` behavior.
- `onItemAssetLoaded(@Nonnull LoadedAssetsEvent<String, Item, ?> event)`
  - Executes `onItemAssetLoaded` behavior.
- `onItemAssetCreated(@Nonnull AssetEditorAssetCreatedEvent event)`
  - Executes `onItemAssetCreated` behavior.
- `onModelAssetCreated(@Nonnull AssetEditorAssetCreatedEvent event)`
  - Executes `onModelAssetCreated` behavior.
- `onEquipItem(@Nonnull AssetEditorActivateButtonEvent event)`
  - Executes `onEquipItem` behavior.
- `onUseModel(@Nonnull AssetEditorActivateButtonEvent event)`
  - Executes `onUseModel` behavior.
- `onUpdateWeatherPreviewLockEvent(@Nonnull AssetEditorUpdateWeatherPreviewLockEvent event)`
  - Executes `onUpdateWeatherPreviewLockEvent` behavior.
- `onResetModel(@Nonnull AssetEditorActivateButtonEvent event)`
  - Executes `onResetModel` behavior.
- `equipItem(@Nonnull Path assetPath, @Nonnull EditorClient editorClient)`
  - Executes `equipItem` behavior.
- `useModel(@Nonnull Path assetPath, @Nonnull EditorClient editorClient)`
  - Executes `useModel` behavior.
- `onRequestLocalizationKeyDataSet(@Nonnull AssetEditorFetchAutoCompleteDataEvent event)`
  - Executes `onRequestLocalizationKeyDataSet` behavior.
- `onRequestBlockGroupsDataSet(@Nonnull AssetEditorFetchAutoCompleteDataEvent event)`
  - Executes `onRequestBlockGroupsDataSet` behavior.
- `onRequestItemCategoriesDataSet(@Nonnull AssetEditorRequestDataSetEvent event)`
  - Executes `onRequestItemCategoriesDataSet` behavior.
- `onClientDisconnected(@Nonnull AssetEditorClientDisconnectEvent event)`
  - Executes `onClientDisconnected` behavior.
- `resetTimeSettings(@Nonnull EditorClient editorClient, @Nonnull PlayerRef playerRef)`
  - Executes `resetTimeSettings` behavior.
- `handleWeatherOrEnvironmentUnselected(@Nonnull EditorClient editorClient, @Nonnull Path assetPath, boolean wasWeather)`
  - Executes `handleWeatherOrEnvironmentUnselected` behavior.
- `handleWeatherOrEnvironmentSelected(@Nonnull EditorClient editorClient, @Nonnull Path assetPath, boolean isWeather)`
  - Executes `handleWeatherOrEnvironmentSelected` behavior.
- `onSelectAsset(@Nonnull AssetEditorSelectAssetEvent event)`
  - Executes `onSelectAsset` behavior.
- `getModelPreviewPacketForItem(@Nonnull AssetPath assetPath, @Nullable Item item)`
  - Executes `getModelPreviewPacketForItem` behavior.
- `getDefaultItemIconProperties(@Nonnull Item item)`
  - Executes `getDefaultItemIconProperties` behavior.
- `getEventRegistry()`
  - Executes `getEventRegistry` behavior.

## Notes
- No additional notes.
