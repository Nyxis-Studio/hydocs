# KeyedCodec

## Overview
- Documentation for `KeyedCodec`.
- Declared as a class in `com.hypixel.hytale.codec`.

## Constructors
- `KeyedCodec(@Nonnull String key, Codec<T> codec)`
  - Creates a `KeyedCodec` instance.
- `KeyedCodec(@Nonnull String key, Codec<T> codec, boolean required)`
  - Creates a `KeyedCodec` instance.
- `KeyedCodec(@Nonnull String key, Codec<T> codec, boolean required, boolean bypassCaseCheck)`
  - Creates a `KeyedCodec` instance.

## Methods
- `getKey()`
  - Executes `getKey` behavior.
- `getNow(BsonDocument document)`
  - Executes `getNow` behavior.
- `getNow(BsonDocument document, @Nonnull ExtraInfo extraInfo)`
  - Executes `getNow` behavior.
- `getOrNull(BsonDocument document)`
  - Executes `getOrNull` behavior.
- `getOrNull(BsonDocument document, @Nonnull ExtraInfo extraInfo)`
  - Executes `getOrNull` behavior.
- `get(BsonDocument document)`
  - Executes `get` behavior.
- `get(@Nullable BsonDocument document, @Nonnull ExtraInfo extraInfo)`
  - Executes `get` behavior.
- `getOrDefault(@Nullable BsonDocument document, @Nonnull ExtraInfo extraInfo, T def)`
  - Executes `getOrDefault` behavior.
- `getAndInherit(@Nullable BsonDocument document, T parent, @Nonnull ExtraInfo extraInfo)`
  - Executes `getAndInherit` behavior.
- `put(@Nonnull BsonDocument document, T t)`
  - Executes `put` behavior.
- `put(@Nonnull BsonDocument document, @Nullable T t, @Nonnull ExtraInfo extraInfo)`
  - Executes `put` behavior.
- `decode(BsonValue bsonValue, @Nonnull ExtraInfo extraInfo)`
  - Executes `decode` behavior.
- `decodeAndInherit(@Nullable BsonValue bsonValue, T parent, @Nonnull ExtraInfo extraInfo)`
  - Executes `decodeAndInherit` behavior.
- `encode(T t, ExtraInfo extraInfo)`
  - Executes `encode` behavior.
- `getChildCodec()`
  - Executes `getChildCodec` behavior.
- `isRequired()`
  - Executes `isRequired` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
