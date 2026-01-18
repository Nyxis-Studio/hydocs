# EntityUIComponent

## Overview
- Documentation for `EntityUIComponent`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `EntityUIComponent()`
  - Creates a `EntityUIComponent` instance.
- `EntityUIComponent(@Nonnull EntityUIType type, @Nullable Vector2f hitboxOffset, boolean unknown, int entityStatIndex, @Nullable RangeVector2f combatTextRandomPositionOffsetRange, float combatTextViewportMargin, float combatTextDuration, float combatTextHitAngleModifierStrength, float combatTextFontSize, @Nullable Color combatTextColor, @Nullable CombatTextEntityUIComponentAnimationEvent[] combatTextAnimationEvents)`
  - Creates a `EntityUIComponent` instance.
- `EntityUIComponent(@Nonnull EntityUIComponent other)`
  - Creates a `EntityUIComponent` instance.

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
