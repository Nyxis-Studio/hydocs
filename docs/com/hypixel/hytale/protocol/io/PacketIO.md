# PacketIO

## Overview
- Documentation for `PacketIO`.
- Declared as a class in `com.hypixel.hytale.protocol.io`.

## Constructors
- `PacketIO()`
  - Creates a `PacketIO` instance.

## Methods
- `readHalfLE(@Nonnull ByteBuf buf, int index)`
  - Executes `readHalfLE` behavior.
- `writeHalfLE(@Nonnull ByteBuf buf, float value)`
  - Executes `writeHalfLE` behavior.
- `readBytes(@Nonnull ByteBuf buf, int offset, int length)`
  - Executes `readBytes` behavior.
- `readByteArray(@Nonnull ByteBuf buf, int offset, int length)`
  - Executes `readByteArray` behavior.
- `readShortArrayLE(@Nonnull ByteBuf buf, int offset, int length)`
  - Executes `readShortArrayLE` behavior.
- `readFloatArrayLE(@Nonnull ByteBuf buf, int offset, int length)`
  - Executes `readFloatArrayLE` behavior.
- `readFixedAsciiString(@Nonnull ByteBuf buf, int offset, int length)`
  - Executes `readFixedAsciiString` behavior.
- `readFixedString(@Nonnull ByteBuf buf, int offset, int length)`
  - Executes `readFixedString` behavior.
- `readVarString(@Nonnull ByteBuf buf, int offset)`
  - Executes `readVarString` behavior.
- `readVarAsciiString(@Nonnull ByteBuf buf, int offset)`
  - Executes `readVarAsciiString` behavior.
- `readVarString(@Nonnull ByteBuf buf, int offset, Charset charset)`
  - Executes `readVarString` behavior.
- `utf8ByteLength(@Nonnull String s)`
  - Executes `utf8ByteLength` behavior.
- `stringSize(@Nonnull String s)`
  - Executes `stringSize` behavior.
- `writeFixedBytes(@Nonnull ByteBuf buf, @Nonnull byte[] data, int length)`
  - Executes `writeFixedBytes` behavior.
- `writeFixedAsciiString(@Nonnull ByteBuf buf, @Nullable String value, int length)`
  - Executes `writeFixedAsciiString` behavior.
- `writeFixedString(@Nonnull ByteBuf buf, @Nullable String value, int length)`
  - Executes `writeFixedString` behavior.
- `writeVarString(@Nonnull ByteBuf buf, @Nonnull String value, int maxLength)`
  - Executes `writeVarString` behavior.
- `writeVarAsciiString(@Nonnull ByteBuf buf, @Nonnull String value, int maxLength)`
  - Executes `writeVarAsciiString` behavior.
- `readUUID(@Nonnull ByteBuf buf, int offset)`
  - Executes `readUUID` behavior.
- `writeUUID(@Nonnull ByteBuf buf, @Nonnull UUID value)`
  - Executes `writeUUID` behavior.
- `halfToFloat(short half)`
  - Executes `halfToFloat` behavior.
- `floatToHalf(float f)`
  - Executes `floatToHalf` behavior.
- `compressToBuffer(@Nonnull ByteBuf src, @Nonnull ByteBuf dst, int dstOffset, int maxDstSize)`
  - Executes `compressToBuffer` behavior.
- `decompressFromBuffer(@Nonnull ByteBuf src, int srcOffset, int srcLength, int maxDecompressedSize)`
  - Executes `decompressFromBuffer` behavior.
- `writeFramedPacket(@Nonnull Packet packet, @Nonnull Class<? extends Packet> packetClass, @Nonnull ByteBuf out, @Nonnull PacketStatsRecorder statsRecorder)`
  - Executes `writeFramedPacket` behavior.
- `readFramedPacket(@Nonnull ByteBuf in, int payloadLength, @Nonnull PacketStatsRecorder statsRecorder)`
  - Executes `readFramedPacket` behavior.
- `readFramedPacketWithInfo(@Nonnull ByteBuf in, int payloadLength, @Nonnull PacketRegistry.PacketInfo info, @Nonnull PacketStatsRecorder statsRecorder)`
  - Executes `readFramedPacketWithInfo` behavior.

## Notes
- No additional notes.
