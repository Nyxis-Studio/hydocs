# UUIDBinaryCodec

## Overview
- Documentation for `UUIDBinaryCodec`.
- Declared as a class in `com.hypixel.hytale.codec.codecs`.

## Constructors
- None.

## Methods
- `decode(@Nonnull BsonValue bsonValue, ExtraInfo extraInfo)`
  - Executes `decode` behavior.
- `encode(@Nonnull UUID uuid, ExtraInfo extraInfo)`
  - Executes `encode` behavior.
- `decodeJson(@Nonnull RawJsonReader reader, ExtraInfo extraInfo)`
  - Executes `decodeJson` behavior.
- `writeLongToArrayBigEndian(@Nonnull byte[] bytes, int offset, long x)`
  - Executes `writeLongToArrayBigEndian` behavior.
- `readLongFromArrayBigEndian(@Nonnull byte[] bytes, int offset)`
  - Executes `readLongFromArrayBigEndian` behavior.
- `uuidFromBytes(@Nonnull byte[] bytes)`
  - Executes `uuidFromBytes` behavior.
- `uuidFromHex(String src)`
  - Executes `uuidFromHex` behavior.
- `toSchema(@Nonnull SchemaContext context)`
  - Executes `toSchema` behavior.

## Notes
- No additional notes.
