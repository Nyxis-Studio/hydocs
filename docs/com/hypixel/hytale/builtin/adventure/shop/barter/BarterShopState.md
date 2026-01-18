**Source Hash:** `13025dbda4a20326c8b1a0f0c5e129d931cfe3dc1e93509cdcbd04770a0a4c1b`

# BarterShopState

## Overview

## Constructor Descriptions
- `BarterShopState()`
  - Creates a `BarterShopState` instance.

## Method Descriptions
- `initialize(@Nonnull Path dataDirectory)`: Add description.
  - Executes `initialize` behavior.
- `get()`: Add description.
  - Executes `get` behavior.
- `load()`: Add description.
  - Executes `load` behavior.
- `save()`: Add description.
  - Executes `save` behavior.
- `shutdown()`: Add description.
  - Executes `shutdown` behavior.
- `calculateNextScheduledRestock(@Nonnull Instant gameTime, int intervalDays, int restockHour)`: Add description.
  - Executes `calculateNextScheduledRestock` behavior.
- `getOrCreateShopState(BarterShopAsset asset, @Nonnull Instant gameTime)`: Add description.
  - Executes `getOrCreateShopState` behavior.
- `checkRefresh(BarterShopAsset asset, @Nonnull Instant gameTime)`: Add description.
  - Executes `checkRefresh` behavior.
- `getStockArray(BarterShopAsset asset, @Nonnull Instant gameTime)`: Add description.
  - Executes `getStockArray` behavior.
- `getResolvedTrades(BarterShopAsset asset, @Nonnull Instant gameTime)`: Add description.
  - Executes `getResolvedTrades` behavior.
- `executeTrade(BarterShopAsset asset, int tradeIndex, int quantity, @Nonnull Instant gameTime)`: Add description.
  - Executes `executeTrade` behavior.
- `getCurrentStock()`: Add description.
  - Executes `getCurrentStock` behavior.
- `getNextRefreshTime()`: Add description.
  - Executes `getNextRefreshTime` behavior.
- `setNextRefreshTime(Instant time)`: Add description.
  - Executes `setNextRefreshTime` behavior.
- `getResolveSeed()`: Add description.
  - Executes `getResolveSeed` behavior.
- `setResolveSeed(Long seed)`: Add description.
  - Executes `setResolveSeed` behavior.
- `getResolvedTrades(@Nonnull BarterShopAsset asset)`: Add description.
  - Executes `getResolvedTrades` behavior.
- `resolveTradeSlots(@Nonnull BarterShopAsset asset, long seed)`: Add description.
  - Executes `resolveTradeSlots` behavior.
- `resetStockAndResolve(@Nonnull BarterShopAsset asset)`: Add description.
  - Executes `resetStockAndResolve` behavior.
- `resetStock(BarterShopAsset asset)`: Add description.
  - Executes `resetStock` behavior.
- `expandStockIfNeeded(BarterShopAsset asset)`: Add description.
  - Executes `expandStockIfNeeded` behavior.
- `hasStock(int tradeIndex, int quantity)`: Add description.
  - Executes `hasStock` behavior.
- `decrementStock(int tradeIndex, int quantity)`: Add description.
  - Executes `decrementStock` behavior.
- `getStock(int tradeIndex)`: Add description.
  - Executes `getStock` behavior.

## Notes
- No additional notes.
