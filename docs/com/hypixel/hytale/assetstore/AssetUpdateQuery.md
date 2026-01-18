# AssetUpdateQuery

**Overview**
Defines asset update parameters, including comparison and cache rebuild policy.
Provides presets and flags to control which caches are rebuilt.

**Constructors**
- `AssetUpdateQuery(boolean disableAssetCompare, RebuildCache rebuildCache)`: sets comparison behavior and rebuild policy.
- `AssetUpdateQuery(RebuildCache rebuildCache)`: uses `AssetStore.DISABLE_ASSET_COMPARE` and sets rebuild.

**Methods**
- `isDisableAssetCompare()`: returns whether asset comparison is disabled.
- `getRebuildCache()`: returns the cache rebuild configuration.
- `toString()`: returns a textual representation of the query.

**Notes**
- Presets: `DEFAULT` and `DEFAULT_NO_REBUILD`.

---

# AssetUpdateQuery.RebuildCache

**Overview**
Represents cache rebuild flags for asset categories.
Supports presets and custom configurations.

**Constructors**
- `RebuildCache(boolean blockTextures, boolean models, boolean modelTextures, boolean mapGeometry, boolean itemIcons, boolean commonAssetsRebuild)`: defines individual flags.

**Methods**
- `isBlockTextures()`: indicates rebuild of block textures.
- `isModels()`: indicates rebuild of models.
- `isModelTextures()`: indicates rebuild of model textures.
- `isMapGeometry()`: indicates rebuild of map geometry.
- `isItemIcons()`: indicates rebuild of item icons.
- `isCommonAssetsRebuild()`: indicates rebuild of common assets.
- `toBuilder()`: creates a builder from the current state.
- `builder()`: creates an empty builder.
- `toString()`: returns a textual representation of the flags.

---

# AssetUpdateQuery.RebuildCacheBuilder

**Overview**
Builder for `RebuildCache`, allowing incremental flag configuration.

**Constructors**
- `RebuildCacheBuilder()`: starts with default false flags.
- `RebuildCacheBuilder(boolean blockTextures, boolean models, boolean modelTextures, boolean mapGeometry, boolean itemIcons, boolean commonAssetsRebuild)`: starts with provided values.

**Methods**
- `setBlockTextures(boolean blockTextures)`: sets the block texture flag.
- `setModels(boolean models)`: sets the model flag.
- `setModelTextures(boolean modelTextures)`: sets the model texture flag.
- `setMapGeometry(boolean mapGeometry)`: sets the map geometry flag.
- `setItemIcons(boolean itemIcons)`: sets the item icon flag.
- `setCommonAssetsRebuild(boolean commonAssetsRebuild)`: sets the common assets rebuild flag.
- `build()`: creates a `RebuildCache` instance.
- `toString()`: returns a textual representation of the builder.
