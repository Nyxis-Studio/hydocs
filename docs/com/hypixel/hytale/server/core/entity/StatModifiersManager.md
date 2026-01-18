**Source Hash:** `c76c2e7dbb2849cbe5f69a25863ed2ccf9f1fd9dd1a504b9f21b686c7532cc71`

# StatModifiersManager

## Overview

## Constructor Descriptions
- `none()`: No documented methods.

## Method Descriptions
- `setRecalculate(boolean value)`: Add description.
  - Executes `setRecalculate` behavior.
- `queueEntityStatsToClear(@Nonnull int[] entityStatsToClear)`: Add description.
  - Executes `queueEntityStatsToClear` behavior.
- `recalculateEntityStatModifiers(@Nonnull Ref<EntityStore> ref, @Nonnull EntityStatMap statMap, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `recalculateEntityStatModifiers` behavior.
- `applyEffectModifiers(@Nonnull EntityStatMap statMap, @Nonnull Int2ObjectMap<Object2FloatMap<StaticModifier.CalculationType>> statModifiers)`: Add description.
  - Executes `applyEffectModifiers` behavior.
- `computeStatModifiers(double brokenPenalty, @Nonnull Int2ObjectMap<Object2FloatMap<StaticModifier.CalculationType>> statModifiers, @Nonnull ItemStack itemInHand, @Nonnull Int2ObjectMap<StaticModifier[]> itemStatModifiers)`: Add description.
  - Executes `computeStatModifiers` behavior.
- `addArmorStatModifiers(@Nonnull ItemStack itemStack, double brokenPenalties, @Nonnull Int2ObjectOpenHashMap<Object2FloatMap<StaticModifier.CalculationType>> statModifiers)`: Add description.
  - Executes `addArmorStatModifiers` behavior.
- `addItemStatModifiers(@Nullable ItemStack itemStack, @Nonnull EntityStatMap entityStatMap, @Nonnull String prefix, @Nonnull Function<Item, Int2ObjectMap<StaticModifier[]>> toStatModifiers)`: Add description.
  - Executes `addItemStatModifiers` behavior.
- `clearAllStatModifiers(@Nonnull EntityStatMap.Predictable predictable, @Nonnull EntityStatMap entityStatMap, @Nonnull String prefix, @Nullable Int2ObjectMap<StaticModifier[]> excluding)`: Add description.
  - Executes `clearAllStatModifiers` behavior.
- `clearStatModifiers(@Nonnull EntityStatMap.Predictable predictable, @Nonnull EntityStatMap entityStatMap, int statIndex, @Nonnull String prefix, int offset)`: Add description.
  - Executes `clearStatModifiers` behavior.
- `applyStatModifiers(@Nonnull EntityStatMap statMap, @Nonnull Int2ObjectMap<Object2FloatMap<StaticModifier.CalculationType>> statModifiers)`: Add description.
  - Executes `applyStatModifiers` behavior.

## Notes
- No additional notes.
