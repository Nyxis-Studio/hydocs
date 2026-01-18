# ItemQuality

## Overview
- Documentation for `ItemQuality`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ItemQuality()`
  - Creates a `ItemQuality` instance.
- `ItemQuality(@Nullable String id, @Nullable String itemTooltipTexture, @Nullable String itemTooltipArrowTexture, @Nullable String slotTexture, @Nullable String blockSlotTexture, @Nullable String specialSlotTexture, @Nullable Color textColor, @Nullable String localizationKey, boolean visibleQualityLabel, boolean renderSpecialSlot, boolean hideFromSearch)`
  - Creates a `ItemQuality` instance.
- `ItemQuality(@Nonnull ItemQuality other)`
  - Creates a `ItemQuality` instance.

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
