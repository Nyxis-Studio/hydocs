# AssetLoadResult

**Overview**
Represents the result of an asset load, including successes and failures.
Aggregates loaded assets, key-to-path mappings, and child asset results.

**Constructors**
- `AssetLoadResult(Map<K, T> loadedAssets, Map<K, Path> loadedKeyToPathMap, Set<K> failedToLoadKeys, Set<Path> failedToLoadPaths, Map<Class<? extends JsonAssetWithMap>, AssetLoadResult> childAssetResults)`: initializes the full load result.

**Methods**
- `getLoadedAssets()`: returns the loaded assets map.
- `getLoadedKeyToPathMap()`: returns the key-to-path map.
- `getFailedToLoadKeys()`: returns keys that failed to load.
- `getFailedToLoadPaths()`: returns paths that failed to load.
- `hasFailed()`: checks for local or child result failures.

**Notes**
- `hasFailed()` walks child results recursively to surface aggregate failures.
