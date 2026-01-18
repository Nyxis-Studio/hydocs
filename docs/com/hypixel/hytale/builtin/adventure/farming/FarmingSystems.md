# FarmingSystems

**Overview**
Collection of farming-related systems for soil, crops, and coop entities.
Handles tick updates, state migration, and coop resident lifecycle.

**Constructors**
- Not applicable. Container class for nested systems.

**Methods**
- `updateSoilDecayTime(CommandBuffer<ChunkStore> commandBuffer, TilledSoilBlock soilBlock, BlockType blockType)`: computes and stores soil decay time.

**Notes**
- Includes nested systems: `MigrateFarming`, `CoopResidentTicking`, `CoopResidentEntitySystem`, `OnCoopAdded`, `Ticking`, `OnFarmBlockAdded`, `OnSoilAdded`.

---

# FarmingSystems.MigrateFarming

**Overview**
Migration system that converts legacy `FarmingBlockState` into `FarmingBlock`.

**Methods**
- `onEntityAdd(Holder<ChunkStore> holder, AddReason reason, Store<ChunkStore> store)`: migrates state on add.
- `onEntityRemoved(Holder<ChunkStore> holder, RemoveReason reason, Store<ChunkStore> store)`: no-op.
- `getQuery()`: returns the query for legacy farming states.

---

# FarmingSystems.CoopResidentTicking

**Overview**
Entity tick system that despawns coop residents when flagged.

**Methods**
- `getQuery()`: targets entities with `CoopResidentComponent`.
- `tick(float dt, int index, ArchetypeChunk<EntityStore> archetypeChunk, Store<EntityStore> store, CommandBuffer<EntityStore> commandBuffer)`: removes marked residents.

---

# FarmingSystems.CoopResidentEntitySystem

**Overview**
Handles coop resident cleanup when entities are removed.

**Methods**
- `getQuery()`: targets entities with `CoopResidentComponent`.
- `onEntityAdded(Ref<EntityStore> ref, AddReason reason, Store<EntityStore> store, CommandBuffer<EntityStore> commandBuffer)`: no-op.
- `onEntityRemove(Ref<EntityStore> ref, RemoveReason reason, Store<EntityStore> store, CommandBuffer<EntityStore> commandBuffer)`: updates coop records when residents despawn.

---

# FarmingSystems.OnCoopAdded

**Overview**
Schedules coop ticks and handles coop block removal cleanup.

**Methods**
- `onEntityAdded(Ref<ChunkStore> ref, AddReason reason, Store<ChunkStore> store, CommandBuffer<ChunkStore> commandBuffer)`: schedules first tick.
- `onEntityRemove(Ref<ChunkStore> ref, RemoveReason reason, Store<ChunkStore> store, CommandBuffer<ChunkStore> commandBuffer)`: handles coop block break.
- `getQuery()`: returns the coop block query.

---

# FarmingSystems.Ticking

**Overview**
Tick system that updates crops, soil decay, and coop behavior.

**Methods**
- `tick(float dt, int index, ArchetypeChunk<ChunkStore> archetypeChunk, Store<ChunkStore> store, CommandBuffer<ChunkStore> commandBuffer)`: runs per-block ticking logic.

---

# FarmingSystems.OnFarmBlockAdded

**Overview**
Initializes farming block state when crops are added.

**Methods**
- `onEntityAdded(Ref<ChunkStore> ref, AddReason reason, Store<ChunkStore> store, CommandBuffer<ChunkStore> commandBuffer)`: ensures stage set and schedules ticks.
- `onEntityRemove(Ref<ChunkStore> ref, RemoveReason reason, Store<ChunkStore> store, CommandBuffer<ChunkStore> commandBuffer)`: no-op.
- `getQuery()`: returns the farming block query.

---

# FarmingSystems.OnSoilAdded

**Overview**
Schedules decay ticks for tilled soil blocks.

**Methods**
- `onEntityAdded(Ref<ChunkStore> ref, AddReason reason, Store<ChunkStore> store, CommandBuffer<ChunkStore> commandBuffer)`: computes and schedules decay.
- `onEntityRemove(Ref<ChunkStore> ref, RemoveReason reason, Store<ChunkStore> store, CommandBuffer<ChunkStore> commandBuffer)`: no-op.
- `getQuery()`: returns the tilled soil query.
