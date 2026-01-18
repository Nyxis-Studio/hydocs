# Connect

## Overview
- Documentation for `Connect`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.connection`.

## Constructors
- `Connect()`
  - Creates a `Connect` instance.
- `Connect(@Nonnull String protocolHash, @Nonnull ClientType clientType, @Nullable String language, @Nullable String identityToken, @Nonnull UUID uuid, @Nonnull String username, @Nullable byte[] referralData, @Nullable HostAddress referralSource)`
  - Creates a `Connect` instance.
- `Connect(@Nonnull Connect other)`
  - Creates a `Connect` instance.

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
