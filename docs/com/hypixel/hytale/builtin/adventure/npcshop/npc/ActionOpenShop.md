**Source Hash:** `08f4555fbcd840fe3ea6ee23a3c9f81ba74b114d19746d9a8782c3d532fe104d`
**Last Updated:** 2026-01-18T18:54:44-03:00

# ActionOpenShop

## Overview

NPC action component that opens a standard shop interface for players when they interact with an NPC. Provides a traditional shop system where players can purchase items using currency.

## Constructor Descriptions
- `ActionOpenShop(@Nonnull BuilderActionOpenShop builder, @Nonnull BuilderSupport support)`
  - Creates a `ActionOpenShop` instance with the specified shop configuration.
  - Extracts the shop ID from the builder for later use when opening the shop interface.

## Field Descriptions
- `shopId`: The identifier of the shop to open.

## Method Descriptions
- `canExecute(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, InfoProvider sensorInfo, double dt, @Nonnull Store<EntityStore> store)`: Determines if the shop can be opened.
  - Returns `true` if the base action can execute and there is an interaction target (player) available.
- `execute(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, InfoProvider sensorInfo, double dt, @Nonnull Store<EntityStore> store)`: Opens the shop interface.
  - Validates that an interaction target exists.
  - Asserts that the player has valid PlayerRef and Player components.
  - Opens a `ShopPage` for the target player using their page manager.
  - Returns `true` upon successful execution.

## Notes
- Extends `ActionBase` for standard NPC action behavior.
- Requires a valid player interaction target to execute.
- Uses assertions for player component validation, indicating these should not fail under normal conditions.
- Differs from `ActionOpenBarterShop` by using currency-based transactions instead of item exchanges.
