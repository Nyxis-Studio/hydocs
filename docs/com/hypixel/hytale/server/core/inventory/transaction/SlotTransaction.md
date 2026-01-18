# SlotTransaction

## Overview
- Documentation for `SlotTransaction`.
- Declared as a class in `com.hypixel.hytale.server.core.inventory.transaction`.

## Constructors
- `SlotTransaction(false, ActionType.ADD, -1, null, null, null, false, false, false)`
  - Creates a `SlotTransaction` instance.
- `SlotTransaction(boolean succeeded, @Nonnull ActionType action, short slot, @Nullable ItemStack slotBefore, @Nullable ItemStack slotAfter, @Nullable ItemStack output, boolean allOrNothing, boolean exactAmount, boolean filter)`
  - Creates a `SlotTransaction` instance.
- `SlotTransaction(this.succeeded, this.action, newSlot, this.slotBefore, this.slotAfter, this.output, this.allOrNothing, this.exactAmount, this.filter)`
  - Creates a `SlotTransaction` instance.

## Methods
- `succeeded()`
  - Executes `succeeded` behavior.
- `wasSlotModified(short slot)`
  - Executes `wasSlotModified` behavior.
- `getAction()`
  - Executes `getAction` behavior.
- `getSlot()`
  - Executes `getSlot` behavior.
- `getSlotBefore()`
  - Executes `getSlotBefore` behavior.
- `getSlotAfter()`
  - Executes `getSlotAfter` behavior.
- `getOutput()`
  - Executes `getOutput` behavior.
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
