# CameraEffectSystem

**Overview**
Damage event system that applies camera shake effects to players.
Computes intensity based on damage percentage and sends shake packets.

**Constructors**
- Uses the base system constructor; no explicit constructor defined.

**Methods**
- `getGroup()`: returns the damage inspection system group.
- `getQuery()`: returns the query for entities with player ref and stats.
- `handle(int index, ArchetypeChunk<EntityStore> archetypeChunk, Store<EntityStore> store, CommandBuffer<EntityStore> commandBuffer, Damage damage)`: resolves the camera effect and sends a shake packet.

**Notes**
- Uses `CameraEffectsConfig` to map damage causes to effect indices.
- Intensity is clamped based on damage amount versus max health.
