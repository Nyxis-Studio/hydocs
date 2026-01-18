**Source Hash:** `3c1d4fbb3827520bfba32c95cf7e2d90624a0c497b036a133b2b873596712f57`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# TempleRespawnPlayersSystem

## Overview
Delayed entity system that teleports players back to spawn if they fall below a configured Y level in the forgotten temple. Plays a configured respawn sound after teleporting.

## Field Descriptions
- `QUERY`: Query selecting player entities with transforms.

## Constructor Descriptions
- `TempleRespawnPlayersSystem()`: Creates the system with a one-second tick interval.

## Method Descriptions
- `tick(float dt, int index, ArchetypeChunk<EntityStore> archetypeChunk, Store<EntityStore> store, CommandBuffer<EntityStore> commandBuffer)`: Checks player Y position and teleports to spawn when below the threshold.
- `getQuery()`: Returns the player transform query.

## Usage Notes
- Requires `ForgottenTempleConfig` to be present in gameplay config or it does nothing.

## Examples
```java
TempleRespawnPlayersSystem system = new TempleRespawnPlayersSystem();
```
