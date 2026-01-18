# AbstractMetaStore

## Overview
- Documentation for `AbstractMetaStore`.
- Declared as a class in `com.hypixel.hytale.server.core.meta`.

## Constructors
- `AbstractMetaStore(K parent, IMetaRegistry<K> registry, boolean bypassEncodedCache)`
  - Creates a `AbstractMetaStore` instance.

## Methods
- `get0(MetaKey<T> var1)`
  - Executes `get0` behavior.
- `getMetaStore()`
  - Executes `getMetaStore` behavior.
- `getRegistry()`
  - Executes `getRegistry` behavior.
- `forEachUnknownEntry(BiConsumer<String, BsonValue> consumer)`
  - Executes `forEachUnknownEntry` behavior.
- `markMetaStoreDirty()`
  - Executes `markMetaStoreDirty` behavior.
- `consumeMetaStoreDirty()`
  - Executes `consumeMetaStoreDirty` behavior.
- `decodeOrNewMetaObject(MetaKey<T> key)`
  - Executes `decodeOrNewMetaObject` behavior.
- `tryDecodeUnknownKey(@Nonnull PersistentMetaKey<T> key)`
  - Executes `tryDecodeUnknownKey` behavior.
- `encode(final ExtraInfo extraInfo)`
  - Executes `encode` behavior.
- `accept(MetaKey<T> key, T value)`
  - Executes `accept` behavior.
- `decode(@Nonnull BsonDocument document, ExtraInfo extraInfo)`
  - Executes `decode` behavior.

## Notes
- No additional notes.
