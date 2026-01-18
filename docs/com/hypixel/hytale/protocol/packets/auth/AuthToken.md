# AuthToken

## Overview
- Documentation for `AuthToken`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.auth`.

## Constructors
- `AuthToken()`
  - Creates a `AuthToken` instance.
- `AuthToken(@Nullable String accessToken, @Nullable String serverAuthorizationGrant)`
  - Creates a `AuthToken` instance.
- `AuthToken(@Nonnull AuthToken other)`
  - Creates a `AuthToken` instance.

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
