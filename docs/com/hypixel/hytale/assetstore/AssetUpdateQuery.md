**Source Hash:** `97defb0ac1246aa2cb3b022ccea48af19f51e5c6fd75dc46ee6af3b6ee99701c`
**Last Updated:** `2026-01-18T17:16:53-03:00`

# AssetUpdateQuery

## Overview
Defines asset update parameters, including comparison and cache rebuild policy. Provides presets and flags to control which caches are rebuilt.

## Field Descriptions
- `DEFAULT`: Uses `RebuildCache.DEFAULT` for full cache rebuilds.
- `DEFAULT_NO_REBUILD`: Uses `RebuildCache.NO_REBUILD` to skip rebuilding caches.
- `disableAssetCompare`: Whether asset comparison is disabled during updates.
- `rebuildCache`: Cache rebuild configuration to apply during updates.

## Constructor Descriptions
- `AssetUpdateQuery(boolean disableAssetCompare, RebuildCache rebuildCache)`: Sets comparison behavior and rebuild policy.
- `AssetUpdateQuery(RebuildCache rebuildCache)`: Uses `AssetStore.DISABLE_ASSET_COMPARE` and the provided rebuild policy.

## Method Descriptions
- `isDisableAssetCompare()`: Returns whether asset comparison is disabled.
- `getRebuildCache()`: Returns the cache rebuild configuration.
- `toString()`: Returns a textual representation of the query.

## Usage Notes
- Use `DEFAULT` or `DEFAULT_NO_REBUILD` to apply common cache rebuild strategies.

## Examples
```java
AssetUpdateQuery query = AssetUpdateQuery.DEFAULT_NO_REBUILD;
```

---

# AssetUpdateQuery.RebuildCache

## Overview
Represents cache rebuild flags for asset categories. Provides presets for full rebuild or no rebuild, and utilities to create builder-based overrides.

## Field Descriptions
- `DEFAULT`: Full rebuild across all cache categories.
- `NO_REBUILD`: Disables rebuild across all cache categories.
- `blockTextures`: Whether block textures should be rebuilt.
- `models`: Whether models should be rebuilt.
- `modelTextures`: Whether model textures should be rebuilt.
- `mapGeometry`: Whether map geometry should be rebuilt.
- `itemIcons`: Whether item icons should be rebuilt.
- `commonAssetsRebuild`: Whether common assets should be rebuilt.

## Constructor Descriptions
- `RebuildCache(boolean blockTextures, boolean models, boolean modelTextures, boolean mapGeometry, boolean itemIcons, boolean commonAssetsRebuild)`: Defines individual rebuild flags.

## Method Descriptions
- `isBlockTextures()`: Returns whether block textures should be rebuilt.
- `isModels()`: Returns whether models should be rebuilt.
- `isModelTextures()`: Returns whether model textures should be rebuilt.
- `isMapGeometry()`: Returns whether map geometry should be rebuilt.
- `isItemIcons()`: Returns whether item icons should be rebuilt.
- `isCommonAssetsRebuild()`: Returns whether common assets should be rebuilt.
- `toBuilder()`: Creates a builder from the current flag configuration.
- `builder()`: Creates a builder with all flags defaulting to false.
- `toString()`: Returns a textual representation of the flags.

## Usage Notes
- Use `toBuilder()` when you need to tweak an existing rebuild configuration.

## Examples
```java
AssetUpdateQuery.RebuildCache cache = AssetUpdateQuery.RebuildCache.DEFAULT;
```

---

# AssetUpdateQuery.RebuildCacheBuilder

## Overview
Builder for `RebuildCache`, allowing incremental flag configuration.

## Field Descriptions
- `blockTextures`: Whether block textures should be rebuilt.
- `models`: Whether models should be rebuilt.
- `modelTextures`: Whether model textures should be rebuilt.
- `mapGeometry`: Whether map geometry should be rebuilt.
- `itemIcons`: Whether item icons should be rebuilt.
- `commonAssetsRebuild`: Whether common assets should be rebuilt.

## Constructor Descriptions
- `RebuildCacheBuilder()`: Starts with all flags set to false.
- `RebuildCacheBuilder(boolean blockTextures, boolean models, boolean modelTextures, boolean mapGeometry, boolean itemIcons, boolean commonAssetsRebuild)`: Starts with the provided flag values.

## Method Descriptions
- `setBlockTextures(boolean blockTextures)`: Sets the block textures rebuild flag.
- `setModels(boolean models)`: Sets the models rebuild flag.
- `setModelTextures(boolean modelTextures)`: Sets the model textures rebuild flag.
- `setMapGeometry(boolean mapGeometry)`: Sets the map geometry rebuild flag.
- `setItemIcons(boolean itemIcons)`: Sets the item icons rebuild flag.
- `setCommonAssetsRebuild(boolean commonAssetsRebuild)`: Sets the common assets rebuild flag.
- `build()`: Builds a `RebuildCache` instance from the configured flags.
- `toString()`: Returns a textual representation of the builder state.

## Usage Notes
- Builder setters mutate the builder in-place; call `build()` to create a new `RebuildCache`.

## Examples
```java
AssetUpdateQuery.RebuildCache cache = AssetUpdateQuery.RebuildCache.builder()
    .build();
```
