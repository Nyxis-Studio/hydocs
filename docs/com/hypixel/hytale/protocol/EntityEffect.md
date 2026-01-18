# EntityEffect

## Overview
- Documentation for `EntityEffect`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `EntityEffect()`
  - Creates a `EntityEffect` instance.
- `EntityEffect(@Nullable String id, @Nullable String name, @Nullable ApplicationEffects applicationEffects, int worldRemovalSoundEventIndex, int localRemovalSoundEventIndex, @Nullable ModelOverride modelOverride, float duration, boolean infinite, boolean debuff, @Nullable String statusEffectIcon, @Nonnull OverlapBehavior overlapBehavior, double damageCalculatorCooldown, @Nullable Map<Integer, Float> statModifiers, @Nonnull ValueType valueType)`
  - Creates a `EntityEffect` instance.
- `EntityEffect(@Nonnull EntityEffect other)`
  - Creates a `EntityEffect` instance.

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
