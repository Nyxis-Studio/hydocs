# CraftingPlugin

## Overview
- Documentation for `CraftingPlugin`.
- Declared as a class in `com.hypixel.hytale.builtin.crafting`.

## Constructors
- `CraftingPlugin(@Nonnull JavaPluginInit init)`
  - Creates a `CraftingPlugin` instance.

## Methods
- `getAvailableRecipesForCategory(String benchId, String benchCategoryId)`
  - Executes `getAvailableRecipesForCategory` behavior.
- `isValidCraftingMaterialForBench(BenchState benchState, ItemStack itemStack)`
  - Executes `isValidCraftingMaterialForBench` behavior.
- `isValidUpgradeMaterialForBench(BenchState benchState, ItemStack itemStack)`
  - Executes `isValidUpgradeMaterialForBench` behavior.
- `setup()`
  - Executes `setup` behavior.
- `onItemAssetLoad(LoadedAssetsEvent<String, Item, DefaultAssetMap<String, Item>> event)`
  - Executes `onItemAssetLoad` behavior.
- `onItemAssetRemove(@Nonnull RemovedAssetsEvent<String, Item, DefaultAssetMap<String, Item>> event)`
  - Executes `onItemAssetRemove` behavior.
- `onRecipeLoad(LoadedAssetsEvent<String, CraftingRecipe, DefaultAssetMap<String, CraftingRecipe>> event)`
  - Executes `onRecipeLoad` behavior.
- `onRecipeRemove(RemovedAssetsEvent<String, CraftingRecipe, DefaultAssetMap<String, CraftingRecipe>> event)`
  - Executes `onRecipeRemove` behavior.
- `computeBenchRecipeRegistries()`
  - Executes `computeBenchRecipeRegistries` behavior.
- `getBenchRecipes(@Nonnull Bench bench)`
  - Executes `getBenchRecipes` behavior.
- `getBenchRecipes(BenchType benchType, String name)`
  - Executes `getBenchRecipes` behavior.
- `getBenchRecipes(BenchType benchType, String benchId, @Nullable String category)`
  - Executes `getBenchRecipes` behavior.
- `hasCategory(@Nonnull CraftingRecipe recipe, String category)`
  - Executes `hasCategory` behavior.
- `learnRecipe(@Nonnull Ref<EntityStore> ref, @Nonnull String recipeId, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `learnRecipe` behavior.
- `forgetRecipe(@Nonnull Ref<EntityStore> ref, @Nonnull String itemId, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `forgetRecipe` behavior.
- `sendKnownRecipes(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `sendKnownRecipes` behavior.
- `getCraftingManagerComponentType()`
  - Executes `getCraftingManagerComponentType` behavior.
- `get()`
  - Executes `get` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `onEntityAdded(@Nonnull Ref<EntityStore> ref, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<EntityStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityRemove` behavior.

## Notes
- No additional notes.
