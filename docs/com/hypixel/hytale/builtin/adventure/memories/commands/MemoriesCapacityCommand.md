**Source Hash:** `e11b0f02181058915bf966d897183c849d072e58c191e973d4b2e0115323e626`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# MemoriesCapacityCommand

## Overview
Player command that sets a player's memories capacity and toggles the feature. Removing capacity clears the component and updates the client feature status.

## Field Descriptions
- `capacityArg`: Required integer argument for the new capacity.

## Constructor Descriptions
- `MemoriesCapacityCommand()`: Registers the `capacity` subcommand and its argument.

## Method Descriptions
- `execute(CommandContext context, Store<EntityStore> store, Ref<EntityStore> ref, PlayerRef playerRef, World world)`: Sets the memories capacity, removing the component when capacity is zero or less and sending feature status packets.

## Usage Notes
- Setting capacity to zero or less disables memories for the player.

## Examples
```java
// /memories capacity 5
```
