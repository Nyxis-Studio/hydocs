# SoundEvent

## Overview
- Documentation for `SoundEvent`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `SoundEvent()`
  - Creates a `SoundEvent` instance.
- `SoundEvent(@Nullable String id, float volume, float pitch, float musicDuckingVolume, float ambientDuckingVolume, int maxInstance, boolean preventSoundInterruption, float startAttenuationDistance, float maxDistance, @Nullable SoundEventLayer[] layers, int audioCategory)`
  - Creates a `SoundEvent` instance.
- `SoundEvent(@Nonnull SoundEvent other)`
  - Creates a `SoundEvent` instance.

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
