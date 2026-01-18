# ItemUtility

## Overview
- Documentation for `ItemUtility`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ItemUtility()`
  - Creates a `ItemUtility` instance.
- `ItemUtility(boolean usable, boolean compatible, @Nullable int[] entityStatsToClear, @Nullable Map<Integer, Modifier[]> statModifiers)`
  - Creates a `ItemUtility` instance.
- `ItemUtility(@Nonnull ItemUtility other)`
  - Creates a `ItemUtility` instance.

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
