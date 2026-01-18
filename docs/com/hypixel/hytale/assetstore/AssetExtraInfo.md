# AssetExtraInfo

**Overview**
Carries extra asset metadata for validation and diagnostics during loading.
Stores an optional asset path and a `Data` object with tags and contained assets.

**Constructors**
- `AssetExtraInfo(Data data)`: creates a context without a path, keeping only the data.
- `AssetExtraInfo(Path assetPath, Data data)`: creates a context with path and data for the asset.

**Methods**
- `generateKey()`: builds a composite key from the internal index and next identifier.
- `getKey()`: returns the asset key stored in `Data`.
- `getAssetPath()`: returns the asset path if available.
- `getData()`: returns the associated `Data` object.
- `appendDetailsTo(StringBuilder sb)`: appends id and path to the validation details.
- `getValidationResults()`: returns asset-typed validation results.
- `toString()`: includes path and data in the diagnostic string.

**Notes**
- Extends `ExtraInfo` and creates `AssetValidationResults` by default.
- `Data` centralizes tags, contained asset references, and root container access.

---

# AssetExtraInfo.Data

**Overview**
Stores asset metadata during loading: tags, class, key, parent, and contained assets.
Supports tag inheritance from a container and expanded tags for fast queries.

**Constructors**
- `Data(Class<? extends JsonAsset<K>> assetClass, K key, K parentKey)`: creates a basic asset context.
- `Data(Data containerData, Class<? extends JsonAsset<K>> aClass, K key, K parentKey, boolean inheritContainerTags)`: links to a container and optionally inherits its tags.

**Methods**
- `getAssetClass()`: returns the asset class.
- `getKey()`: returns the asset key.
- `getParentKey()`: returns the parent key.
- `getRootContainerData()`: walks up the container chain to the root.
- `getContainerData()`: returns the immediate container, if any.
- `getContainerKey(Class<? extends JsonAsset<K>> aClass)`: finds the container key for a specific class.
- `putTags(Map<String, String[]> tags)`: registers raw tags and expanded indices.
- `getRawTags()`: returns the raw tag map (immutable).
- `getTags()`: returns the tag index map (immutable).
- `getExpandedTagIndexes()`: returns the expanded tag index set (immutable).
- `getTag(int tagIndex)`: returns tag values by index.
- `addContainedAsset(Class<T> assetClass, T asset)`: stores loaded assets of a type.
- `addContainedAsset(Class<T> assetClass, RawAsset<K> rawAsset)`: stores raw assets.
- `fetchContainedAssets(K key, Map<Class<? extends JsonAssetWithMap>, Map<K, List<Object>>> containedAssets)`: aggregates contained assets by key.
- `fetchContainedRawAssets(K key, Map<Class<? extends JsonAssetWithMap>, Map<K, List<RawAsset<Object>>>> containedAssets)`: aggregates contained raw assets by key.
- `containsAsset(Class<T> tClass, K key)`: checks whether a loaded or raw asset is contained.
- `loadContainedAssets(boolean reloading)`: triggers loading of contained assets.
- `toString()`: returns a diagnostic string with tags and references.

**Notes**
- Uses `AssetRegistry` tag indices to accelerate queries and validation.
- Exposes immutable collections for public access.
