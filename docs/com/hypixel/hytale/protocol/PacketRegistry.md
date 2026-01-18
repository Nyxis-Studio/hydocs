# PacketRegistry

## Overview
- Documentation for `PacketRegistry`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `PacketRegistry()`
  - Creates a `PacketRegistry` instance.

## Methods
- `register(int id, String name, Class<? extends Packet> type, int fixedBlockSize, int maxSize, boolean compressed, BiFunction<ByteBuf, Integer, ValidationResult> validate, BiFunction<ByteBuf, Integer, Packet> deserialize)`
  - Executes `register` behavior.
- `getById(int id)`
  - Executes `getById` behavior.
- `getId(Class<? extends Packet> type)`
  - Executes `getId` behavior.
- `all()`
  - Executes `all` behavior.
- `PacketInfo(int id, @Nonnull String name, @Nonnull Class<? extends Packet> type, int fixedBlockSize, int maxSize, boolean compressed, @Nonnull BiFunction<ByteBuf, Integer, ValidationResult> validate, @Nonnull BiFunction<ByteBuf, Integer, Packet> deserialize)`
  - Executes `PacketInfo` behavior.

## Notes
- No additional notes.
