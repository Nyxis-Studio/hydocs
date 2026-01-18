**Source Hash:** `f781b9a3ea745448be40d0bf3437aea381e67f7754dc1e05e475ed47c8071c14`

# AssetManager

## Overview

## Constructor Descriptions
- `AssetManager(@Nonnull EventRegistry eventRegistry, @Nonnull HytaleLogger logger)`
  - Creates a `AssetManager` instance.

## Method Descriptions
- `loadBlockMaskAssets(@Nonnull LoadedAssetsEvent<String, BlockMaskAsset, DefaultAssetMap<String, BlockMaskAsset>> event)`: Add description.
  - Executes `loadBlockMaskAssets` behavior.
- `loadDensityAssets(@Nonnull LoadedAssetsEvent<String, DensityAsset, DefaultAssetMap<String, DensityAsset>> event)`: Add description.
  - Executes `loadDensityAssets` behavior.
- `loadAssignmentsAssets(@Nonnull LoadedAssetsEvent<String, AssignmentsAsset, DefaultAssetMap<String, AssignmentsAsset>> event)`: Add description.
  - Executes `loadAssignmentsAssets` behavior.
- `loadBiomeAssets(@Nonnull LoadedAssetsEvent<String, BiomeAsset, DefaultAssetMap<String, BiomeAsset>> event)`: Add description.
  - Executes `loadBiomeAssets` behavior.
- `loadWorldStructureAssets(@Nonnull LoadedAssetsEvent<String, WorldStructureAsset, DefaultAssetMap<String, WorldStructureAsset>> event)`: Add description.
  - Executes `loadWorldStructureAssets` behavior.
- `loadSettingsAssets(@Nonnull LoadedAssetsEvent<String, SettingsAsset, DefaultAssetMap<String, SettingsAsset>> event)`: Add description.
  - Executes `loadSettingsAssets` behavior.
- `getSettingsAsset()`: Add description.
  - Executes `getSettingsAsset` behavior.
- `getWorldStructureAsset(@Nonnull String id)`: Add description.
  - Executes `getWorldStructureAsset` behavior.
- `registerReloadListener(@Nonnull Runnable l)`: Add description.
  - Executes `registerReloadListener` behavior.
- `unregisterReloadListener(@Nonnull Runnable l)`: Add description.
  - Executes `unregisterReloadListener` behavior.
- `triggerReloadListeners()`: Add description.
  - Executes `triggerReloadListeners` behavior.

## Notes
- No additional notes.
