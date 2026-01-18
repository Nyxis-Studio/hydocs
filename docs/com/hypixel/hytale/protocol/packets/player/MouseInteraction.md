# MouseInteraction

## Overview
- Documentation for `MouseInteraction`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.player`.

## Constructors
- `MouseInteraction()`
  - Creates a `MouseInteraction` instance.
- `MouseInteraction(long clientTimestamp, int activeSlot, @Nullable String itemInHandId, @Nullable Vector2f screenPoint, @Nullable MouseButtonEvent mouseButton, @Nullable MouseMotionEvent mouseMotion, @Nullable WorldInteraction worldInteraction)`
  - Creates a `MouseInteraction` instance.
- `MouseInteraction(@Nonnull MouseInteraction other)`
  - Creates a `MouseInteraction` instance.

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
