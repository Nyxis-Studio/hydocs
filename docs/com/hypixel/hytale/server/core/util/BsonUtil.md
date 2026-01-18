# BsonUtil

## Overview
- Documentation for `BsonUtil`.
- Declared as a class in `com.hypixel.hytale.server.core.util`.

## Constructors
- None.

## Methods
- `writeToBytes(@Nullable BsonDocument document)`
  - Executes `writeToBytes` behavior.
- `readFromBytes(@Nullable byte[] buf)`
  - Executes `readFromBytes` behavior.
- `readFromBuffer(@Nullable ByteBuffer buf)`
  - Executes `readFromBuffer` behavior.
- `readFromBinaryStream(@Nonnull ByteBuf buf)`
  - Executes `readFromBinaryStream` behavior.
- `writeToBinaryStream(@Nonnull ByteBuf buf, BsonDocument doc)`
  - Executes `writeToBinaryStream` behavior.
- `writeDocumentBytes(@Nonnull Path file, BsonDocument document)`
  - Executes `writeDocumentBytes` behavior.
- `writeDocument(@Nonnull Path file, BsonDocument document)`
  - Executes `writeDocument` behavior.
- `writeDocument(@Nonnull Path file, BsonDocument document, boolean backup)`
  - Executes `writeDocument` behavior.
- `readDocument(@Nonnull Path file)`
  - Executes `readDocument` behavior.
- `readDocument(@Nonnull Path file, boolean backup)`
  - Executes `readDocument` behavior.
- `readDocumentNow(@Nonnull Path file)`
  - Executes `readDocumentNow` behavior.
- `readDocumentBak(@Nonnull Path fileOrig)`
  - Executes `readDocumentBak` behavior.
- `translateJsonToBson(@Nonnull JsonElement element)`
  - Executes `translateJsonToBson` behavior.
- `translateBsonToJson(BsonDocument value)`
  - Executes `translateBsonToJson` behavior.
- `toJson(BsonDocument document)`
  - Executes `toJson` behavior.
- `writeSync(@Nonnull Path path, @Nonnull Codec<T> codec, T value, @Nonnull HytaleLogger logger)`
  - Executes `writeSync` behavior.

## Notes
- No additional notes.
