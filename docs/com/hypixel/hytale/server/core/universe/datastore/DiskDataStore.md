# DiskDataStore

## Overview
- Documentation for `DiskDataStore`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.datastore`.

## Constructors
- `DiskDataStore(@Nonnull String path, BuilderCodec<T> codec)`
  - Creates a `DiskDataStore` instance.

## Methods
- `getPath()`
  - Executes `getPath` behavior.
- `getCodec()`
  - Executes `getCodec` behavior.
- `load(String id)`
  - Executes `load` behavior.
- `save(String id, T value)`
  - Executes `save` behavior.
- `remove(String id)`
  - Executes `remove` behavior.
- `list()`
  - Executes `list` behavior.
- `loadAll()`
  - Executes `loadAll` behavior.
- `removeAll()`
  - Executes `removeAll` behavior.
- `load0(@Nonnull Path path)`
  - Executes `load0` behavior.
- `getPathFromId(@Nonnull Path path, String id)`
  - Executes `getPathFromId` behavior.
- `getBackupPathFromId(@Nonnull Path path, String id)`
  - Executes `getBackupPathFromId` behavior.
- `getIdFromPath(@Nonnull Path path)`
  - Executes `getIdFromPath` behavior.

## Notes
- No additional notes.
