# ApplicationEffects

## Overview
- Documentation for `ApplicationEffects`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ApplicationEffects()`
  - Creates a `ApplicationEffects` instance.
- `ApplicationEffects(@Nullable Color entityBottomTint, @Nullable Color entityTopTint, @Nullable String entityAnimationId, @Nullable ModelParticle[] particles, @Nullable ModelParticle[] firstPersonParticles, @Nullable String screenEffect, float horizontalSpeedMultiplier, int soundEventIndexLocal, int soundEventIndexWorld, @Nullable String modelVFXId, @Nullable MovementEffects movementEffects, float mouseSensitivityAdjustmentTarget, float mouseSensitivityAdjustmentDuration, @Nullable AbilityEffects abilityEffects)`
  - Creates a `ApplicationEffects` instance.
- `ApplicationEffects(@Nonnull ApplicationEffects other)`
  - Creates a `ApplicationEffects` instance.

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
