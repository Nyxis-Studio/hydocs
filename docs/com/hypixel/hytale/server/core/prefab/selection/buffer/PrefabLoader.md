# PrefabLoader

## Overview
- Documentation for `PrefabLoader`.
- Declared as a class in `com.hypixel.hytale.server.core.prefab.selection.buffer`.

## Constructors
- `PrefabLoader(Path rootFolder)`
  - Creates a `PrefabLoader` instance.

## Methods
- `getRootFolder()`
  - Executes `getRootFolder` behavior.
- `resolvePrefabs(@Nonnull String prefabName, @Nonnull Consumer<Path> pathConsumer)`
  - Executes `resolvePrefabs` behavior.
- `resolvePrefabs(@Nonnull Path rootFolder, @Nonnull String prefabName, @Nonnull Consumer<Path> pathConsumer)`
  - Executes `resolvePrefabs` behavior.
- `resolvePrefabFolder(@Nonnull Path rootFolder, @Nonnull String prefabName, final @Nonnull Consumer<Path> pathConsumer)`
  - Executes `resolvePrefabFolder` behavior.
- `visitFile(@Nonnull Path file, BasicFileAttributes attrs)`
  - Executes `visitFile` behavior.
- `resolveRelativeJsonPath(@Nonnull String prefabName, @Nonnull Path prefabPath, @Nonnull Path rootPrefabDir)`
  - Executes `resolveRelativeJsonPath` behavior.
- `getFilepathLengthNoExtension(@Nonnull String filepath)`
  - Executes `getFilepathLengthNoExtension` behavior.

## Notes
- No additional notes.
