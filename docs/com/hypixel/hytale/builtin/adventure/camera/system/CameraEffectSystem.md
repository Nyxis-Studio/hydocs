**Source Hash:** `efca1d4de16e033c4b5a406e0ce46cc1f57a69e73be735513909542355ebbcab`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# CameraEffectSystem

## Overview
Damage event system that applies camera shake effects to players. Computes intensity based on damage percentage and sends shake packets.

## Field Descriptions
- `PLAYER_REF_COMPONENT_TYPE`: Component type for player references.
- `ENTITY_STAT_MAP_COMPONENT_TYPE`: Component type for entity stats.
- `QUERY`: Query matching entities with player ref and stats.

## Constructor Descriptions
- None. Uses the base system constructor.

## Method Descriptions
- `getGroup()`: Returns the damage inspection system group.
- `getQuery()`: Returns the query for entities with player ref and stats.
- `handle(int index, ArchetypeChunk<EntityStore> archetypeChunk, Store<EntityStore> store, CommandBuffer<EntityStore> commandBuffer, Damage damage)`: Resolves camera effects, clamps intensity based on damage vs max health, and sends the shake packet.

## Usage Notes
- Uses `CameraEffectsConfig` to map damage causes to effect indices when no explicit camera effect metadata is present.

## Examples
```java
systemRegistry.registerSystem(new CameraEffectSystem());
```
