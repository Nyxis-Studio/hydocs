# ResourceTransaction

## Overview
- Documentation for `ResourceTransaction`.
- Declared as a class in `com.hypixel.hytale.server.core.inventory.transaction`.

## Constructors
- `ResourceTransaction(boolean succeeded, @Nonnull ActionType action, @Nonnull ResourceQuantity resource, int remainder, int consumed, boolean allOrNothing, boolean exactAmount, boolean filter, @Nonnull List<ResourceSlotTransaction> slotTransactions)`
  - Creates a `ResourceTransaction` instance.
- `ResourceTransaction(this.succeeded()`
  - Creates a `ResourceTransaction` instance.
- `ResourceTransaction(succeeded, this.action, this.resource, this.remainder, this.consumed, this.allOrNothing, this.exactAmount, this.filter, slotTransactions)`
  - Creates a `ResourceTransaction` instance.

## Methods
- `getAction()`
  - Executes `getAction` behavior.
- `getResource()`
  - Executes `getResource` behavior.
- `getRemainder()`
  - Executes `getRemainder` behavior.
- `getConsumed()`
  - Executes `getConsumed` behavior.
- `isAllOrNothing()`
  - Executes `isAllOrNothing` behavior.
- `isExactAmount()`
  - Executes `isExactAmount` behavior.
- `isFilter()`
  - Executes `isFilter` behavior.
- `toParent(ItemContainer parent, short start, ItemContainer container)`
  - Executes `toParent` behavior.
- `fromParent(ItemContainer parent, short start, @Nonnull ItemContainer container)`
  - Executes `fromParent` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
