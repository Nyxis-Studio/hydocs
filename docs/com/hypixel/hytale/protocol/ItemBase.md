**Source Hash:** `883c34bdf7f10065746c34cec2674109f66ea0f18a9e6f259c9ed63662fad90f`

# ItemBase

## Overview

## Constructor Descriptions
- `ItemBase()`
  - Creates a `ItemBase` instance.
- `ItemBase(@Nullable String id, @Nullable String model, float scale, @Nullable String texture, @Nullable String animation, @Nullable String playerAnimationsId, boolean usePlayerAnimations, int maxStack, int reticleIndex, @Nullable String icon, @Nullable AssetIconProperties iconProperties, @Nullable ItemTranslationProperties translationProperties, int itemLevel, int qualityIndex, @Nullable ItemResourceType[] resourceTypes, boolean consumable, boolean variant, int blockId, @Nullable ItemTool tool, @Nullable ItemWeapon weapon, @Nullable ItemArmor armor, @Nullable ItemGlider gliderConfig, @Nullable ItemUtility utility, @Nullable BlockSelectorToolData blockSelectorTool, @Nullable ItemBuilderToolData builderToolData, @Nullable ItemEntityConfig itemEntity, @Nullable String set, @Nullable String[] categories, @Nullable ModelParticle[] particles, @Nullable ModelParticle[] firstPersonParticles, @Nullable ModelTrail[] trails, @Nullable ColorLight light, double durability, int soundEventIndex, int itemSoundSetIndex, @Nullable Map<InteractionType, Integer> interactions, @Nullable Map<String, Integer> interactionVars, @Nullable InteractionConfiguration interactionConfig, @Nullable String droppedItemAnimation, @Nullable int[] tagIndexes, @Nullable Map<Integer, ItemAppearanceCondition[]> itemAppearanceConditions, @Nullable int[] displayEntityStatsHUD, @Nullable ItemPullbackConfiguration pullbackConfig, boolean clipsGeometry, boolean renderDeployablePreview)`
  - Creates a `ItemBase` instance.
- `ItemBase(@Nonnull ItemBase other)`
  - Creates a `ItemBase` instance.

## Method Descriptions
- `deserialize(@Nonnull ByteBuf buf, int offset)`: Add description.
  - Executes `deserialize` behavior.
- `computeBytesConsumed(@Nonnull ByteBuf buf, int offset)`: Add description.
  - Executes `computeBytesConsumed` behavior.
- `serialize(@Nonnull ByteBuf buf)`: Add description.
  - Executes `serialize` behavior.
- `computeSize()`: Add description.
  - Executes `computeSize` behavior.
- `validateStructure(@Nonnull ByteBuf buffer, int offset)`: Add description.
  - Executes `validateStructure` behavior.
- `clone()`: Add description.
  - Executes `clone` behavior.
- `equals(Object obj)`: Add description.
  - Executes `equals` behavior.
- `hashCode()`: Add description.
  - Executes `hashCode` behavior.

## Notes
- No additional notes.
