# ModifyInventoryInteraction

## Overview
- Documentation for `ModifyInventoryInteraction`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ModifyInventoryInteraction()`
  - Creates a `ModifyInventoryInteraction` instance.
- `ModifyInventoryInteraction(@Nonnull WaitForDataFrom waitForDataFrom, @Nullable InteractionEffects effects, float horizontalSpeedMultiplier, float runTime, boolean cancelOnItemChange, @Nullable Map<GameMode, InteractionSettings> settings, @Nullable InteractionRules rules, @Nullable int[] tags, @Nullable InteractionCameraSettings camera, int next, int failed, @Nullable GameMode requiredGameMode, @Nullable ItemWithAllMetadata itemToRemove, int adjustHeldItemQuantity, @Nullable ItemWithAllMetadata itemToAdd, @Nullable String brokenItem, double adjustHeldItemDurability)`
  - Creates a `ModifyInventoryInteraction` instance.
- `ModifyInventoryInteraction(@Nonnull ModifyInventoryInteraction other)`
  - Creates a `ModifyInventoryInteraction` instance.

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
