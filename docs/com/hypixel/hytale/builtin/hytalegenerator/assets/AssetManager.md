# AssetManager

## Overview
- Documentation for `AssetManager`.
- Declared as a class in `com.hypixel.hytale.builtin.hytalegenerator.assets`.

## Constructors
- `AssetManager(@Nonnull EventRegistry eventRegistry, @Nonnull HytaleLogger logger)`
  - Creates a `AssetManager` instance.

## Methods
- `loadBlockMaskAssets(@Nonnull LoadedAssetsEvent<String, BlockMaskAsset, DefaultAssetMap<String, BlockMaskAsset>> event)`
  - Executes `loadBlockMaskAssets` behavior.
- `loadDensityAssets(@Nonnull LoadedAssetsEvent<String, DensityAsset, DefaultAssetMap<String, DensityAsset>> event)`
  - Executes `loadDensityAssets` behavior.
- `loadAssignmentsAssets(@Nonnull LoadedAssetsEvent<String, AssignmentsAsset, DefaultAssetMap<String, AssignmentsAsset>> event)`
  - Executes `loadAssignmentsAssets` behavior.
- `loadBiomeAssets(@Nonnull LoadedAssetsEvent<String, BiomeAsset, DefaultAssetMap<String, BiomeAsset>> event)`
  - Executes `loadBiomeAssets` behavior.
- `loadWorldStructureAssets(@Nonnull LoadedAssetsEvent<String, WorldStructureAsset, DefaultAssetMap<String, WorldStructureAsset>> event)`
  - Executes `loadWorldStructureAssets` behavior.
- `loadSettingsAssets(@Nonnull LoadedAssetsEvent<String, SettingsAsset, DefaultAssetMap<String, SettingsAsset>> event)`
  - Executes `loadSettingsAssets` behavior.
- `getSettingsAsset()`
  - Executes `getSettingsAsset` behavior.
- `getWorldStructureAsset(@Nonnull String id)`
  - Executes `getWorldStructureAsset` behavior.
- `registerReloadListener(@Nonnull Runnable l)`
  - Executes `registerReloadListener` behavior.
- `unregisterReloadListener(@Nonnull Runnable l)`
  - Executes `unregisterReloadListener` behavior.
- `triggerReloadListeners()`
  - Executes `triggerReloadListeners` behavior.

## Notes
- No additional notes.
