# MouseButtonEvent

## Overview
- Documentation for `MouseButtonEvent`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `MouseButtonEvent()`
  - Creates a `MouseButtonEvent` instance.
- `MouseButtonEvent(@Nonnull MouseButtonType mouseButtonType, @Nonnull MouseButtonState state, byte clicks)`
  - Creates a `MouseButtonEvent` instance.
- `MouseButtonEvent(@Nonnull MouseButtonEvent other)`
  - Creates a `MouseButtonEvent` instance.

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
