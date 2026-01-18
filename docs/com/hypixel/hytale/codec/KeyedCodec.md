**Source Hash:** `5b3e0a8520e1e86136c927ef961f3d671d95565fa3c2faffaa2f6b865e9e468b`

# KeyedCodec

## Overview

## Constructor Descriptions
- `KeyedCodec(@Nonnull String key, Codec<T> codec)`
  - Creates a `KeyedCodec` instance.
- `KeyedCodec(@Nonnull String key, Codec<T> codec, boolean required)`
  - Creates a `KeyedCodec` instance.
- `KeyedCodec(@Nonnull String key, Codec<T> codec, boolean required, boolean bypassCaseCheck)`
  - Creates a `KeyedCodec` instance.

## Method Descriptions
- `getKey()`: Add description.
  - Executes `getKey` behavior.
- `getNow(BsonDocument document)`: Add description.
  - Executes `getNow` behavior.
- `getNow(BsonDocument document, @Nonnull ExtraInfo extraInfo)`: Add description.
  - Executes `getNow` behavior.
- `getOrNull(BsonDocument document)`: Add description.
  - Executes `getOrNull` behavior.
- `getOrNull(BsonDocument document, @Nonnull ExtraInfo extraInfo)`: Add description.
  - Executes `getOrNull` behavior.
- `get(BsonDocument document)`: Add description.
  - Executes `get` behavior.
- `get(@Nullable BsonDocument document, @Nonnull ExtraInfo extraInfo)`: Add description.
  - Executes `get` behavior.
- `getOrDefault(@Nullable BsonDocument document, @Nonnull ExtraInfo extraInfo, T def)`: Add description.
  - Executes `getOrDefault` behavior.
- `getAndInherit(@Nullable BsonDocument document, T parent, @Nonnull ExtraInfo extraInfo)`: Add description.
  - Executes `getAndInherit` behavior.
- `put(@Nonnull BsonDocument document, T t)`: Add description.
  - Executes `put` behavior.
- `put(@Nonnull BsonDocument document, @Nullable T t, @Nonnull ExtraInfo extraInfo)`: Add description.
  - Executes `put` behavior.
- `decode(BsonValue bsonValue, @Nonnull ExtraInfo extraInfo)`: Add description.
  - Executes `decode` behavior.
- `decodeAndInherit(@Nullable BsonValue bsonValue, T parent, @Nonnull ExtraInfo extraInfo)`: Add description.
  - Executes `decodeAndInherit` behavior.
- `encode(T t, ExtraInfo extraInfo)`: Add description.
  - Executes `encode` behavior.
- `getChildCodec()`: Add description.
  - Executes `getChildCodec` behavior.
- `isRequired()`: Add description.
  - Executes `isRequired` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.

## Notes
- No additional notes.
