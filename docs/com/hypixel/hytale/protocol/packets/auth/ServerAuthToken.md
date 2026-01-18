# ServerAuthToken

## Overview
- Documentation for `ServerAuthToken`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.auth`.

## Constructors
- `ServerAuthToken()`
  - Creates a `ServerAuthToken` instance.
- `ServerAuthToken(@Nullable String serverAccessToken, @Nullable byte[] passwordChallenge)`
  - Creates a `ServerAuthToken` instance.
- `ServerAuthToken(@Nonnull ServerAuthToken other)`
  - Creates a `ServerAuthToken` instance.

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
