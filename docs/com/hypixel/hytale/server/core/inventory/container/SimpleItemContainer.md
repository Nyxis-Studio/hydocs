# SimpleItemContainer

## Overview
- Documentation for `SimpleItemContainer`.
- Declared as a class in `com.hypixel.hytale.server.core.inventory.container`.

## Constructors
- `SimpleItemContainer()`
  - Creates a `SimpleItemContainer` instance.
- `SimpleItemContainer(short capacity)`
  - Creates a `SimpleItemContainer` instance.
- `SimpleItemContainer(@Nonnull SimpleItemContainer other)`
  - Creates a `SimpleItemContainer` instance.
- `SimpleItemContainer(this)`
  - Creates a `SimpleItemContainer` instance.

## Methods
- `readAction(@Nonnull Supplier<V> action)`
  - Executes `readAction` behavior.
- `readAction(@Nonnull Function<X, V> action, X x)`
  - Executes `readAction` behavior.
- `writeAction(@Nonnull Supplier<V> action)`
  - Executes `writeAction` behavior.
- `writeAction(@Nonnull Function<X, V> action, X x)`
  - Executes `writeAction` behavior.
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
- `internal_clear()`
  - Executes `internal_clear` behavior.
- `clone()`
  - Executes `clone` behavior.
- `isEmpty()`
  - Executes `isEmpty` behavior.
- `setGlobalFilter(@Nonnull FilterType globalFilter)`
  - Executes `setGlobalFilter` behavior.
- `setSlotFilter(FilterActionType actionType, short slot, @Nullable SlotFilter filter)`
  - Executes `setSlotFilter` behavior.
- `getItemStack(short slot)`
  - Executes `getItemStack` behavior.
- `equals(Object o)`
  - Executes `equals` behavior.
- `hashCode()`
  - Executes `hashCode` behavior.
- `getNewContainer(short capacity)`
  - Executes `getNewContainer` behavior.
- `addOrDropItemStack(@Nonnull ComponentAccessor<EntityStore> store, @Nonnull Ref<EntityStore> ref, @Nonnull ItemContainer itemContainer, @Nonnull ItemStack itemStack)`
  - Executes `addOrDropItemStack` behavior.
- `addOrDropItemStack(@Nonnull ComponentAccessor<EntityStore> store, @Nonnull Ref<EntityStore> ref, @Nonnull ItemContainer itemContainer, short slot, @Nonnull ItemStack itemStack)`
  - Executes `addOrDropItemStack` behavior.
- `addOrDropItemStacks(@Nonnull ComponentAccessor<EntityStore> store, @Nonnull Ref<EntityStore> ref, @Nonnull ItemContainer itemContainer, List<ItemStack> itemStacks)`
  - Executes `addOrDropItemStacks` behavior.
- `tryAddOrderedOrDropItemStacks(@Nonnull ComponentAccessor<EntityStore> store, @Nonnull Ref<EntityStore> ref, @Nonnull ItemContainer itemContainer, List<ItemStack> itemStacks)`
  - Executes `tryAddOrderedOrDropItemStacks` behavior.

## Notes
- No additional notes.
