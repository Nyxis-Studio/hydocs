# DelegateItemContainer

## Overview
- Documentation for `DelegateItemContainer`.
- Declared as a class in `com.hypixel.hytale.server.core.inventory.container`.

## Constructors
- `DelegateItemContainer(T delegate)`
  - Creates a `DelegateItemContainer` instance.

## Methods
- `getDelegate()`
  - Executes `getDelegate` behavior.
- `readAction(Supplier<V> action)`
  - Executes `readAction` behavior.
- `readAction(Function<X, V> action, X x)`
  - Executes `readAction` behavior.
- `writeAction(Supplier<V> action)`
  - Executes `writeAction` behavior.
- `writeAction(Function<X, V> action, X x)`
  - Executes `writeAction` behavior.
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
- `testFilter(FilterActionType actionType, short slot, ItemStack itemStack)`
  - Executes `testFilter` behavior.
- `getCapacity()`
  - Executes `getCapacity` behavior.
- `clear()`
  - Executes `clear` behavior.
- `clone()`
  - Executes `clone` behavior.
- `isEmpty()`
  - Executes `isEmpty` behavior.
- `setGlobalFilter(@Nonnull FilterType globalFilter)`
  - Executes `setGlobalFilter` behavior.
- `setSlotFilter(FilterActionType actionType, short slot, @Nullable SlotFilter filter)`
  - Executes `setSlotFilter` behavior.
- `registerChangeEvent(short priority, @Nonnull Consumer<ItemContainer.ItemContainerChangeEvent> consumer)`
  - Executes `registerChangeEvent` behavior.
- `sendUpdate(@Nonnull Transaction transaction)`
  - Executes `sendUpdate` behavior.
- `equals(@Nullable Object o)`
  - Executes `equals` behavior.
- `hashCode()`
  - Executes `hashCode` behavior.

## Notes
- No additional notes.
