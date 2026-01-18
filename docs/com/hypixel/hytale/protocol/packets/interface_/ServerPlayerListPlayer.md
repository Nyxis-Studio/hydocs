# ServerPlayerListPlayer

## Overview
- Documentation for `ServerPlayerListPlayer`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.interface_`.

## Constructors
- `ServerPlayerListPlayer()`
  - Creates a `ServerPlayerListPlayer` instance.
- `ServerPlayerListPlayer(@Nonnull UUID uuid, @Nullable String username, @Nullable UUID worldUuid, int ping)`
  - Creates a `ServerPlayerListPlayer` instance.
- `ServerPlayerListPlayer(@Nonnull ServerPlayerListPlayer other)`
  - Creates a `ServerPlayerListPlayer` instance.

## Methods
- `deserialize(@Nonnull ByteBuf buf, int offset)`
  - Executes `deserialize` behavior.
- `computeBytesConsumed(@Nonnull ByteBuf buf, int offset)`
  - Executes `computeBytesConsumed` behavior.
- `serialize(@Nonnull ByteBuf buf)`
  - Executes `serialize` behavior.
- `computeSize()`
  - Executes `computeSize` behavior.
- `validateStructure(@Nonnull ByteBuf buffer, int offset)`
  - Executes `validateStructure` behavior.
- `clone()`
  - Executes `clone` behavior.
- `equals(Object obj)`
  - Executes `equals` behavior.
- `hashCode()`
  - Executes `hashCode` behavior.

## Notes
- No additional notes.
