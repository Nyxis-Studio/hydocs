# MetaRegistry

## Overview
- Documentation for `MetaRegistry`.
- Declared as a class in `com.hypixel.hytale.server.core.meta`.

## Constructors
- None.

## Methods
- `registerMetaObject(Function<K, T> function, boolean persistent, String keyName, @Nonnull Codec<T> codec)`
  - Executes `registerMetaObject` behavior.
- `newMetaObject(@Nonnull MetaKey<T> key, K parent)`
  - Executes `newMetaObject` behavior.
- `forEachMetaEntry(@Nonnull IMetaStore<K> store, final @Nonnull IMetaRegistry.MetaEntryConsumer consumer)`
  - Executes `forEachMetaEntry` behavior.
- `accept(int id, T value)`
  - Executes `accept` behavior.
- `getFunction()`
  - Executes `getFunction` behavior.
- `getKey()`
  - Executes `getKey` behavior.

## Notes
- No additional notes.
