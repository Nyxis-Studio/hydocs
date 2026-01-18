**Source Hash:** `61b65d325875ba15a33d53b78476c3cdfa6ed9e2afcbabb5984af2c9f31a83a2`

# ItemStackItemContainer

## Overview

## Constructor Descriptions
- `ItemStackItemContainer(ItemContainer parentContainer, short itemStackSlot, ItemStack originalItemStack, short capacity, ItemStack[] items)`
  - Creates a `ItemStackItemContainer` instance.
- `ItemStackItemContainer(itemContainer, slot, itemStack, capacity, items)`
  - Creates a `ItemStackItemContainer` instance.
- `ItemStackItemContainer(itemContainer, slot, itemStack, capacity, new ItemStack[capacity])`
  - Creates a `ItemStackItemContainer` instance.

## Method Descriptions
- `getParentContainer()`: Add description.
  - Executes `getParentContainer` behavior.
- `getItemStackSlot()`: Add description.
  - Executes `getItemStackSlot` behavior.
- `getOriginalItemStack()`: Add description.
  - Executes `getOriginalItemStack` behavior.
- `isItemStackValid()`: Add description.
  - Executes `isItemStackValid` behavior.
- `getCapacity()`: Add description.
  - Executes `getCapacity` behavior.
- `setGlobalFilter(@Nonnull FilterType globalFilter)`: Add description.
  - Executes `setGlobalFilter` behavior.
- `setSlotFilter(FilterActionType actionType, short slot, @Nullable SlotFilter filter)`: Add description.
  - Executes `setSlotFilter` behavior.
- `clone()`: Add description.
  - Executes `clone` behavior.
- `readAction(@Nonnull Supplier<V> action)`: Add description.
  - Executes `readAction` behavior.
- `readAction(@Nonnull Function<X, V> action, X x)`: Add description.
  - Executes `readAction` behavior.
- `writeAction(@Nonnull Supplier<V> action)`: Add description.
  - Executes `writeAction` behavior.
- `writeAction(@Nonnull Function<X, V> action, X x)`: Add description.
  - Executes `writeAction` behavior.
- `isEmpty()`: Add description.
  - Executes `isEmpty` behavior.
- `internal_clear()`: Add description.
  - Executes `internal_clear` behavior.
- `internal_getSlot(short slot)`: Add description.
  - Executes `internal_getSlot` behavior.
- `internal_setSlot(short slot, ItemStack itemStack)`: Add description.
  - Executes `internal_setSlot` behavior.
- `internal_removeSlot(short slot)`: Add description.
  - Executes `internal_removeSlot` behavior.
- `cantAddToSlot(short slot, ItemStack itemStack, ItemStack slotItemStack)`: Add description.
  - Executes `cantAddToSlot` behavior.
- `cantRemoveFromSlot(short slot)`: Add description.
  - Executes `cantRemoveFromSlot` behavior.
- `cantDropFromSlot(short slot)`: Add description.
  - Executes `cantDropFromSlot` behavior.
- `cantMoveToSlot(ItemContainer fromContainer, short slotFrom)`: Add description.
  - Executes `cantMoveToSlot` behavior.
- `testFilter(FilterActionType actionType, short slot, ItemStack itemStack)`: Add description.
  - Executes `testFilter` behavior.
- `getItemStack(short slot)`: Add description.
  - Executes `getItemStack` behavior.
- `writeToItemStack(@Nonnull ItemContainer itemContainer, short slot, ItemStack originalItemStack, ItemStack[] items)`: Add description.
  - Executes `writeToItemStack` behavior.
- `getContainer(@Nonnull ItemContainer itemContainer, short slot)`: Add description.
  - Executes `getContainer` behavior.
- `makeContainerWithCapacity(@Nonnull ItemContainer itemContainer, short slot, short capacity)`: Add description.
  - Executes `makeContainerWithCapacity` behavior.
- `ensureContainer(@Nonnull ItemContainer itemContainer, short slot, short capacity)`: Add description.
  - Executes `ensureContainer` behavior.
- `ensureConfiguredContainer(@Nonnull ItemContainer itemContainer, short slot, @Nonnull ItemStackContainerConfig config)`: Add description.
  - Executes `ensureConfiguredContainer` behavior.

## Notes
- No additional notes.
