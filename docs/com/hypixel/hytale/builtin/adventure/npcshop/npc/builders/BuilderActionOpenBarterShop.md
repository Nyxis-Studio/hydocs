**Source Hash:** `0ba47e164cc6336e37964d6d6c69b72ecc28425ea77fb2974eca15c5ee3ee871`
**Last Updated:** 2026-01-18T19:03:47-03:00

# BuilderActionOpenBarterShop

## Overview
Builder action for NPC interactions that opens a barter shop interface for players. This class extends BuilderActionBase and provides the configuration and creation logic for opening barter shops through NPC interactions. It validates shop existence and manages the shop asset reference.

## Field Descriptions
- `shopId`: Asset holder containing the reference to the barter shop to be opened. Protected final field that stores the shop identifier used during action execution.

## Constructor Descriptions
- `BuilderActionOpenBarterShop()`: Creates a new builder instance for barter shop opening actions. Initializes the shopId asset holder for configuration.

## Method Descriptions
- `getShortDescription()`: Returns "Open the barter shop UI for the current player". Provides a brief description of what this action does when executed.
- `getLongDescription()`: Returns the same description as getShortDescription(). Currently identical to short description for this action type.
- `build(@Nonnull BuilderSupport builderSupport)`: Creates and returns a new ActionOpenBarterShop instance configured with this builder and the provided support context. This is the main factory method for creating executable actions.
- `getBuilderDescriptorState()`: Returns BuilderDescriptorState.Stable, indicating this builder is ready for production use and has a stable API.
- `readConfig(@Nonnull JsonElement data)`: Configures the builder from JSON data, requiring a "Shop" asset reference validated by BarterShopExistsValidator. Also enforces that this action can only be used with Interaction instruction types.
- `getShopId(@Nonnull BuilderSupport support)`: Retrieves the configured shop ID from the asset holder using the provided execution context.

## Usage Notes
- This builder is specifically for barter shops, which differ from regular shops in their trading mechanisms
- The shop asset must exist and be valid according to BarterShopExistsValidator before the action can be created
- Only supports Interaction instruction types - cannot be used with other NPC instruction types
- The shopId is resolved at execution time using the provided BuilderSupport context

## Examples
```java
// Configure a barter shop action in JSON
{
  "Shop": "village_blacksmith_barter",
  "type": "open_barter_shop"
}

// Access shop ID during execution
BuilderActionOpenBarterShop builder = new BuilderActionOpenBarterShop();
String shopId = builder.getShopId(builderSupport);
```
