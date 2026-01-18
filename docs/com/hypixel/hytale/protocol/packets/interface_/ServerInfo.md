# ServerInfo

## Overview
- Documentation for `ServerInfo`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.interface_`.

## Constructors
- `ServerInfo()`
  - Creates a `ServerInfo` instance.
- `ServerInfo(@Nullable String serverName, @Nullable String motd, int maxPlayers)`
  - Creates a `ServerInfo` instance.
- `ServerInfo(@Nonnull ServerInfo other)`
  - Creates a `ServerInfo` instance.

## Methods
- `getId()`
  - Executes `getId` behavior.
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
