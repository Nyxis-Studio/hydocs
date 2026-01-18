# AmbienceFXConditions

## Overview
- Documentation for `AmbienceFXConditions`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `AmbienceFXConditions()`
  - Creates a `AmbienceFXConditions` instance.
- `AmbienceFXConditions(boolean never, @Nullable int[] environmentIndices, @Nullable int[] weatherIndices, @Nullable int[] fluidFXIndices, int environmentTagPatternIndex, int weatherTagPatternIndex, @Nullable AmbienceFXBlockSoundSet[] surroundingBlockSoundSets, @Nullable Range altitude, @Nullable Rangeb walls, boolean roof, int roofMaterialTagPatternIndex, boolean floor, @Nullable Rangeb sunLightLevel, @Nullable Rangeb torchLightLevel, @Nullable Rangeb globalLightLevel, @Nullable Rangef dayTime)`
  - Creates a `AmbienceFXConditions` instance.
- `AmbienceFXConditions(@Nonnull AmbienceFXConditions other)`
  - Creates a `AmbienceFXConditions` instance.

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
