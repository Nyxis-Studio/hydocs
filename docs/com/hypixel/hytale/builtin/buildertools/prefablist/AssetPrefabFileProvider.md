# AssetPrefabFileProvider

## Overview
- Documentation for `AssetPrefabFileProvider`.
- Declared as a class in `com.hypixel.hytale.builtin.buildertools.prefablist`.

## Constructors
- None.

## Methods
- `searchInDirectory(final @Nonnull Path root, final @Nonnull String packKey, final @Nonnull String basePath, final @Nonnull String searchQuery, final @Nonnull List<SearchResult> results)`
  - Executes `searchInDirectory` behavior.
- `visitFile(@Nonnull Path file, @Nonnull BasicFileAttributes attrs)`
  - Executes `visitFile` behavior.
- `getPackKey(@Nonnull PrefabStore.AssetPackPrefabPath packPath)`
  - Executes `getPackKey` behavior.
- `removeExtension(@Nonnull String fileName)`
  - Executes `removeExtension` behavior.
- `resolveVirtualPath(@Nonnull String virtualPath)`
  - Executes `resolveVirtualPath` behavior.
- `getPackDisplayName(@Nonnull String packKey)`
  - Executes `getPackDisplayName` behavior.
- `SearchResult(@Nonnull String relativePath, @Nonnull String displayName, int score)`
  - Executes `SearchResult` behavior.

## Notes
- No additional notes.
