**Source Hash:** `890de427f23064d3ec77e9b6d57f602b9963ea99fedd79b4ece4ab3ccff2906d`

# CraftingPlugin

## Overview

## Constructor Descriptions
- `CraftingPlugin(@Nonnull JavaPluginInit init)`
  - Creates a `CraftingPlugin` instance.

## Method Descriptions
- `getAvailableRecipesForCategory(String benchId, String benchCategoryId)`: Add description.
  - Executes `getAvailableRecipesForCategory` behavior.
- `isValidCraftingMaterialForBench(BenchState benchState, ItemStack itemStack)`: Add description.
  - Executes `isValidCraftingMaterialForBench` behavior.
- `isValidUpgradeMaterialForBench(BenchState benchState, ItemStack itemStack)`: Add description.
  - Executes `isValidUpgradeMaterialForBench` behavior.
- `setup()`: Add description.
  - Executes `setup` behavior.
- `onItemAssetLoad(LoadedAssetsEvent<String, Item, DefaultAssetMap<String, Item>> event)`: Add description.
  - Executes `onItemAssetLoad` behavior.
- `onItemAssetRemove(@Nonnull RemovedAssetsEvent<String, Item, DefaultAssetMap<String, Item>> event)`: Add description.
  - Executes `onItemAssetRemove` behavior.
- `onRecipeLoad(LoadedAssetsEvent<String, CraftingRecipe, DefaultAssetMap<String, CraftingRecipe>> event)`: Add description.
  - Executes `onRecipeLoad` behavior.
- `onRecipeRemove(RemovedAssetsEvent<String, CraftingRecipe, DefaultAssetMap<String, CraftingRecipe>> event)`: Add description.
  - Executes `onRecipeRemove` behavior.
- `computeBenchRecipeRegistries()`: Add description.
  - Executes `computeBenchRecipeRegistries` behavior.
- `getBenchRecipes(@Nonnull Bench bench)`: Add description.
  - Executes `getBenchRecipes` behavior.
- `getBenchRecipes(BenchType benchType, String name)`: Add description.
  - Executes `getBenchRecipes` behavior.
- `getBenchRecipes(BenchType benchType, String benchId, @Nullable String category)`: Add description.
  - Executes `getBenchRecipes` behavior.
- `hasCategory(@Nonnull CraftingRecipe recipe, String category)`: Add description.
  - Executes `hasCategory` behavior.
- `learnRecipe(@Nonnull Ref<EntityStore> ref, @Nonnull String recipeId, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `learnRecipe` behavior.
- `forgetRecipe(@Nonnull Ref<EntityStore> ref, @Nonnull String itemId, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `forgetRecipe` behavior.
- `sendKnownRecipes(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `sendKnownRecipes` behavior.
- `getCraftingManagerComponentType()`: Add description.
  - Executes `getCraftingManagerComponentType` behavior.
- `get()`: Add description.
  - Executes `get` behavior.
- `getQuery()`: Add description.
  - Executes `getQuery` behavior.
- `onEntityAdded(@Nonnull Ref<EntityStore> ref, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<EntityStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `onEntityRemove` behavior.

## Notes
- No additional notes.
