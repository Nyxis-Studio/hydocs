# CombinedItemContainer

## Overview
- Documentation for `CombinedItemContainer`.
- Declared as a class in `com.hypixel.hytale.server.core.inventory.container`.

## Constructors
- `CombinedItemContainer(ItemContainer ... containers)`
  - Creates a `CombinedItemContainer` instance.

## Methods
- `getContainer(int index)`
  - Executes `getContainer` behavior.
- `getContainersSize()`
  - Executes `getContainersSize` behavior.
- `getContainerForSlot(short slot)`
  - Executes `getContainerForSlot` behavior.
- `readAction(@Nonnull Supplier<V> action)`
  - Executes `readAction` behavior.
- `readAction0(int i, @Nonnull Supplier<V> action)`
  - Executes `readAction0` behavior.
- `readAction(@Nonnull Function<X, V> action, X x)`
  - Executes `readAction` behavior.
- `readAction0(int i, @Nonnull Function<X, V> action, X x)`
  - Executes `readAction0` behavior.
- `writeAction(@Nonnull Supplier<V> action)`
  - Executes `writeAction` behavior.
- `writeAction0(int i, @Nonnull Supplier<V> action)`
  - Executes `writeAction0` behavior.
- `writeAction(@Nonnull Function<X, V> action, X x)`
  - Executes `writeAction` behavior.
- `writeAction0(int i, @Nonnull Function<X, V> action, X x)`
  - Executes `writeAction0` behavior.
- `internal_clear()`
  - Executes `internal_clear` behavior.
- `internal_getSlot(short slot)`
  - Executes `internal_getSlot` behavior.
- `internal_setSlot(short slot, ItemStack itemStack)`
  - Executes `internal_setSlot` behavior.
- `internal_removeSlot(short slot)`
  - Executes `internal_removeSlot` behavior.
- `cantAddToSlot(short slot, ItemStack itemStack, ItemStack slotItemStack)`
  - Executes `cantAddToSlot` behavior.
- `cantRemoveFromSlot(short slot)`
  - Executes `cantRemoveFromSlot` behavior.
- `cantDropFromSlot(short slot)`
  - Executes `cantDropFromSlot` behavior.
- `cantMoveToSlot(ItemContainer fromContainer, short slotFrom)`
  - Executes `cantMoveToSlot` behavior.
- `getCapacity()`
  - Executes `getCapacity` behavior.
- `clone()`
  - Executes `clone` behavior.
- `registerChangeEvent(short priority, @Nonnull Consumer<ItemContainer.ItemContainerChangeEvent> consumer)`
  - Executes `registerChangeEvent` behavior.
- `sendUpdate(@Nonnull Transaction transaction)`
  - Executes `sendUpdate` behavior.
- `containsContainer(ItemContainer itemContainer)`
  - Executes `containsContainer` behavior.
- `equals(Object o)`
  - Executes `equals` behavior.
- `hashCode()`
  - Executes `hashCode` behavior.
- `setGlobalFilter(FilterType globalFilter)`
  - Executes `setGlobalFilter` behavior.
- `setSlotFilter(FilterActionType actionType, short slot, SlotFilter filter)`
  - Executes `setSlotFilter` behavior.

## Notes
- No additional notes.
