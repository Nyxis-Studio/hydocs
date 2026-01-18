# MovementStates

## Overview
- Documentation for `MovementStates`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `MovementStates()`
  - Creates a `MovementStates` instance.
- `MovementStates(boolean idle, boolean horizontalIdle, boolean jumping, boolean flying, boolean walking, boolean running, boolean sprinting, boolean crouching, boolean forcedCrouching, boolean falling, boolean climbing, boolean inFluid, boolean swimming, boolean swimJumping, boolean onGround, boolean mantling, boolean sliding, boolean mounting, boolean rolling, boolean sitting, boolean gliding, boolean sleeping)`
  - Creates a `MovementStates` instance.
- `MovementStates(@Nonnull MovementStates other)`
  - Creates a `MovementStates` instance.

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
