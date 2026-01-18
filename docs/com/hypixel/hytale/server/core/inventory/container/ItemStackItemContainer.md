# ItemStackItemContainer

## Overview
- Documentation for `ItemStackItemContainer`.
- Declared as a class in `com.hypixel.hytale.server.core.inventory.container`.

## Constructors
- `ItemStackItemContainer(ItemContainer parentContainer, short itemStackSlot, ItemStack originalItemStack, short capacity, ItemStack[] items)`
  - Creates a `ItemStackItemContainer` instance.
- `ItemStackItemContainer(itemContainer, slot, itemStack, capacity, items)`
  - Creates a `ItemStackItemContainer` instance.
- `ItemStackItemContainer(itemContainer, slot, itemStack, capacity, new ItemStack[capacity])`
  - Creates a `ItemStackItemContainer` instance.

## Methods
- `getParentContainer()`
  - Executes `getParentContainer` behavior.
- `getItemStackSlot()`
  - Executes `getItemStackSlot` behavior.
- `getOriginalItemStack()`
  - Executes `getOriginalItemStack` behavior.
- `isItemStackValid()`
  - Executes `isItemStackValid` behavior.
- `getCapacity()`
  - Executes `getCapacity` behavior.
- `setGlobalFilter(@Nonnull FilterType globalFilter)`
  - Executes `setGlobalFilter` behavior.
- `setSlotFilter(FilterActionType actionType, short slot, @Nullable SlotFilter filter)`
  - Executes `setSlotFilter` behavior.
- `clone()`
  - Executes `clone` behavior.
- `readAction(@Nonnull Supplier<V> action)`
  - Executes `readAction` behavior.
- `readAction(@Nonnull Function<X, V> action, X x)`
  - Executes `readAction` behavior.
- `writeAction(@Nonnull Supplier<V> action)`
  - Executes `writeAction` behavior.
- `writeAction(@Nonnull Function<X, V> action, X x)`
  - Executes `writeAction` behavior.
- `isEmpty()`
  - Executes `isEmpty` behavior.
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
- `getItemStack(short slot)`
  - Executes `getItemStack` behavior.
- `writeToItemStack(@Nonnull ItemContainer itemContainer, short slot, ItemStack originalItemStack, ItemStack[] items)`
  - Executes `writeToItemStack` behavior.
- `getContainer(@Nonnull ItemContainer itemContainer, short slot)`
  - Executes `getContainer` behavior.
- `makeContainerWithCapacity(@Nonnull ItemContainer itemContainer, short slot, short capacity)`
  - Executes `makeContainerWithCapacity` behavior.
- `ensureContainer(@Nonnull ItemContainer itemContainer, short slot, short capacity)`
  - Executes `ensureContainer` behavior.
- `ensureConfiguredContainer(@Nonnull ItemContainer itemContainer, short slot, @Nonnull ItemStackContainerConfig config)`
  - Executes `ensureConfiguredContainer` behavior.

## Notes
- No additional notes.
