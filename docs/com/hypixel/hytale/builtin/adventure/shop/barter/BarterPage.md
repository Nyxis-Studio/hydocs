# BarterPage

## Overview
- Documentation for `BarterPage`.
- Declared as a class in `com.hypixel.hytale.builtin.adventure.shop.barter`.

## Constructors
- `BarterPage(@Nonnull PlayerRef playerRef, @Nonnull String shopId)`
  - Creates a `BarterPage` instance.

## Methods
- `isTradeValid(BarterTrade trade)`
  - Executes `isTradeValid` behavior.
- `getSafeItemId(String itemId)`
  - Executes `getSafeItemId` behavior.
- `build(@Nonnull Ref<EntityStore> ref, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder, @Nonnull Store<EntityStore> store)`
  - Executes `build` behavior.
- `handleDataEvent(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull BarterEventData data)`
  - Executes `handleDataEvent` behavior.
- `updateAfterTrade(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, int tradedIndex)`
  - Executes `updateAfterTrade` behavior.
- `countItemsInContainer(ItemContainer container, String itemId)`
  - Executes `countItemsInContainer` behavior.
- `removeItemsFromContainer(ItemContainer container, String itemId, int amount)`
  - Executes `removeItemsFromContainer` behavior.
- `refreshUI(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store)`
  - Executes `refreshUI` behavior.
- `getRefreshTimerText(BarterShopState barterState, Instant gameTime)`
  - Executes `getRefreshTimerText` behavior.
- `getTradeIndex()`
  - Executes `getTradeIndex` behavior.
- `getQuantity()`
  - Executes `getQuantity` behavior.
- `isShiftHeld()`
  - Executes `isShiftHeld` behavior.

## Notes
- No additional notes.
