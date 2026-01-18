# BlockSoundSet

## Overview
- Documentation for `BlockSoundSet`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `BlockSoundSet()`
  - Creates a `BlockSoundSet` instance.
- `BlockSoundSet(@Nullable String id, @Nullable Map<BlockSoundEvent, Integer> soundEventIndices, @Nullable FloatRange moveInRepeatRange)`
  - Creates a `BlockSoundSet` instance.
- `BlockSoundSet(@Nonnull BlockSoundSet other)`
  - Creates a `BlockSoundSet` instance.

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
