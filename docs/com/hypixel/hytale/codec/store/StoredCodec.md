# StoredCodec

## Overview
- Documentation for `StoredCodec`.
- Declared as a class in `com.hypixel.hytale.codec.store`.

## Constructors
- `StoredCodec(CodecKey<T> key)`
  - Creates a `StoredCodec` instance.

## Methods
- `decode(BsonValue bsonValue, @Nonnull ExtraInfo extraInfo)`
  - Executes `decode` behavior.
- `encode(T t, @Nonnull ExtraInfo extraInfo)`
  - Executes `encode` behavior.
- `decodeJson(@Nonnull RawJsonReader reader, ExtraInfo extraInfo)`
  - Executes `decodeJson` behavior.
- `toSchema(@Nonnull SchemaContext context)`
  - Executes `toSchema` behavior.

## Notes
- No additional notes.
