# InteractionEffects

## Overview
- Documentation for `InteractionEffects`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `InteractionEffects()`
  - Creates a `InteractionEffects` instance.
- `InteractionEffects(@Nullable ModelParticle[] particles, @Nullable ModelParticle[] firstPersonParticles, int worldSoundEventIndex, int localSoundEventIndex, @Nullable ModelTrail[] trails, boolean waitForAnimationToFinish, @Nullable String itemPlayerAnimationsId, @Nullable String itemAnimationId, boolean clearAnimationOnFinish, boolean clearSoundEventOnFinish, @Nullable CameraShakeEffect cameraShake, @Nullable MovementEffects movementEffects, float startDelay)`
  - Creates a `InteractionEffects` instance.
- `InteractionEffects(@Nonnull InteractionEffects other)`
  - Creates a `InteractionEffects` instance.

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
