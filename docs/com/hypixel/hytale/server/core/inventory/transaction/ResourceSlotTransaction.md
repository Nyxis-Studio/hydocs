# ResourceSlotTransaction

## Overview
- Documentation for `ResourceSlotTransaction`.
- Declared as a class in `com.hypixel.hytale.server.core.inventory.transaction`.

## Constructors
- `ResourceSlotTransaction(boolean succeeded, @Nonnull ActionType action, short slot, @Nullable ItemStack slotBefore, @Nullable ItemStack slotAfter, @Nullable ItemStack output, boolean allOrNothing, boolean exactAmount, boolean filter, @Nonnull ResourceQuantity query, int remainder, int consumed)`
  - Creates a `ResourceSlotTransaction` instance.
- `ResourceSlotTransaction(this.succeeded()`
  - Creates a `ResourceSlotTransaction` instance.

## Methods
- `getQuery()`
  - Executes `getQuery` behavior.
- `getRemainder()`
  - Executes `getRemainder` behavior.
- `getConsumed()`
  - Executes `getConsumed` behavior.
- `toParent(ItemContainer parent, short start, ItemContainer container)`
  - Executes `toParent` behavior.
- `fromParent(ItemContainer parent, short start, @Nonnull ItemContainer container)`
  - Executes `fromParent` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
