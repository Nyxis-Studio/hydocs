# Trail

## Overview
- Documentation for `Trail`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `Trail()`
  - Creates a `Trail` instance.
- `Trail(@Nullable String id, @Nullable String texture, int lifeSpan, float roll, @Nullable Edge start, @Nullable Edge end, float lightInfluence, @Nonnull FXRenderMode renderMode, @Nullable IntersectionHighlight intersectionHighlight, boolean smooth, @Nullable Vector2i frameSize, @Nullable Range frameRange, int frameLifeSpan)`
  - Creates a `Trail` instance.
- `Trail(@Nonnull Trail other)`
  - Creates a `Trail` instance.

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
