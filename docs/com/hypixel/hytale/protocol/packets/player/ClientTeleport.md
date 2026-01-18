# ClientTeleport

## Overview
- Documentation for `ClientTeleport`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.player`.

## Constructors
- `ClientTeleport()`
  - Creates a `ClientTeleport` instance.
- `ClientTeleport(byte teleportId, @Nullable ModelTransform modelTransform, boolean resetVelocity)`
  - Creates a `ClientTeleport` instance.
- `ClientTeleport(@Nonnull ClientTeleport other)`
  - Creates a `ClientTeleport` instance.

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
