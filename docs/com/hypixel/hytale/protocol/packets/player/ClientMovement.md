# ClientMovement

## Overview
- Documentation for `ClientMovement`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.player`.

## Constructors
- `ClientMovement()`
  - Creates a `ClientMovement` instance.
- `ClientMovement(@Nullable MovementStates movementStates, @Nullable HalfFloatPosition relativePosition, @Nullable Position absolutePosition, @Nullable Direction bodyOrientation, @Nullable Direction lookOrientation, @Nullable TeleportAck teleportAck, @Nullable Position wishMovement, @Nullable Vector3d velocity, int mountedTo, @Nullable MovementStates riderMovementStates)`
  - Creates a `ClientMovement` instance.
- `ClientMovement(@Nonnull ClientMovement other)`
  - Creates a `ClientMovement` instance.

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
