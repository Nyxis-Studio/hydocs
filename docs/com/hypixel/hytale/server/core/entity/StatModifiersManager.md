# StatModifiersManager

## Overview
- Documentation for `StatModifiersManager`.
- Declared as a class in `com.hypixel.hytale.server.core.entity`.

## Constructors
- None.

## Methods
- `setRecalculate(boolean value)`
  - Executes `setRecalculate` behavior.
- `queueEntityStatsToClear(@Nonnull int[] entityStatsToClear)`
  - Executes `queueEntityStatsToClear` behavior.
- `recalculateEntityStatModifiers(@Nonnull Ref<EntityStore> ref, @Nonnull EntityStatMap statMap, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `recalculateEntityStatModifiers` behavior.
- `applyEffectModifiers(@Nonnull EntityStatMap statMap, @Nonnull Int2ObjectMap<Object2FloatMap<StaticModifier.CalculationType>> statModifiers)`
  - Executes `applyEffectModifiers` behavior.
- `computeStatModifiers(double brokenPenalty, @Nonnull Int2ObjectMap<Object2FloatMap<StaticModifier.CalculationType>> statModifiers, @Nonnull ItemStack itemInHand, @Nonnull Int2ObjectMap<StaticModifier[]> itemStatModifiers)`
  - Executes `computeStatModifiers` behavior.
- `addArmorStatModifiers(@Nonnull ItemStack itemStack, double brokenPenalties, @Nonnull Int2ObjectOpenHashMap<Object2FloatMap<StaticModifier.CalculationType>> statModifiers)`
  - Executes `addArmorStatModifiers` behavior.
- `addItemStatModifiers(@Nullable ItemStack itemStack, @Nonnull EntityStatMap entityStatMap, @Nonnull String prefix, @Nonnull Function<Item, Int2ObjectMap<StaticModifier[]>> toStatModifiers)`
  - Executes `addItemStatModifiers` behavior.
- `clearAllStatModifiers(@Nonnull EntityStatMap.Predictable predictable, @Nonnull EntityStatMap entityStatMap, @Nonnull String prefix, @Nullable Int2ObjectMap<StaticModifier[]> excluding)`
  - Executes `clearAllStatModifiers` behavior.
- `clearStatModifiers(@Nonnull EntityStatMap.Predictable predictable, @Nonnull EntityStatMap entityStatMap, int statIndex, @Nonnull String prefix, int offset)`
  - Executes `clearStatModifiers` behavior.
- `applyStatModifiers(@Nonnull EntityStatMap statMap, @Nonnull Int2ObjectMap<Object2FloatMap<StaticModifier.CalculationType>> statModifiers)`
  - Executes `applyStatModifiers` behavior.

## Notes
- No additional notes.
