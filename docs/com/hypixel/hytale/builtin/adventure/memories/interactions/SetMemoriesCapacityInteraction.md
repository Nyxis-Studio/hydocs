**Source Hash:** `7ea07f94efaca2c6c47c712d608679f64c3799e729f56a15a5d01ef1897887ad`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# SetMemoriesCapacityInteraction

## Overview
Instant interaction that increases a player's memories capacity and unlocks the feature if it was previously disabled. Sends feature status updates and notifications when unlocking for the first time.

## Field Descriptions
- `CODEC`: Builder codec for the capacity setting.
- `capacity`: Target capacity to set for the player.

## Constructor Descriptions
- `SetMemoriesCapacityInteraction()`: Creates the interaction instance used by the codec.

## Method Descriptions
- `firstRun(InteractionType type, InteractionContext context, CooldownHandler cooldownHandler)`: Updates player capacity, sends unlock notifications, and sets the interaction state.
- `getWaitForDataFrom()`: Requires server data before execution.
- `toString()`: Returns the base interaction string.

## Usage Notes
- The interaction fails if the requested capacity is not higher than the current capacity.

## Examples
```java
SetMemoriesCapacityInteraction interaction = new SetMemoriesCapacityInteraction();
```
