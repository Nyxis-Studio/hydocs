**Source Hash:** `25f8c66550d168cb2dc27618750eea1b2c69ead57768770a750a6afb962e7e30`

# PacketIO

## Overview

## Constructor Descriptions
- `PacketIO()`
  - Creates a `PacketIO` instance.

## Method Descriptions
- `readHalfLE(@Nonnull ByteBuf buf, int index)`: Add description.
  - Executes `readHalfLE` behavior.
- `writeHalfLE(@Nonnull ByteBuf buf, float value)`: Add description.
  - Executes `writeHalfLE` behavior.
- `readBytes(@Nonnull ByteBuf buf, int offset, int length)`: Add description.
  - Executes `readBytes` behavior.
- `readByteArray(@Nonnull ByteBuf buf, int offset, int length)`: Add description.
  - Executes `readByteArray` behavior.
- `readShortArrayLE(@Nonnull ByteBuf buf, int offset, int length)`: Add description.
  - Executes `readShortArrayLE` behavior.
- `readFloatArrayLE(@Nonnull ByteBuf buf, int offset, int length)`: Add description.
  - Executes `readFloatArrayLE` behavior.
- `readFixedAsciiString(@Nonnull ByteBuf buf, int offset, int length)`: Add description.
  - Executes `readFixedAsciiString` behavior.
- `readFixedString(@Nonnull ByteBuf buf, int offset, int length)`: Add description.
  - Executes `readFixedString` behavior.
- `readVarString(@Nonnull ByteBuf buf, int offset)`: Add description.
  - Executes `readVarString` behavior.
- `readVarAsciiString(@Nonnull ByteBuf buf, int offset)`: Add description.
  - Executes `readVarAsciiString` behavior.
- `readVarString(@Nonnull ByteBuf buf, int offset, Charset charset)`: Add description.
  - Executes `readVarString` behavior.
- `utf8ByteLength(@Nonnull String s)`: Add description.
  - Executes `utf8ByteLength` behavior.
- `stringSize(@Nonnull String s)`: Add description.
  - Executes `stringSize` behavior.
- `writeFixedBytes(@Nonnull ByteBuf buf, @Nonnull byte[] data, int length)`: Add description.
  - Executes `writeFixedBytes` behavior.
- `writeFixedAsciiString(@Nonnull ByteBuf buf, @Nullable String value, int length)`: Add description.
  - Executes `writeFixedAsciiString` behavior.
- `writeFixedString(@Nonnull ByteBuf buf, @Nullable String value, int length)`: Add description.
  - Executes `writeFixedString` behavior.
- `writeVarString(@Nonnull ByteBuf buf, @Nonnull String value, int maxLength)`: Add description.
  - Executes `writeVarString` behavior.
- `writeVarAsciiString(@Nonnull ByteBuf buf, @Nonnull String value, int maxLength)`: Add description.
  - Executes `writeVarAsciiString` behavior.
- `readUUID(@Nonnull ByteBuf buf, int offset)`: Add description.
  - Executes `readUUID` behavior.
- `writeUUID(@Nonnull ByteBuf buf, @Nonnull UUID value)`: Add description.
  - Executes `writeUUID` behavior.
- `halfToFloat(short half)`: Add description.
  - Executes `halfToFloat` behavior.
- `floatToHalf(float f)`: Add description.
  - Executes `floatToHalf` behavior.
- `compressToBuffer(@Nonnull ByteBuf src, @Nonnull ByteBuf dst, int dstOffset, int maxDstSize)`: Add description.
  - Executes `compressToBuffer` behavior.
- `decompressFromBuffer(@Nonnull ByteBuf src, int srcOffset, int srcLength, int maxDecompressedSize)`: Add description.
  - Executes `decompressFromBuffer` behavior.
- `writeFramedPacket(@Nonnull Packet packet, @Nonnull Class<? extends Packet> packetClass, @Nonnull ByteBuf out, @Nonnull PacketStatsRecorder statsRecorder)`: Add description.
  - Executes `writeFramedPacket` behavior.
- `readFramedPacket(@Nonnull ByteBuf in, int payloadLength, @Nonnull PacketStatsRecorder statsRecorder)`: Add description.
  - Executes `readFramedPacket` behavior.
- `readFramedPacketWithInfo(@Nonnull ByteBuf in, int payloadLength, @Nonnull PacketRegistry.PacketInfo info, @Nonnull PacketStatsRecorder statsRecorder)`: Add description.
  - Executes `readFramedPacketWithInfo` behavior.

## Notes
- No additional notes.
