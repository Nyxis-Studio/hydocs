# CraftingManager

## Overview
- Documentation for `CraftingManager`.
- Declared as a class in `com.hypixel.hytale.builtin.crafting.component`.

## Constructors
- `CraftingManager()`
  - Creates a `CraftingManager` instance.
- `CraftingManager(@Nonnull CraftingManager other)`
  - Creates a `CraftingManager` instance.
- `CraftingManager(this)`
  - Creates a `CraftingManager` instance.

## Methods
- `getComponentType()`
  - Executes `getComponentType` behavior.
- `hasBenchSet()`
  - Executes `hasBenchSet` behavior.
- `setBench(int x, int y, int z, @Nonnull BlockType blockType)`
  - Executes `setBench` behavior.
- `clearBench(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store)`
  - Executes `clearBench` behavior.
- `craftItem(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> store, @Nonnull CraftingRecipe recipe, int quantity, @Nonnull ItemContainer itemContainer)`
  - Executes `craftItem` behavior.
- `getRecipeOutputTranslationKey(CraftingRecipe recipe)`
  - Executes `getRecipeOutputTranslationKey` behavior.
- `queueCraft(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> store, @Nonnull CraftingWindow window, int transactionId, @Nonnull CraftingRecipe recipe, int quantity, @Nonnull ItemContainer inputItemContainer, @Nonnull InputRemovalType inputRemovalType)`
  - Executes `queueCraft` behavior.
- `tick(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> store, float dt)`
  - Executes `tick` behavior.
- `cancelAllCrafting(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> store)`
  - Executes `cancelAllCrafting` behavior.
- `isValidBenchForRecipe(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> store, @Nonnull CraftingRecipe recipe)`
  - Executes `isValidBenchForRecipe` behavior.
- `giveOutput(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> store, @Nonnull CraftingJob job, int currentItemId)`
  - Executes `giveOutput` behavior.
- `giveOutput(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> store, @Nonnull CraftingRecipe craftingRecipe, int quantity)`
  - Executes `giveOutput` behavior.
- `removeInputFromInventory(@Nonnull CraftingJob job, int currentItemId)`
  - Executes `removeInputFromInventory` behavior.
- `removeInputFromInventory(@Nonnull ItemContainer itemContainer, @Nonnull CraftingRecipe craftingRecipe, int quantity)`
  - Executes `removeInputFromInventory` behavior.
- `refundInputToInventory(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> store, @Nonnull CraftingJob job, int currentItemId)`
  - Executes `refundInputToInventory` behavior.
- `getOutputItemStacks(@Nonnull CraftingRecipe recipe)`
  - Executes `getOutputItemStacks` behavior.
- `getOutputItemStacks(@Nonnull CraftingRecipe recipe, int quantity)`
  - Executes `getOutputItemStacks` behavior.
- `getOutputItemStack(@Nonnull MaterialQuantity outputMaterial, @Nonnull String id)`
  - Executes `getOutputItemStack` behavior.
- `getOutputItemStack(@Nonnull MaterialQuantity outputMaterial, int quantity)`
  - Executes `getOutputItemStack` behavior.
- `getInputMaterials(@Nonnull CraftingRecipe recipe)`
  - Executes `getInputMaterials` behavior.
- `getInputMaterials(@Nonnull MaterialQuantity[] input)`
  - Executes `getInputMaterials` behavior.
- `getInputMaterials(@Nonnull CraftingRecipe recipe, int quantity)`
  - Executes `getInputMaterials` behavior.
- `getInputMaterials(@Nonnull MaterialQuantity[] input, int quantity)`
  - Executes `getInputMaterials` behavior.
- `matches(@Nonnull MaterialQuantity craftingMaterial, @Nonnull ItemStack itemStack)`
  - Executes `matches` behavior.
- `generateInventoryHints(@Nonnull List<CraftingRecipe> recipes, int inputSlotIndex, @Nonnull ItemContainer container)`
  - Executes `generateInventoryHints` behavior.
- `matchesAnyRecipe(@Nonnull List<CraftingRecipe> recipes, int inputSlotIndex, @Nonnull ItemStack slotItemStack)`
  - Executes `matchesAnyRecipe` behavior.
- `startTierUpgrade(Ref<EntityStore> ref, ComponentAccessor<EntityStore> store, @Nonnull BenchWindow window)`
  - Executes `startTierUpgrade` behavior.
- `finishTierUpgrade(Ref<EntityStore> ref, ComponentAccessor<EntityStore> store)`
  - Executes `finishTierUpgrade` behavior.
- `getBenchTierLevelData(int level)`
  - Executes `getBenchTierLevelData` behavior.
- `getBenchUpgradeRequierement(int tierLevel)`
  - Executes `getBenchUpgradeRequierement` behavior.
- `getBenchTierLevel(ComponentAccessor<EntityStore> store)`
  - Executes `getBenchTierLevel` behavior.
- `getContainersAroundBench(@Nonnull BenchState benchState)`
  - Executes `getContainersAroundBench` behavior.
- `feedExtraResourcesSection(BenchState benchState, MaterialExtraResourcesSection extraResourcesSection)`
  - Executes `feedExtraResourcesSection` behavior.
- `toString()`
  - Executes `toString` behavior.
- `clone()`
  - Executes `clone` behavior.
- `computeLoadingPercent()`
  - Executes `computeLoadingPercent` behavior.

## Notes
- No additional notes.
