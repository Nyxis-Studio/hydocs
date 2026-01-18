# ClearTransaction

## Overview
- Documentation for `ClearTransaction`.
- Declared as a class in `com.hypixel.hytale.server.core.inventory.transaction`.

## Constructors
- `ClearTransaction(true, 0, ItemStack.EMPTY_ARRAY)`
  - Creates a `ClearTransaction` instance.
- `ClearTransaction(boolean succeeded, short start, @Nonnull ItemStack[] items)`
  - Creates a `ClearTransaction` instance.
- `ClearTransaction(this.succeeded, newStart, this.items)`
  - Creates a `ClearTransaction` instance.
- `ClearTransaction(this.succeeded, 0, Arrays.copyOfRange(this.items, (int)`
  - Creates a `ClearTransaction` instance.
- `ClearTransaction(this.succeeded, newStart, Arrays.copyOf(this.items, (int)`
  - Creates a `ClearTransaction` instance.

## Methods
- `succeeded()`
  - Executes `succeeded` behavior.
- `wasSlotModified(short slot)`
  - Executes `wasSlotModified` behavior.
- `getItems()`
  - Executes `getItems` behavior.
- `toParent(ItemContainer parent, short start, ItemContainer container)`
  - Executes `toParent` behavior.
- `fromParent(ItemContainer parent, short start, @Nonnull ItemContainer container)`
  - Executes `fromParent` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
