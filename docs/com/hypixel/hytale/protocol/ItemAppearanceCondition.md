# ItemAppearanceCondition

## Overview
- Documentation for `ItemAppearanceCondition`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ItemAppearanceCondition()`
  - Creates a `ItemAppearanceCondition` instance.
- `ItemAppearanceCondition(@Nullable ModelParticle[] particles, @Nullable ModelParticle[] firstPersonParticles, @Nullable String model, @Nullable String texture, @Nullable String modelVFXId, @Nullable FloatRange condition, @Nonnull ValueType conditionValueType, int localSoundEventId, int worldSoundEventId)`
  - Creates a `ItemAppearanceCondition` instance.
- `ItemAppearanceCondition(@Nonnull ItemAppearanceCondition other)`
  - Creates a `ItemAppearanceCondition` instance.

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
