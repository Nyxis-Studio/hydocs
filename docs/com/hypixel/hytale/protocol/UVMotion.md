# UVMotion

## Overview
- Documentation for `UVMotion`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `UVMotion()`
  - Creates a `UVMotion` instance.
- `UVMotion(@Nullable String texture, boolean addRandomUVOffset, float speedX, float speedY, float scale, float strength, @Nonnull UVMotionCurveType strengthCurveType)`
  - Creates a `UVMotion` instance.
- `UVMotion(@Nonnull UVMotion other)`
  - Creates a `UVMotion` instance.

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
