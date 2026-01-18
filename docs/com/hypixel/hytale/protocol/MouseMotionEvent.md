# MouseMotionEvent

## Overview
- Documentation for `MouseMotionEvent`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `MouseMotionEvent()`
  - Creates a `MouseMotionEvent` instance.
- `MouseMotionEvent(@Nullable MouseButtonType[] mouseButtonType, @Nullable Vector2i relativeMotion)`
  - Creates a `MouseMotionEvent` instance.
- `MouseMotionEvent(@Nonnull MouseMotionEvent other)`
  - Creates a `MouseMotionEvent` instance.

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
