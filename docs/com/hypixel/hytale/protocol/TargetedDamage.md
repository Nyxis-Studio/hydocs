# TargetedDamage

## Overview
- Documentation for `TargetedDamage`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `TargetedDamage()`
  - Creates a `TargetedDamage` instance.
- `TargetedDamage(int index, @Nullable DamageEffects damageEffects, int next)`
  - Creates a `TargetedDamage` instance.
- `TargetedDamage(@Nonnull TargetedDamage other)`
  - Creates a `TargetedDamage` instance.

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
