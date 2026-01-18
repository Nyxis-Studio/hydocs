**Source Hash:** `916ba9eefec41b127e59a32e2a22480d8d4461abde17327ed320f28096020d01`

# PacketRegistry

## Overview

## Constructor Descriptions
- `PacketRegistry()`
  - Creates a `PacketRegistry` instance.

## Method Descriptions
- `register(int id, String name, Class<? extends Packet> type, int fixedBlockSize, int maxSize, boolean compressed, BiFunction<ByteBuf, Integer, ValidationResult> validate, BiFunction<ByteBuf, Integer, Packet> deserialize)`: Add description.
  - Executes `register` behavior.
- `getById(int id)`: Add description.
  - Executes `getById` behavior.
- `getId(Class<? extends Packet> type)`: Add description.
  - Executes `getId` behavior.
- `all()`: Add description.
  - Executes `all` behavior.
- `PacketInfo(int id, @Nonnull String name, @Nonnull Class<? extends Packet> type, int fixedBlockSize, int maxSize, boolean compressed, @Nonnull BiFunction<ByteBuf, Integer, ValidationResult> validate, @Nonnull BiFunction<ByteBuf, Integer, Packet> deserialize)`: Add description.
  - Executes `PacketInfo` behavior.

## Notes
- No additional notes.
