# SoundEventLayer

## Overview
- Documentation for `SoundEventLayer`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `SoundEventLayer()`
  - Creates a `SoundEventLayer` instance.
- `SoundEventLayer(float volume, float startDelay, boolean looping, int probability, float probabilityRerollDelay, int roundRobinHistorySize, @Nullable SoundEventLayerRandomSettings randomSettings, @Nullable String[] files)`
  - Creates a `SoundEventLayer` instance.
- `SoundEventLayer(@Nonnull SoundEventLayer other)`
  - Creates a `SoundEventLayer` instance.

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
