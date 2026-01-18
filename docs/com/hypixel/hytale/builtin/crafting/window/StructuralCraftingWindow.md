# StructuralCraftingWindow

## Overview
- Documentation for `StructuralCraftingWindow`.
- Declared as a class in `com.hypixel.hytale.builtin.crafting.window`.

## Constructors
- `StructuralCraftingWindow(BenchState benchState)`
  - Creates a `StructuralCraftingWindow` instance.

## Methods
- `isValidInput(FilterActionType filterActionType, ItemContainer itemContainer, short i, ItemStack itemStack)`
  - Executes `isValidInput` behavior.
- `sortRecipes(ObjectList<CraftingRecipe> matching, StructuralCraftingBench structuralBench)`
  - Executes `sortRecipes` behavior.
- `hasHeaderCategory(StructuralCraftingBench bench, CraftingRecipe recipe)`
  - Executes `hasHeaderCategory` behavior.
- `getSortingPriority(StructuralCraftingBench bench, CraftingRecipe recipe)`
  - Executes `getSortingPriority` behavior.
- `handleAction(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull WindowAction action)`
  - Executes `handleAction` behavior.
- `playCraftSound(Ref<EntityStore> ref, Store<EntityStore> store, Item item)`
  - Executes `playCraftSound` behavior.
- `changeBlockType(@Nonnull Ref<EntityStore> ref, boolean down, @Nonnull Store<EntityStore> store)`
  - Executes `changeBlockType` behavior.
- `getItemContainer()`
  - Executes `getItemContainer` behavior.
- `onOpen0()`
  - Executes `onOpen0` behavior.
- `onClose0()`
  - Executes `onClose0` behavior.
- `updateRecipes()`
  - Executes `updateRecipes` behavior.
- `getMatchingRecipes(@Nullable ItemStack inputStack)`
  - Executes `getMatchingRecipes` behavior.

## Notes
- No additional notes.
