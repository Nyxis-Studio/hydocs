# Cloud

## Overview
- Documentation for `Cloud`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `Cloud()`
  - Creates a `Cloud` instance.
- `Cloud(@Nullable String texture, @Nullable Map<Float, Float> speeds, @Nullable Map<Float, ColorAlpha> colors)`
  - Creates a `Cloud` instance.
- `Cloud(@Nonnull Cloud other)`
  - Creates a `Cloud` instance.

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
