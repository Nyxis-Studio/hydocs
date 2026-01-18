**Source Hash:** `5ec22d95d93b35f1e31dc2b6bc27cdc36f57059c62db3aa1db388dc1e8801416`

# CraftingManager

## Overview

## Constructor Descriptions
- `CraftingManager()`
  - Creates a `CraftingManager` instance.
- `CraftingManager(@Nonnull CraftingManager other)`
  - Creates a `CraftingManager` instance.
- `CraftingManager(this)`
  - Creates a `CraftingManager` instance.

## Method Descriptions
- `getComponentType()`: Add description.
  - Executes `getComponentType` behavior.
- `hasBenchSet()`: Add description.
  - Executes `hasBenchSet` behavior.
- `setBench(int x, int y, int z, @Nonnull BlockType blockType)`: Add description.
  - Executes `setBench` behavior.
- `clearBench(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `clearBench` behavior.
- `craftItem(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> store, @Nonnull CraftingRecipe recipe, int quantity, @Nonnull ItemContainer itemContainer)`: Add description.
  - Executes `craftItem` behavior.
- `getRecipeOutputTranslationKey(CraftingRecipe recipe)`: Add description.
  - Executes `getRecipeOutputTranslationKey` behavior.
- `queueCraft(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> store, @Nonnull CraftingWindow window, int transactionId, @Nonnull CraftingRecipe recipe, int quantity, @Nonnull ItemContainer inputItemContainer, @Nonnull InputRemovalType inputRemovalType)`: Add description.
  - Executes `queueCraft` behavior.
- `tick(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> store, float dt)`: Add description.
  - Executes `tick` behavior.
- `cancelAllCrafting(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> store)`: Add description.
  - Executes `cancelAllCrafting` behavior.
- `isValidBenchForRecipe(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> store, @Nonnull CraftingRecipe recipe)`: Add description.
  - Executes `isValidBenchForRecipe` behavior.
- `giveOutput(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> store, @Nonnull CraftingJob job, int currentItemId)`: Add description.
  - Executes `giveOutput` behavior.
- `giveOutput(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> store, @Nonnull CraftingRecipe craftingRecipe, int quantity)`: Add description.
  - Executes `giveOutput` behavior.
- `removeInputFromInventory(@Nonnull CraftingJob job, int currentItemId)`: Add description.
  - Executes `removeInputFromInventory` behavior.
- `removeInputFromInventory(@Nonnull ItemContainer itemContainer, @Nonnull CraftingRecipe craftingRecipe, int quantity)`: Add description.
  - Executes `removeInputFromInventory` behavior.
- `refundInputToInventory(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> store, @Nonnull CraftingJob job, int currentItemId)`: Add description.
  - Executes `refundInputToInventory` behavior.
- `getOutputItemStacks(@Nonnull CraftingRecipe recipe)`: Add description.
  - Executes `getOutputItemStacks` behavior.
- `getOutputItemStacks(@Nonnull CraftingRecipe recipe, int quantity)`: Add description.
  - Executes `getOutputItemStacks` behavior.
- `getOutputItemStack(@Nonnull MaterialQuantity outputMaterial, @Nonnull String id)`: Add description.
  - Executes `getOutputItemStack` behavior.
- `getOutputItemStack(@Nonnull MaterialQuantity outputMaterial, int quantity)`: Add description.
  - Executes `getOutputItemStack` behavior.
- `getInputMaterials(@Nonnull CraftingRecipe recipe)`: Add description.
  - Executes `getInputMaterials` behavior.
- `getInputMaterials(@Nonnull MaterialQuantity[] input)`: Add description.
  - Executes `getInputMaterials` behavior.
- `getInputMaterials(@Nonnull CraftingRecipe recipe, int quantity)`: Add description.
  - Executes `getInputMaterials` behavior.
- `getInputMaterials(@Nonnull MaterialQuantity[] input, int quantity)`: Add description.
  - Executes `getInputMaterials` behavior.
- `matches(@Nonnull MaterialQuantity craftingMaterial, @Nonnull ItemStack itemStack)`: Add description.
  - Executes `matches` behavior.
- `generateInventoryHints(@Nonnull List<CraftingRecipe> recipes, int inputSlotIndex, @Nonnull ItemContainer container)`: Add description.
  - Executes `generateInventoryHints` behavior.
- `matchesAnyRecipe(@Nonnull List<CraftingRecipe> recipes, int inputSlotIndex, @Nonnull ItemStack slotItemStack)`: Add description.
  - Executes `matchesAnyRecipe` behavior.
- `startTierUpgrade(Ref<EntityStore> ref, ComponentAccessor<EntityStore> store, @Nonnull BenchWindow window)`: Add description.
  - Executes `startTierUpgrade` behavior.
- `finishTierUpgrade(Ref<EntityStore> ref, ComponentAccessor<EntityStore> store)`: Add description.
  - Executes `finishTierUpgrade` behavior.
- `getBenchTierLevelData(int level)`: Add description.
  - Executes `getBenchTierLevelData` behavior.
- `getBenchUpgradeRequierement(int tierLevel)`: Add description.
  - Executes `getBenchUpgradeRequierement` behavior.
- `getBenchTierLevel(ComponentAccessor<EntityStore> store)`: Add description.
  - Executes `getBenchTierLevel` behavior.
- `getContainersAroundBench(@Nonnull BenchState benchState)`: Add description.
  - Executes `getContainersAroundBench` behavior.
- `feedExtraResourcesSection(BenchState benchState, MaterialExtraResourcesSection extraResourcesSection)`: Add description.
  - Executes `feedExtraResourcesSection` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.
- `clone()`: Add description.
  - Executes `clone` behavior.
- `computeLoadingPercent()`: Add description.
  - Executes `computeLoadingPercent` behavior.

## Notes
- No additional notes.
