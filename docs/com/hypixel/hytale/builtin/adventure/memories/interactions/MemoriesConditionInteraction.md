**Source Hash:** `983ed1887a743ecd972ff3143e95339370b261c54f8f33ac8ccfce2ef0072de0`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# MemoriesConditionInteraction

## Overview
Interaction that branches based on the player's current memories level. Resolves which child interaction to run by matching the level against configured keys and executes a fallback when none match.

## Field Descriptions
- `CODEC`: Builder codec for level-to-interaction mappings and failure path.
- `TAG_FAILED`: Collector tag used when walking the failure branch.
- `next`: Map of memory level to child interaction IDs.
- `sortedKeys`: Sorted list of configured level keys for deterministic branching.
- `levelToLabel`: Lookup map for label indices by level.
- `failed`: Optional fallback interaction ID when no level matches.

## Constructor Descriptions
- `MemoriesConditionInteraction()`: Creates the interaction instance used by the codec.

## Method Descriptions
- `tick0(boolean firstRun, float time, InteractionType type, InteractionContext context, CooldownHandler cooldownHandler)`: Evaluates memories level and jumps to the matching label or failure label.
- `simulateTick0(boolean firstRun, float time, InteractionType type, InteractionContext context, CooldownHandler cooldownHandler)`: Simulates the same branching using cached server state.
- `compile(OperationsBuilder builder)`: Emits operations for each level branch plus a fallback branch.
- `generatePacket()`: Creates the protocol packet for client sync.
- `configurePacket(Interaction packet)`: Encodes level-to-interaction mappings into the packet.
- `walk(Collector collector, InteractionContext context)`: Walks child interactions for collection and validation.
- `needsRemoteSync()`: Returns `false` because this interaction is server-only.
- `getWaitForDataFrom()`: Requires server data before execution.

## Usage Notes
- Level keys are sorted so the label indices remain stable across executions.

## Examples
```java
MemoriesConditionInteraction interaction = new MemoriesConditionInteraction();
```
