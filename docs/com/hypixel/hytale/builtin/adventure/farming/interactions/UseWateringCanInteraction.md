**Source Hash:** `c3ab8c2f7f60a6b0712a0da36e1cf46e23eef1a5a040a0f3a4b0bbc12a3604ba`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# UseWateringCanInteraction

## Overview
Waters tilled soil or crop blocks when a watering can is used. Applies a watered-until timestamp and schedules chunk ticks on the soil and adjacent block, failing when no valid soil block can be resolved.

## Field Descriptions
- `CODEC`: Builder codec that serializes the duration and refresh modifier configuration.
- `duration`: Number of seconds to keep the soil watered after interaction.
- `refreshModifiers`: Modifier IDs to refresh (stored but not used by the interaction logic).

## Constructor Descriptions
- `UseWateringCanInteraction()`: Creates the interaction instance used by the codec.

## Method Descriptions
- `getWaitForDataFrom()`: Requires server data before executing this interaction.
- `interactWithBlock(World world, CommandBuffer<EntityStore> commandBuffer, InteractionType type, InteractionContext context, ItemStack itemInHand, Vector3i targetBlock, CooldownHandler cooldownHandler)`: Ensures a block entity, updates soil watering time, schedules ticks, and marks failures when soil is missing.
- `simulateInteractWithBlock(InteractionType type, InteractionContext context, ItemStack itemInHand, World world, Vector3i targetBlock)`: No-op simulation on the client.

## Usage Notes
- If the target block is a farming block, the interaction waters the tilled soil directly beneath it.
- The interaction sets ticking on both the soil block and the block above to keep growth updates active.

## Examples
```java
UseWateringCanInteraction interaction = new UseWateringCanInteraction();
```
