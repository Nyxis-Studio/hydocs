# MoveTransaction

## Overview
- Documentation for `MoveTransaction`.
- Declared as a class in `com.hypixel.hytale.server.core.inventory.transaction`.

## Constructors
- `MoveTransaction(boolean succeeded, @Nonnull SlotTransaction removeTransaction, @Nonnull MoveType moveType, @Nonnull ItemContainer otherContainer, T addTransaction)`
  - Creates a `MoveTransaction` instance.

## Methods
- `succeeded()`
  - Executes `succeeded` behavior.
- `getRemoveTransaction()`
  - Executes `getRemoveTransaction` behavior.
- `getMoveType()`
  - Executes `getMoveType` behavior.
- `getOtherContainer()`
  - Executes `getOtherContainer` behavior.
- `getAddTransaction()`
  - Executes `getAddTransaction` behavior.
- `toInverted(@Nonnull ItemContainer itemContainer)`
  - Executes `toInverted` behavior.
- `wasSlotModified(short slot)`
  - Executes `wasSlotModified` behavior.
- `toParent(ItemContainer parent, short start, ItemContainer container)`
  - Executes `toParent` behavior.
- `fromParent(ItemContainer parent, short start, @Nonnull ItemContainer container)`
  - Executes `fromParent` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
