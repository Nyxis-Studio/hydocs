# BlockMovementSettings

## Overview
- Documentation for `BlockMovementSettings`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `BlockMovementSettings()`
  - Creates a `BlockMovementSettings` instance.
- `BlockMovementSettings(boolean isClimbable, float climbUpSpeedMultiplier, float climbDownSpeedMultiplier, float climbLateralSpeedMultiplier, boolean isBouncy, float bounceVelocity, float drag, float friction, float terminalVelocityModifier, float horizontalSpeedMultiplier, float acceleration, float jumpForceMultiplier)`
  - Creates a `BlockMovementSettings` instance.
- `BlockMovementSettings(@Nonnull BlockMovementSettings other)`
  - Creates a `BlockMovementSettings` instance.

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
