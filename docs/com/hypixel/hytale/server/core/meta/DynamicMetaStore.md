# DynamicMetaStore

## Overview
- Documentation for `DynamicMetaStore`.
- Declared as a class in `com.hypixel.hytale.server.core.meta`.

## Constructors
- `DynamicMetaStore(K parent, IMetaRegistry<K> registry)`
  - Creates a `DynamicMetaStore` instance.
- `DynamicMetaStore(K parent, IMetaRegistry<K> registry, boolean bypassEncodedCache)`
  - Creates a `DynamicMetaStore` instance.

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
- `removeSerializedMetaObject(MetaKey<T> key)`
  - Executes `removeSerializedMetaObject` behavior.
- `hasMetaObject(@Nonnull MetaKey<?> key)`
  - Executes `hasMetaObject` behavior.
- `forEachMetaObject(@Nonnull IMetaStore.MetaEntryConsumer consumer)`
  - Executes `forEachMetaObject` behavior.
- `clone(K parent)`
  - Executes `clone` behavior.
- `copyFrom(@Nonnull DynamicMetaStore<K> other)`
  - Executes `copyFrom` behavior.

## Notes
- No additional notes.
