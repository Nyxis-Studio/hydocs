# EntityStatType

## Overview
- Documentation for `EntityStatType`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `EntityStatType()`
  - Creates a `EntityStatType` instance.
- `EntityStatType(@Nullable String id, float value, float min, float max, @Nullable EntityStatEffects minValueEffects, @Nullable EntityStatEffects maxValueEffects, @Nonnull EntityStatResetBehavior resetBehavior)`
  - Creates a `EntityStatType` instance.
- `EntityStatType(@Nonnull EntityStatType other)`
  - Creates a `EntityStatType` instance.

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
