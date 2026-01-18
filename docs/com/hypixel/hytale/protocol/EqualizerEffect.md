# EqualizerEffect

## Overview
- Documentation for `EqualizerEffect`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `EqualizerEffect()`
  - Creates a `EqualizerEffect` instance.
- `EqualizerEffect(@Nullable String id, float lowGain, float lowCutOff, float lowMidGain, float lowMidCenter, float lowMidWidth, float highMidGain, float highMidCenter, float highMidWidth, float highGain, float highCutOff)`
  - Creates a `EqualizerEffect` instance.
- `EqualizerEffect(@Nonnull EqualizerEffect other)`
  - Creates a `EqualizerEffect` instance.

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
