**Source Hash:** `5b4dd09d48c0d6a0fdf11371d96777f72477b798661543e3e55674bc91528c8b`

# CombinedItemContainer

## Overview

## Constructor Descriptions
- `CombinedItemContainer(ItemContainer ... containers)`
  - Creates a `CombinedItemContainer` instance.

## Method Descriptions
- `getContainer(int index)`: Add description.
  - Executes `getContainer` behavior.
- `getContainersSize()`: Add description.
  - Executes `getContainersSize` behavior.
- `getContainerForSlot(short slot)`: Add description.
  - Executes `getContainerForSlot` behavior.
- `readAction(@Nonnull Supplier<V> action)`: Add description.
  - Executes `readAction` behavior.
- `readAction0(int i, @Nonnull Supplier<V> action)`: Add description.
  - Executes `readAction0` behavior.
- `readAction(@Nonnull Function<X, V> action, X x)`: Add description.
  - Executes `readAction` behavior.
- `readAction0(int i, @Nonnull Function<X, V> action, X x)`: Add description.
  - Executes `readAction0` behavior.
- `writeAction(@Nonnull Supplier<V> action)`: Add description.
  - Executes `writeAction` behavior.
- `writeAction0(int i, @Nonnull Supplier<V> action)`: Add description.
  - Executes `writeAction0` behavior.
- `writeAction(@Nonnull Function<X, V> action, X x)`: Add description.
  - Executes `writeAction` behavior.
- `writeAction0(int i, @Nonnull Function<X, V> action, X x)`: Add description.
  - Executes `writeAction0` behavior.
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
- `getCapacity()`: Add description.
  - Executes `getCapacity` behavior.
- `clone()`: Add description.
  - Executes `clone` behavior.
- `registerChangeEvent(short priority, @Nonnull Consumer<ItemContainer.ItemContainerChangeEvent> consumer)`: Add description.
  - Executes `registerChangeEvent` behavior.
- `sendUpdate(@Nonnull Transaction transaction)`: Add description.
  - Executes `sendUpdate` behavior.
- `containsContainer(ItemContainer itemContainer)`: Add description.
  - Executes `containsContainer` behavior.
- `equals(Object o)`: Add description.
  - Executes `equals` behavior.
- `hashCode()`: Add description.
  - Executes `hashCode` behavior.
- `setGlobalFilter(FilterType globalFilter)`: Add description.
  - Executes `setGlobalFilter` behavior.
- `setSlotFilter(FilterActionType actionType, short slot, SlotFilter filter)`: Add description.
  - Executes `setSlotFilter` behavior.

## Notes
- No additional notes.
