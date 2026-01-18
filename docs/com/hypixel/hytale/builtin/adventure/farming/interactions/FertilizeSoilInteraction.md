**Source Hash:** `00934a540f52352402a2dd56913e641619c695447c2f23adc2bf6421af45a41b`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# FertilizeSoilInteraction

## Overview
Interaction that fertilizes soil blocks or their supporting soil. Attempts to mark soil as fertilized and schedules tick updates.

## Field Descriptions
- `CODEC`: Builder codec for fertilize soil interactions.
- `refreshModifiers`: Modifier names to refresh after fertilization.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `getWaitForDataFrom()`: Returns `WaitForDataFrom.Server`.
- `interactWithBlock(World world, CommandBuffer<EntityStore> commandBuffer, InteractionType type, InteractionContext context, ItemStack itemInHand, Vector3i targetBlock, CooldownHandler cooldownHandler)`: Fertilizes the target soil (or soil beneath crops) and marks affected blocks for ticking.
- `simulateInteractWithBlock(InteractionType type, InteractionContext context, ItemStack itemInHand, World world, Vector3i targetBlock)`: No-op simulation.

## Usage Notes
- Returns failure when no soil entity is present or the soil is already fertilized.

## Examples
```java
FertilizeSoilInteraction interaction = FertilizeSoilInteraction.CODEC.decode(reader, extraInfo);
```
