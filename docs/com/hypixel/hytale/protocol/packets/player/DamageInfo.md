# DamageInfo

## Overview
- Documentation for `DamageInfo`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.player`.

## Constructors
- `DamageInfo()`
  - Creates a `DamageInfo` instance.
- `DamageInfo(@Nullable Vector3d damageSourcePosition, float damageAmount, @Nullable DamageCause damageCause)`
  - Creates a `DamageInfo` instance.
- `DamageInfo(@Nonnull DamageInfo other)`
  - Creates a `DamageInfo` instance.

## Methods
- `getId()`
  - Executes `getId` behavior.
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
