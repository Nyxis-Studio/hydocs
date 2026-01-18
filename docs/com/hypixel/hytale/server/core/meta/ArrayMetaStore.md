# ArrayMetaStore

## Overview
- Documentation for `ArrayMetaStore`.
- Declared as a class in `com.hypixel.hytale.server.core.meta`.

## Constructors
- `ArrayMetaStore(K parent, IMetaRegistry<K> registry)`
  - Creates a `ArrayMetaStore` instance.
- `ArrayMetaStore(K parent, IMetaRegistry<K> registry, boolean bypassEncodedCache)`
  - Creates a `ArrayMetaStore` instance.

## Methods
- `get0(@Nonnull MetaKey<T> key)`
  - Executes `get0` behavior.
- `getMetaObject(@Nonnull MetaKey<T> key)`
  - Executes `getMetaObject` behavior.
- `getIfPresentMetaObject(@Nonnull MetaKey<T> key)`
  - Executes `getIfPresentMetaObject` behavior.
- `putMetaObject(@Nonnull MetaKey<T> key, T obj)`
  - Executes `putMetaObject` behavior.
- `removeMetaObject(@Nonnull MetaKey<T> key)`
  - Executes `removeMetaObject` behavior.
- `removeSerializedMetaObject(@Nonnull MetaKey<T> key)`
  - Executes `removeSerializedMetaObject` behavior.
- `hasMetaObject(@Nonnull MetaKey<?> key)`
  - Executes `hasMetaObject` behavior.
- `forEachMetaObject(@Nonnull IMetaStore.MetaEntryConsumer consumer)`
  - Executes `forEachMetaObject` behavior.
- `resizeArray(T obj, int id)`
  - Executes `resizeArray` behavior.

## Notes
- No additional notes.
