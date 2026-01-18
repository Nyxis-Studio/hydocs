# MaterialTransaction

## Overview
- Documentation for `MaterialTransaction`.
- Declared as a class in `com.hypixel.hytale.server.core.inventory.transaction`.

## Constructors
- `MaterialTransaction(boolean succeeded, @Nonnull ActionType action, @Nonnull MaterialQuantity material, int remainder, boolean allOrNothing, boolean exactAmount, boolean filter, @Nonnull List<MaterialSlotTransaction> slotTransactions)`
  - Creates a `MaterialTransaction` instance.
- `MaterialTransaction(this.succeeded()`
  - Creates a `MaterialTransaction` instance.
- `MaterialTransaction(succeeded, this.action, this.material, this.remainder, this.allOrNothing, this.exactAmount, this.filter, slotTransactions)`
  - Creates a `MaterialTransaction` instance.

## Methods
- `getAction()`
  - Executes `getAction` behavior.
- `getMaterial()`
  - Executes `getMaterial` behavior.
- `getRemainder()`
  - Executes `getRemainder` behavior.
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
