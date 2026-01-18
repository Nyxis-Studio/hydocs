**Source Hash:** `73b0dfe12c3a4b2108c9d985b6be378da27ae868555fed946a1d2cfc91d798de`
**Last Updated:** `2026-01-18T17:16:53-03:00`

# AssetLoadResult

## Overview
Represents the result of an asset load operation, including successes and failures. Aggregates loaded assets, key-to-path mappings, and nested results for child asset maps.

## Field Descriptions
- `loadedAssets`: Map of successfully loaded assets keyed by asset id.
- `loadedKeyToPathMap`: Map from asset key to source path for loaded assets.
- `failedToLoadKeys`: Set of asset keys that failed to load.
- `failedToLoadPaths`: Set of asset paths that failed to load.
- `childAssetResults`: Nested results for child asset maps keyed by asset class.

## Constructor Descriptions
- `AssetLoadResult(Map<K, T> loadedAssets, Map<K, Path> loadedKeyToPathMap, Set<K> failedToLoadKeys, Set<Path> failedToLoadPaths, Map<Class<? extends JsonAssetWithMap>, AssetLoadResult> childAssetResults)`: Stores loaded assets, failures, and child results for later inspection.

## Method Descriptions
- `getLoadedAssets()`: Returns the loaded assets map.
- `getLoadedKeyToPathMap()`: Returns the key-to-path map for loaded assets.
- `getFailedToLoadKeys()`: Returns the set of keys that failed to load.
- `getFailedToLoadPaths()`: Returns the set of paths that failed to load.
- `hasFailed()`: Returns true if this result or any child result has failures.

## Usage Notes
- `hasFailed()` checks local failures first, then recursively inspects child results.

## Examples
```java
AssetLoadResult<String, Asset> result = loader.load();
if (result.hasFailed()) {
    // handle failures
}
```
