# Animation

## Overview
- Documentation for `Animation`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `Animation()`
  - Creates a `Animation` instance.
- `Animation(@Nullable String name, float speed, float blendingDuration, boolean looping, float weight, @Nullable int[] footstepIntervals, int soundEventIndex, int passiveLoopCount)`
  - Creates a `Animation` instance.
- `Animation(@Nonnull Animation other)`
  - Creates a `Animation` instance.

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
