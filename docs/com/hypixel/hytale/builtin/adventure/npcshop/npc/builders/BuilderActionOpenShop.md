**Source Hash:** `a710ddaaab33ef15f07fc157e952553231c4e4cd962176c2c2bda4650172277e`
**Last Updated:** 2026-01-18T19:03:47-03:00

# BuilderActionOpenShop

## Overview
Builder action for NPC interactions that opens a regular shop interface for players. This class extends BuilderActionBase and provides the configuration and creation logic for opening standard shops through NPC interactions. Unlike barter shops, this handles traditional currency-based transactions.

## Field Descriptions
- `shopId`: Asset holder containing the reference to the shop to be opened. Protected final field that stores the shop identifier used during action execution.

## Constructor Descriptions
- `BuilderActionOpenShop()`: Creates a new builder instance for shop opening actions. Initializes the shopId asset holder for configuration.

## Method Descriptions
- `getShortDescription()`: Returns "Open the shop UI for the current player". Provides a brief description of what this action does when executed.
- `getLongDescription()`: Returns the same description as getShortDescription(). Currently identical to short description for this action type.
- `build(@Nonnull BuilderSupport builderSupport)`: Creates and returns a new ActionOpenShop instance configured with this builder and the provided support context. This is the main factory method for creating executable actions.
- `getBuilderDescriptorState()`: Returns BuilderDescriptorState.Stable, indicating this builder is ready for production use and has a stable API.
- `readConfig(@Nonnull JsonElement data)`: Configures the builder from JSON data, requiring a "Shop" asset reference validated by ShopExistsValidator. Also enforces that this action can only be used with Interaction instruction types.
- `getShopId(@Nonnull BuilderSupport support)`: Retrieves the configured shop ID from the asset holder using the provided execution context.

## Usage Notes
- This builder is for regular shops with traditional currency-based transactions, distinct from barter shops
- The shop asset must exist and be valid according to ShopExistsValidator before the action can be created
- Only supports Interaction instruction types - cannot be used with other NPC instruction types
- The shopId is resolved at execution time using the provided BuilderSupport context

## Examples
```java
// Configure a shop action in JSON
{
  "Shop": "village_general_store",
  "type": "open_shop"
}

// Access shop ID during execution
BuilderActionOpenShop builder = new BuilderActionOpenShop();
String shopId = builder.getShopId(builderSupport);
```
