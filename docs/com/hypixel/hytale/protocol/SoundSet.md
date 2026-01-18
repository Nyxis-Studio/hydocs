# SoundSet

## Overview
- Documentation for `SoundSet`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `SoundSet()`
  - Creates a `SoundSet` instance.
- `SoundSet(@Nullable String id, @Nullable Map<String, Integer> sounds, @Nonnull SoundCategory category)`
  - Creates a `SoundSet` instance.
- `SoundSet(@Nonnull SoundSet other)`
  - Creates a `SoundSet` instance.

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
