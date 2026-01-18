**Source Hash:** `411b5cf76b91c39bc777614b89239211e2eb195cc6a158bd3ab2d35130b9a537`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# ChangeFarmingStageInteraction

## Overview
Interaction that changes the current farming stage of a block. Supports absolute stage setting and relative increase/decrease logic.

## Field Descriptions
- `LOGGER`: Logger for stage-change debugging.
- `CODEC`: Builder codec for stage-change interactions.
- `targetStage`: Absolute stage index to set (-1 means final stage).
- `increaseBy`: Optional amount to add to the current stage.
- `decreaseBy`: Optional amount to subtract from the current stage.
- `targetStageSet`: Optional stage set name to switch to.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `getWaitForDataFrom()`: Returns `WaitForDataFrom.Server`.
- `interactWithBlock(World world, CommandBuffer<EntityStore> commandBuffer, InteractionType type, InteractionContext context, ItemStack itemInHand, Vector3i targetBlock, CooldownHandler cooldownHandler)`: Resolves or creates the farming block entity, computes the target stage, applies the stage, schedules a tick, and updates ticking state.
- `simulateInteractWithBlock(InteractionType type, InteractionContext context, ItemStack itemInHand, World world, Vector3i targetBlock)`: No-op simulation.
- `toString()`: Returns a diagnostic string.

## Usage Notes
- Creates a new farming block entity when none exists at the target position.
- Emits detailed debug logs for each stage decision.

## Examples
```java
ChangeFarmingStageInteraction interaction = ChangeFarmingStageInteraction.CODEC.decode(reader, extraInfo);
```
