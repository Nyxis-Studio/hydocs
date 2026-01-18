**Source Hash:** `d30f1e10407f8cd7d5eee6df19b9ac78a3e5b3498960099462afe7be6b05fccc`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# FarmingSystems

## Overview
Collection of farming-related systems for soil, crops, and coop entities. Handles tick updates, state migration, and coop resident lifecycle.

## Field Descriptions
- `none`: Container class for nested farming systems.

## Constructor Descriptions
- None. Container class for nested systems.

## Method Descriptions
- `updateSoilDecayTime(CommandBuffer<ChunkStore> commandBuffer, TilledSoilBlock soilBlock, BlockType blockType)`: Computes and stores a randomized decay time based on soil config lifetime; returns whether a decay time was set.

## Usage Notes
- Includes nested systems: `MigrateFarming`, `CoopResidentTicking`, `CoopResidentEntitySystem`, `OnCoopAdded`, `Ticking`, `OnFarmBlockAdded`, `OnSoilAdded`.

## Examples
```java
storeRegistry.registerSystem(new FarmingSystems.Ticking());
```

---

# FarmingSystems.MigrateFarming

## Overview
Migration system that converts legacy `FarmingBlockState` into `FarmingBlock` components.

## Method Descriptions
- `onEntityAdd(Holder<ChunkStore> holder, AddReason reason, Store<ChunkStore> store)`: Copies growth progress, stage set, and spread rate into a new `FarmingBlock` and removes the legacy component.
- `onEntityRemoved(Holder<ChunkStore> holder, RemoveReason reason, Store<ChunkStore> store)`: No-op.
- `getQuery()`: Returns the query for legacy farming state components.

## Usage Notes
- Marked deprecated for removal.

---

# FarmingSystems.CoopResidentTicking

## Overview
Entity tick system that despawns coop residents when flagged.

## Method Descriptions
- `getQuery()`: Targets entities with `CoopResidentComponent`.
- `tick(float dt, int index, ArchetypeChunk<EntityStore> archetypeChunk, Store<EntityStore> store, CommandBuffer<EntityStore> commandBuffer)`: Removes entities marked for despawn.

---

# FarmingSystems.CoopResidentEntitySystem

## Overview
Handles coop resident cleanup when entities are removed.

## Method Descriptions
- `getQuery()`: Targets entities with `CoopResidentComponent`.
- `onEntityAdded(Ref<EntityStore> ref, AddReason reason, Store<EntityStore> store, CommandBuffer<EntityStore> commandBuffer)`: No-op.
- `onEntityRemove(Ref<EntityStore> ref, RemoveReason reason, Store<EntityStore> store, CommandBuffer<EntityStore> commandBuffer)`: Updates coop records for residents removed outside of unload.

---

# FarmingSystems.OnCoopAdded

## Overview
Schedules coop ticks and handles coop block removal cleanup.

## Method Descriptions
- `onEntityAdded(Ref<ChunkStore> ref, AddReason reason, Store<ChunkStore> store, CommandBuffer<ChunkStore> commandBuffer)`: Schedules the first coop tick based on the coop asset timing.
- `onEntityRemove(Ref<ChunkStore> ref, RemoveReason reason, Store<ChunkStore> store, CommandBuffer<ChunkStore> commandBuffer)`: Handles coop block removal by delegating to `CoopBlock.handleBlockBroken`.
- `getQuery()`: Returns the coop block query.

---

# FarmingSystems.Ticking

## Overview
Tick system that updates crops, soil decay, and coop behavior.

## Method Descriptions
- `tick(float dt, int index, ArchetypeChunk<ChunkStore> archetypeChunk, Store<ChunkStore> store, CommandBuffer<ChunkStore> commandBuffer)`: Runs per-block ticking logic for farming blocks, soil, and coops.

---

# FarmingSystems.OnFarmBlockAdded

## Overview
Initializes farming block state when crops are added.

## Method Descriptions
- `onEntityAdded(Ref<ChunkStore> ref, AddReason reason, Store<ChunkStore> store, CommandBuffer<ChunkStore> commandBuffer)`: Initializes stage set/progress, applies the starting stage if needed, and schedules a tick.
- `onEntityRemove(Ref<ChunkStore> ref, RemoveReason reason, Store<ChunkStore> store, CommandBuffer<ChunkStore> commandBuffer)`: No-op.
- `getQuery()`: Returns the farming block query.

---

# FarmingSystems.OnSoilAdded

## Overview
Schedules decay ticks for tilled soil blocks.

## Method Descriptions
- `onEntityAdded(Ref<ChunkStore> ref, AddReason reason, Store<ChunkStore> store, CommandBuffer<ChunkStore> commandBuffer)`: Computes decay time and schedules soil decay ticks when unplanted.
- `onEntityRemove(Ref<ChunkStore> ref, RemoveReason reason, Store<ChunkStore> store, CommandBuffer<ChunkStore> commandBuffer)`: No-op.
- `getQuery()`: Returns the tilled soil query.
