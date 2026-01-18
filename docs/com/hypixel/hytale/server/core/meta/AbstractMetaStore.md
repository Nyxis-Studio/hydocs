**Source Hash:** `5afd9aece03353c0890e5c2890ed5dacb98c1fb7fd052107c06ec1342de2bdb2`

# AbstractMetaStore

## Overview

## Constructor Descriptions
- `AbstractMetaStore(K parent, IMetaRegistry<K> registry, boolean bypassEncodedCache)`
  - Creates a `AbstractMetaStore` instance.

## Method Descriptions
- `get0(MetaKey<T> var1)`: Add description.
  - Executes `get0` behavior.
- `getMetaStore()`: Add description.
  - Executes `getMetaStore` behavior.
- `getRegistry()`: Add description.
  - Executes `getRegistry` behavior.
- `forEachUnknownEntry(BiConsumer<String, BsonValue> consumer)`: Add description.
  - Executes `forEachUnknownEntry` behavior.
- `markMetaStoreDirty()`: Add description.
  - Executes `markMetaStoreDirty` behavior.
- `consumeMetaStoreDirty()`: Add description.
  - Executes `consumeMetaStoreDirty` behavior.
- `decodeOrNewMetaObject(MetaKey<T> key)`: Add description.
  - Executes `decodeOrNewMetaObject` behavior.
- `tryDecodeUnknownKey(@Nonnull PersistentMetaKey<T> key)`: Add description.
  - Executes `tryDecodeUnknownKey` behavior.
- `encode(final ExtraInfo extraInfo)`: Add description.
  - Executes `encode` behavior.
- `accept(MetaKey<T> key, T value)`: Add description.
  - Executes `accept` behavior.
- `decode(@Nonnull BsonDocument document, ExtraInfo extraInfo)`: Add description.
  - Executes `decode` behavior.

## Notes
- No additional notes.
