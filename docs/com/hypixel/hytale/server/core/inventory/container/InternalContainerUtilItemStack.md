# InternalContainerUtilItemStack

## Overview
- Documentation for `InternalContainerUtilItemStack`.
- Declared as a class in `com.hypixel.hytale.server.core.inventory.container`.

## Constructors
- None.

## Methods
- `testAddToExistingSlot(@Nonnull ItemContainer abstractItemContainer, short slot, ItemStack itemStack, int itemMaxStack, int testQuantityRemaining, boolean filter)`
  - Executes `testAddToExistingSlot` behavior.
- `internal_addToExistingSlot(@Nonnull ItemContainer container, short slot, @Nonnull ItemStack itemStack, int itemMaxStack, boolean filter)`
  - Executes `internal_addToExistingSlot` behavior.
- `internal_addToEmptySlot(@Nonnull ItemContainer container, short slot, @Nonnull ItemStack itemStack, int itemMaxStack, boolean filter)`
  - Executes `internal_addToEmptySlot` behavior.
- `testAddToEmptySlots(@Nonnull ItemContainer container, ItemStack itemStack, int itemMaxStack, int testQuantityRemaining, boolean filter)`
  - Executes `testAddToEmptySlots` behavior.
- `internal_addItemStackToSlot(@Nonnull ItemContainer itemContainer, short slot, @Nonnull ItemStack itemStack, boolean allOrNothing, boolean filter)`
  - Executes `internal_addItemStackToSlot` behavior.
- `internal_setItemStackForSlot(@Nonnull ItemContainer itemContainer, short slot, ItemStack itemStack, boolean filter)`
  - Executes `internal_setItemStackForSlot` behavior.
- `internal_removeItemStackFromSlot(@Nonnull ItemContainer itemContainer, short slot, boolean filter)`
  - Executes `internal_removeItemStackFromSlot` behavior.
- `internal_removeItemStackFromSlot(@Nonnull ItemContainer itemContainer, short slot, int quantityToRemove, boolean allOrNothing, boolean filter)`
  - Executes `internal_removeItemStackFromSlot` behavior.
- `internal_removeItemStackFromSlot(@Nonnull ItemContainer itemContainer, short slot, @Nullable ItemStack itemStackToRemove, int quantityToRemove, boolean allOrNothing, boolean filter)`
  - Executes `internal_removeItemStackFromSlot` behavior.
- `internal_removeItemStackFromSlot(@Nonnull ItemContainer itemContainer, short slot, @Nullable ItemStack itemStackToRemove, int quantityToRemove, boolean allOrNothing, boolean filter, BiPredicate<ItemStack, ItemStack> predicate)`
  - Executes `internal_removeItemStackFromSlot` behavior.
- `testRemoveItemStackFromSlot(@Nonnull ItemContainer container, short slot, ItemStack itemStack, int testQuantityRemaining, boolean filter)`
  - Executes `testRemoveItemStackFromSlot` behavior.
- `testRemoveItemStackFromSlot(@Nonnull ItemContainer container, short slot, ItemStack itemStack, int testQuantityRemaining, boolean filter, BiPredicate<ItemStack, ItemStack> predicate)`
  - Executes `testRemoveItemStackFromSlot` behavior.
- `internal_addItemStack(@Nonnull ItemContainer itemContainer, @Nonnull ItemStack itemStack, boolean allOrNothing, boolean fullStacks, boolean filter)`
  - Executes `internal_addItemStack` behavior.
- `internal_addItemStacks(@Nonnull ItemContainer itemContainer, @Nullable List<ItemStack> itemStacks, boolean allOrNothing, boolean fullStacks, boolean filter)`
  - Executes `internal_addItemStacks` behavior.
- `internal_addItemStacksOrdered(@Nonnull ItemContainer itemContainer, short offset, @Nullable List<ItemStack> itemStacks, boolean allOrNothing, boolean filter)`
  - Executes `internal_addItemStacksOrdered` behavior.
- `testAddToExistingItemStacks(@Nonnull ItemContainer container, ItemStack itemStack, int itemMaxStack, int testQuantityRemaining, boolean filter)`
  - Executes `testAddToExistingItemStacks` behavior.
- `internal_removeItemStack(@Nonnull ItemContainer itemContainer, @Nonnull ItemStack itemStack, boolean allOrNothing, boolean filter)`
  - Executes `internal_removeItemStack` behavior.
- `internal_removeItemStacks(@Nonnull ItemContainer itemContainer, @Nullable List<ItemStack> itemStacks, boolean allOrNothing, boolean filter)`
  - Executes `internal_removeItemStacks` behavior.
- `testRemoveItemStackFromItems(@Nonnull ItemContainer container, ItemStack itemStack, int testQuantityRemaining, boolean filter)`
  - Executes `testRemoveItemStackFromItems` behavior.
- `testRemoveItemStackSlotFromItems(@Nonnull ItemContainer container, ItemStack itemStack, int testQuantityRemaining, boolean filter)`
  - Executes `testRemoveItemStackSlotFromItems` behavior.
- `testRemoveItemStackSlotFromItems(@Nonnull ItemContainer container, ItemStack itemStack, int testQuantityRemaining, boolean filter, BiPredicate<ItemStack, ItemStack> predicate)`
  - Executes `testRemoveItemStackSlotFromItems` behavior.

## Notes
- No additional notes.
