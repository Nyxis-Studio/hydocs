# EmptyItemContainer

## Overview
- Documentation for `EmptyItemContainer`.
- Declared as a class in `com.hypixel.hytale.server.core.inventory.container`.

## Constructors
- `EmptyItemContainer()`
  - Creates a `EmptyItemContainer` instance.

## Methods
- `getCapacity()`
  - Executes `getCapacity` behavior.
- `clear()`
  - Executes `clear` behavior.
- `forEach(ShortObjectConsumer<ItemStack> action)`
  - Executes `forEach` behavior.
- `readAction(@Nonnull Supplier<V> action)`
  - Executes `readAction` behavior.
- `readAction(@Nonnull Function<X, V> action, X x)`
  - Executes `readAction` behavior.
- `writeAction(@Nonnull Supplier<V> action)`
  - Executes `writeAction` behavior.
- `writeAction(@Nonnull Function<X, V> action, X x)`
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
- `removeAllItemStacks()`
  - Executes `removeAllItemStacks` behavior.
- `toProtocolMap()`
  - Executes `toProtocolMap` behavior.
- `clone()`
  - Executes `clone` behavior.
- `registerChangeEvent(short priority, Consumer<ItemContainer.ItemContainerChangeEvent> consumer)`
  - Executes `registerChangeEvent` behavior.
- `setGlobalFilter(FilterType globalFilter)`
  - Executes `setGlobalFilter` behavior.
- `setSlotFilter(FilterActionType actionType, short slot, SlotFilter filter)`
  - Executes `setSlotFilter` behavior.

## Notes
- No additional notes.
