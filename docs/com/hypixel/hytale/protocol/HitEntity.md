# HitEntity

## Overview
- Documentation for `HitEntity`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `HitEntity()`
  - Creates a `HitEntity` instance.
- `HitEntity(int next, @Nullable EntityMatcher[] matchers)`
  - Creates a `HitEntity` instance.
- `HitEntity(@Nonnull HitEntity other)`
  - Creates a `HitEntity` instance.

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
