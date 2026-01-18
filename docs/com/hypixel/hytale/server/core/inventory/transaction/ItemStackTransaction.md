# ItemStackTransaction

## Overview
- Documentation for `ItemStackTransaction`.
- Declared as a class in `com.hypixel.hytale.server.core.inventory.transaction`.

## Constructors
- `ItemStackTransaction(false, ActionType.ADD, null, null, false, false, Collections.emptyList()`
  - Creates a `ItemStackTransaction` instance.
- `ItemStackTransaction(boolean succeeded, @Nullable ActionType action, @Nullable ItemStack query, @Nullable ItemStack remainder, boolean allOrNothing, boolean filter, @Nonnull List<ItemStackSlotTransaction> slotTransactions)`
  - Creates a `ItemStackTransaction` instance.
- `ItemStackTransaction(this.succeeded, this.action, this.query, this.remainder, this.allOrNothing, this.filter, slotTransactions)`
  - Creates a `ItemStackTransaction` instance.
- `ItemStackTransaction(succeeded, this.action, this.query, this.remainder, this.allOrNothing, this.filter, slotTransactions)`
  - Creates a `ItemStackTransaction` instance.

## Methods
- `succeeded()`
  - Executes `succeeded` behavior.
- `wasSlotModified(short slot)`
  - Executes `wasSlotModified` behavior.
- `getAction()`
  - Executes `getAction` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `getRemainder()`
  - Executes `getRemainder` behavior.
- `isAllOrNothing()`
  - Executes `isAllOrNothing` behavior.
- `isFilter()`
  - Executes `isFilter` behavior.
- `getSlotTransactions()`
  - Executes `getSlotTransactions` behavior.
- `toParent(ItemContainer parent, short start, ItemContainer container)`
  - Executes `toParent` behavior.
- `fromParent(ItemContainer parent, short start, @Nonnull ItemContainer container)`
  - Executes `fromParent` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
