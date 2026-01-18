# BarterShopState

## Overview
- Documentation for `BarterShopState`.
- Declared as a class in `com.hypixel.hytale.builtin.adventure.shop.barter`.

## Constructors
- `BarterShopState()`
  - Creates a `BarterShopState` instance.

## Methods
- `initialize(@Nonnull Path dataDirectory)`
  - Executes `initialize` behavior.
- `get()`
  - Executes `get` behavior.
- `load()`
  - Executes `load` behavior.
- `save()`
  - Executes `save` behavior.
- `shutdown()`
  - Executes `shutdown` behavior.
- `calculateNextScheduledRestock(@Nonnull Instant gameTime, int intervalDays, int restockHour)`
  - Executes `calculateNextScheduledRestock` behavior.
- `getOrCreateShopState(BarterShopAsset asset, @Nonnull Instant gameTime)`
  - Executes `getOrCreateShopState` behavior.
- `checkRefresh(BarterShopAsset asset, @Nonnull Instant gameTime)`
  - Executes `checkRefresh` behavior.
- `getStockArray(BarterShopAsset asset, @Nonnull Instant gameTime)`
  - Executes `getStockArray` behavior.
- `getResolvedTrades(BarterShopAsset asset, @Nonnull Instant gameTime)`
  - Executes `getResolvedTrades` behavior.
- `executeTrade(BarterShopAsset asset, int tradeIndex, int quantity, @Nonnull Instant gameTime)`
  - Executes `executeTrade` behavior.
- `getCurrentStock()`
  - Executes `getCurrentStock` behavior.
- `getNextRefreshTime()`
  - Executes `getNextRefreshTime` behavior.
- `setNextRefreshTime(Instant time)`
  - Executes `setNextRefreshTime` behavior.
- `getResolveSeed()`
  - Executes `getResolveSeed` behavior.
- `setResolveSeed(Long seed)`
  - Executes `setResolveSeed` behavior.
- `getResolvedTrades(@Nonnull BarterShopAsset asset)`
  - Executes `getResolvedTrades` behavior.
- `resolveTradeSlots(@Nonnull BarterShopAsset asset, long seed)`
  - Executes `resolveTradeSlots` behavior.
- `resetStockAndResolve(@Nonnull BarterShopAsset asset)`
  - Executes `resetStockAndResolve` behavior.
- `resetStock(BarterShopAsset asset)`
  - Executes `resetStock` behavior.
- `expandStockIfNeeded(BarterShopAsset asset)`
  - Executes `expandStockIfNeeded` behavior.
- `hasStock(int tradeIndex, int quantity)`
  - Executes `hasStock` behavior.
- `decrementStock(int tradeIndex, int quantity)`
  - Executes `decrementStock` behavior.
- `getStock(int tradeIndex)`
  - Executes `getStock` behavior.

## Notes
- No additional notes.
