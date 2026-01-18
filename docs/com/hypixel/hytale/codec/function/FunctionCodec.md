# FunctionCodec

## Overview
- Documentation for `FunctionCodec`.
- Declared as a class in `com.hypixel.hytale.codec.function`.

## Constructors
- `FunctionCodec(Codec<T> codec, Function<T, R> decode, Function<R, T> encode)`
  - Creates a `FunctionCodec` instance.

## Methods
- `decode(BsonValue bsonValue, ExtraInfo extraInfo)`
  - Executes `decode` behavior.
- `encode(R r, ExtraInfo extraInfo)`
  - Executes `encode` behavior.
- `decodeJson(@Nonnull RawJsonReader reader, ExtraInfo extraInfo)`
  - Executes `decodeJson` behavior.
- `toSchema(@Nonnull SchemaContext context)`
  - Executes `toSchema` behavior.

## Notes
- No additional notes.
