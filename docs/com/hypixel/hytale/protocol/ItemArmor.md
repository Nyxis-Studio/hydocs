# ItemArmor

## Overview
- Documentation for `ItemArmor`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ItemArmor()`
  - Creates a `ItemArmor` instance.
- `ItemArmor(@Nonnull ItemArmorSlot armorSlot, @Nullable Cosmetic[] cosmeticsToHide, @Nullable Map<Integer, Modifier[]> statModifiers, double baseDamageResistance, @Nullable Map<String, Modifier[]> damageResistance, @Nullable Map<String, Modifier[]> damageEnhancement, @Nullable Map<String, Modifier[]> damageClassEnhancement)`
  - Creates a `ItemArmor` instance.
- `ItemArmor(@Nonnull ItemArmor other)`
  - Creates a `ItemArmor` instance.

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
