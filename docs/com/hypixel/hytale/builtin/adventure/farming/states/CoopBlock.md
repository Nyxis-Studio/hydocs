# CoopBlock

**Overview**
Block component that manages coop residents and produce inventory.
Handles capturing, spawning, and despawning NPC residents.

**Constructors**
- `CoopBlock()`: creates a coop with default storage capacity.
- `CoopBlock(String farmingCoopId, List<CoopResident> residents, ItemContainer itemContainer)`: creates a coop with state.

**Methods**
- `getComponentType()`: returns the coop block component type.
- `getCoopAsset()`: resolves the coop asset by id.
- `tryPutResident(CapturedNPCMetadata metadata, WorldTimeResource worldTimeResource)`: adds a captured resident.
- `tryPutWildResidentFromWild(Store<EntityStore> store, Ref<EntityStore> entityRef, WorldTimeResource worldTimeResource, Vector3i coopLocation)`: captures a wild NPC.
- `getCoopAcceptsNPCGroup(int npcRoleIndex)`: checks allowed NPC groups.
- `generateProduceToInventory(WorldTimeResource worldTimeResource)`: generates produce based on residents.
- `gatherProduceFromInventory(ItemContainer playerInventory)`: transfers produce to a player.
- `ensureSpawnResidentsInWorld(World world, Store<EntityStore> store, Vector3d coopLocation, Vector3d spawnOffset)`: spawns residents around the coop.
- `ensureNoResidentsInWorld(Store<EntityStore> store)`: despawns residents in the world.
- `shouldResidentsBeInCoop(WorldTimeResource worldTimeResource)`: checks roam schedule.
- `getNextScheduledTick(WorldTimeResource worldTimeResource)`: computes next coop tick time.
- `handleResidentDespawn(UUID entityUuid)`: removes a resident record.
- `handleBlockBroken(World world, WorldTimeResource worldTimeResource, Store<EntityStore> store, int blockX, int blockY, int blockZ)`: spawns residents, drops items, and cleans up.
- `hasProduce()`: returns true if storage has items.
- `clone()`: clones the coop block state.

**Notes**
- Uses `CoopResident` to persist resident metadata and spawn refs.

---

# CoopBlock.CoopResident

**Overview**
Data holder for a coop resident, its metadata, and spawn reference.

**Constructors**
- `CoopResident()`: default constructor.
- `CoopResident(CapturedNPCMetadata metadata, PersistentRef persistentRef, Instant lastProduced)`: initializes resident data.

**Methods**
- `getMetadata()`: returns captured NPC metadata.
- `getPersistentRef()`: returns the persistent entity reference.
- `setPersistentRef(PersistentRef persistentRef)`: sets the persistent reference.
- `getDeployedToWorld()`: returns deployment state.
- `setDeployedToWorld(boolean deployedToWorld)`: sets deployment state.
- `getLastProduced()`: returns last produced time.
- `setLastProduced(Instant lastProduced)`: sets last produced time.
