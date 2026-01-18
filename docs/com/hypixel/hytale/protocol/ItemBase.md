# ItemBase

## Overview
- Documentation for `ItemBase`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ItemBase()`
  - Creates a `ItemBase` instance.
- `ItemBase(@Nullable String id, @Nullable String model, float scale, @Nullable String texture, @Nullable String animation, @Nullable String playerAnimationsId, boolean usePlayerAnimations, int maxStack, int reticleIndex, @Nullable String icon, @Nullable AssetIconProperties iconProperties, @Nullable ItemTranslationProperties translationProperties, int itemLevel, int qualityIndex, @Nullable ItemResourceType[] resourceTypes, boolean consumable, boolean variant, int blockId, @Nullable ItemTool tool, @Nullable ItemWeapon weapon, @Nullable ItemArmor armor, @Nullable ItemGlider gliderConfig, @Nullable ItemUtility utility, @Nullable BlockSelectorToolData blockSelectorTool, @Nullable ItemBuilderToolData builderToolData, @Nullable ItemEntityConfig itemEntity, @Nullable String set, @Nullable String[] categories, @Nullable ModelParticle[] particles, @Nullable ModelParticle[] firstPersonParticles, @Nullable ModelTrail[] trails, @Nullable ColorLight light, double durability, int soundEventIndex, int itemSoundSetIndex, @Nullable Map<InteractionType, Integer> interactions, @Nullable Map<String, Integer> interactionVars, @Nullable InteractionConfiguration interactionConfig, @Nullable String droppedItemAnimation, @Nullable int[] tagIndexes, @Nullable Map<Integer, ItemAppearanceCondition[]> itemAppearanceConditions, @Nullable int[] displayEntityStatsHUD, @Nullable ItemPullbackConfiguration pullbackConfig, boolean clipsGeometry, boolean renderDeployablePreview)`
  - Creates a `ItemBase` instance.
- `ItemBase(@Nonnull ItemBase other)`
  - Creates a `ItemBase` instance.

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
