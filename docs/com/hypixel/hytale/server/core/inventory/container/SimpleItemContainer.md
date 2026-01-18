**Source Hash:** `2b102e8e93b6d0b610a0a4b0b1d8db845b2ddd44202b9c04b3d50f7bec1bd7aa`

# SimpleItemContainer

## Overview

## Constructor Descriptions
- `SimpleItemContainer()`
  - Creates a `SimpleItemContainer` instance.
- `SimpleItemContainer(short capacity)`
  - Creates a `SimpleItemContainer` instance.
- `SimpleItemContainer(@Nonnull SimpleItemContainer other)`
  - Creates a `SimpleItemContainer` instance.
- `SimpleItemContainer(this)`
  - Creates a `SimpleItemContainer` instance.

## Method Descriptions
- `readAction(@Nonnull Supplier<V> action)`: Add description.
  - Executes `readAction` behavior.
- `readAction(@Nonnull Function<X, V> action, X x)`: Add description.
  - Executes `readAction` behavior.
- `writeAction(@Nonnull Supplier<V> action)`: Add description.
  - Executes `writeAction` behavior.
- `writeAction(@Nonnull Function<X, V> action, X x)`: Add description.
  - Executes `writeAction` behavior.
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
- `getCapacity()`: Add description.
  - Executes `getCapacity` behavior.
- `internal_clear()`: Add description.
  - Executes `internal_clear` behavior.
- `clone()`: Add description.
  - Executes `clone` behavior.
- `isEmpty()`: Add description.
  - Executes `isEmpty` behavior.
- `setGlobalFilter(@Nonnull FilterType globalFilter)`: Add description.
  - Executes `setGlobalFilter` behavior.
- `setSlotFilter(FilterActionType actionType, short slot, @Nullable SlotFilter filter)`: Add description.
  - Executes `setSlotFilter` behavior.
- `getItemStack(short slot)`: Add description.
  - Executes `getItemStack` behavior.
- `equals(Object o)`: Add description.
  - Executes `equals` behavior.
- `hashCode()`: Add description.
  - Executes `hashCode` behavior.
- `getNewContainer(short capacity)`: Add description.
  - Executes `getNewContainer` behavior.
- `addOrDropItemStack(@Nonnull ComponentAccessor<EntityStore> store, @Nonnull Ref<EntityStore> ref, @Nonnull ItemContainer itemContainer, @Nonnull ItemStack itemStack)`: Add description.
  - Executes `addOrDropItemStack` behavior.
- `addOrDropItemStack(@Nonnull ComponentAccessor<EntityStore> store, @Nonnull Ref<EntityStore> ref, @Nonnull ItemContainer itemContainer, short slot, @Nonnull ItemStack itemStack)`: Add description.
  - Executes `addOrDropItemStack` behavior.
- `addOrDropItemStacks(@Nonnull ComponentAccessor<EntityStore> store, @Nonnull Ref<EntityStore> ref, @Nonnull ItemContainer itemContainer, List<ItemStack> itemStacks)`: Add description.
  - Executes `addOrDropItemStacks` behavior.
- `tryAddOrderedOrDropItemStacks(@Nonnull ComponentAccessor<EntityStore> store, @Nonnull Ref<EntityStore> ref, @Nonnull ItemContainer itemContainer, List<ItemStack> itemStacks)`: Add description.
  - Executes `tryAddOrderedOrDropItemStacks` behavior.

## Notes
- No additional notes.
