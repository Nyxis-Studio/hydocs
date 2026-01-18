# ItemStackSlotTransaction

## Overview
- Documentation for `ItemStackSlotTransaction`.
- Declared as a class in `com.hypixel.hytale.server.core.inventory.transaction`.

## Constructors
- `ItemStackSlotTransaction(boolean succeeded, @Nonnull ActionType action, short slot, @Nullable ItemStack slotBefore, @Nullable ItemStack slotAfter, @Nullable ItemStack output, boolean allOrNothing, boolean exactAmount, boolean filter, boolean addToExistingSlot, @Nullable ItemStack query, @Nullable ItemStack remainder)`
  - Creates a `ItemStackSlotTransaction` instance.
- `ItemStackSlotTransaction(this.succeeded()`
  - Creates a `ItemStackSlotTransaction` instance.

## Methods
- `isAddToExistingSlot()`
  - Executes `isAddToExistingSlot` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `getRemainder()`
  - Executes `getRemainder` behavior.
- `toParent(ItemContainer parent, short start, ItemContainer container)`
  - Executes `toParent` behavior.
- `fromParent(ItemContainer parent, short start, @Nonnull ItemContainer container)`
  - Executes `fromParent` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
