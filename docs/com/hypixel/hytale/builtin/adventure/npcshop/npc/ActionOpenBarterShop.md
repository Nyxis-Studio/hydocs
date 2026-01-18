**Source Hash:** `ddadeee8ae64be059edce5b6c25bb3df65b2c7ae26647ca85a336405c6596f48`
**Last Updated:** 2026-01-18T18:54:44-03:00

# ActionOpenBarterShop

## Overview

NPC action component that opens a barter shop interface for players when they interact with an NPC. Provides a trading system where players can exchange items directly rather than using currency.

## Constructor Descriptions
- `ActionOpenBarterShop(@Nonnull BuilderActionOpenBarterShop builder, @Nonnull BuilderSupport support)`
  - Creates a `ActionOpenBarterShop` instance with the specified shop configuration.
  - Extracts the shop ID from the builder for later use when opening the shop interface.

## Field Descriptions
- `shopId`: The identifier of the barter shop to open.

## Method Descriptions
- `canExecute(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, InfoProvider sensorInfo, double dt, @Nonnull Store<EntityStore> store)`: Determines if the barter shop can be opened.
  - Returns `true` if the base action can execute and there is an interaction target (player) available.
- `execute(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, InfoProvider sensorInfo, double dt, @Nonnull Store<EntityStore> store)`: Opens the barter shop interface.
  - Validates that an interaction target exists and has valid player components.
  - Opens a `BarterPage` for the target player using their page manager.
  - Returns `true` if successful, `false` if any validation fails.

## Notes
- Extends `ActionBase` for standard NPC action behavior.
- Requires a valid player interaction target to execute.
- Uses the player's page manager to open the barter trading interface.
