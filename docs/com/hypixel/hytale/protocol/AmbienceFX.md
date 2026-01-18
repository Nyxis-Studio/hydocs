# AmbienceFX

## Overview
- Documentation for `AmbienceFX`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `AmbienceFX()`
  - Creates a `AmbienceFX` instance.
- `AmbienceFX(@Nullable String id, @Nullable AmbienceFXConditions conditions, @Nullable AmbienceFXSound[] sounds, @Nullable AmbienceFXMusic music, @Nullable AmbienceFXAmbientBed ambientBed, @Nullable AmbienceFXSoundEffect soundEffect, int priority, @Nullable int[] blockedAmbienceFxIndices, int audioCategoryIndex)`
  - Creates a `AmbienceFX` instance.
- `AmbienceFX(@Nonnull AmbienceFX other)`
  - Creates a `AmbienceFX` instance.

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
