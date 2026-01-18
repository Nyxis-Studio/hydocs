# ReverbEffect

## Overview
- Documentation for `ReverbEffect`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ReverbEffect()`
  - Creates a `ReverbEffect` instance.
- `ReverbEffect(@Nullable String id, float dryGain, float modalDensity, float diffusion, float gain, float highFrequencyGain, float decayTime, float highFrequencyDecayRatio, float reflectionGain, float reflectionDelay, float lateReverbGain, float lateReverbDelay, float roomRolloffFactor, float airAbsorptionHighFrequencyGain, boolean limitDecayHighFrequency)`
  - Creates a `ReverbEffect` instance.
- `ReverbEffect(@Nonnull ReverbEffect other)`
  - Creates a `ReverbEffect` instance.

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
