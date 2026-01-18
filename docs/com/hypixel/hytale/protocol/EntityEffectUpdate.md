# EntityEffectUpdate

## Overview
- Documentation for `EntityEffectUpdate`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `EntityEffectUpdate()`
  - Creates a `EntityEffectUpdate` instance.
- `EntityEffectUpdate(@Nonnull EffectOp type, int id, float remainingTime, boolean infinite, boolean debuff, @Nullable String statusEffectIcon)`
  - Creates a `EntityEffectUpdate` instance.
- `EntityEffectUpdate(@Nonnull EntityEffectUpdate other)`
  - Creates a `EntityEffectUpdate` instance.

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
