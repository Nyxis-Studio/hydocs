**Source Hash:** `dab92cad8628d31a6d2c4659f0fe88c378b3f5cb52ee12b5d5af92c2f0c9c70c`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# CoopBlock

## Overview
Chunk component that stores coop state, including captured residents and produced items. Handles resident spawning and despawning, manages produce generation over time, and drops stored items when the coop is broken.

## Field Descriptions
- `STATE_PRODUCE`: Block state key used to indicate available produce.
- `CODEC`: Builder codec for coop state, residents, and inventory storage.
- `LOGGER`: Logger used for warnings and spawn diagnostics.
- `coopAssetId`: Asset ID for the farming coop configuration.
- `residents`: Captured residents tracked by the coop.
- `itemContainer`: Storage container for produced items.

## Constructor Descriptions
- `CoopBlock()`: Creates a coop with a storage container sized to five slots.
- `CoopBlock(String farmingCoopId, List<CoopResident> residents, ItemContainer itemContainer)`: Creates a coop from persisted state and ensures storage capacity.

## Method Descriptions
- `getComponentType()`: Returns the chunk component type used for coop blocks.
- `getCoopAsset()`: Looks up the coop asset definition for the stored asset ID.
- `tryPutResident(CapturedNPCMetadata metadata, WorldTimeResource worldTimeResource)`: Adds a captured resident if capacity and NPC group rules allow it.
- `tryPutWildResidentFromWild(Store<EntityStore> store, Ref<EntityStore> entityRef, WorldTimeResource worldTimeResource, Vector3i coopLocation)`: Converts a wild NPC into a coop resident and tags it with the coop location.
- `getCoopAcceptsNPCGroup(int npcRoleIndex)`: Checks NPC group rules against the coop asset configuration.
- `generateProduceToInventory(WorldTimeResource worldTimeResource)`: Calculates produce since last harvest and adds drops to the coop inventory.
- `gatherProduceFromInventory(ItemContainer playerInventory)`: Transfers all stored items to a player inventory.
- `ensureSpawnResidentsInWorld(World world, Store<EntityStore> store, Vector3d coopLocation, Vector3d spawnOffset)`: Spawns residents around the coop if they are not already deployed.
- `ensureNoResidentsInWorld(Store<EntityStore> store)`: Marks deployed residents for despawn and clears invalid entries.
- `shouldResidentsBeInCoop(WorldTimeResource worldTimeResource)`: Returns whether residents should be in the coop based on roam time.
- `getNextScheduledTick(WorldTimeResource worldTimeResource)`: Computes the next time to tick based on resident roam schedule.
- `handleResidentDespawn(UUID entityUuid)`: Removes the resident record tied to a despawned entity.
- `handleBlockBroken(World world, WorldTimeResource worldTimeResource, Store<EntityStore> store, int blockX, int blockY, int blockZ)`: Spawns residents, generates produce, drops items, and removes coop components.
- `hasProduce()`: Returns whether the coop inventory contains any items.
- `clone()`: Clones the coop state for storage.

## Usage Notes
- The coop enforces a five-slot storage minimum and always upsizes to that capacity.
- Produce generation depends on `lastProduced` timestamps stored per resident.

## Examples
```java
CoopBlock coop = new CoopBlock();
```

---

# CoopBlock.CoopResident

## Overview
Record for a single coop resident, including NPC metadata, persistent entity reference, and last production time.

## Field Descriptions
- `CODEC`: Builder codec for resident persistence.
- `metadata`: Captured NPC metadata for the resident.
- `persistentRef`: Persistent reference to a spawned entity, if any.
- `deployedToWorld`: Whether the resident is currently spawned.
- `lastProduced`: Timestamp of the last produce generation.

## Constructor Descriptions
- `CoopResident()`: Creates an empty resident record.
- `CoopResident(CapturedNPCMetadata metadata, PersistentRef persistentRef, Instant lastProduced)`: Initializes the resident with metadata and timestamps.

## Method Descriptions
- `getMetadata()`: Returns the captured NPC metadata.
- `getPersistentRef()`: Returns the persistent entity reference, if any.
- `setPersistentRef(PersistentRef persistentRef)`: Updates the persistent entity reference.
- `getDeployedToWorld()`: Returns whether the resident is spawned.
- `setDeployedToWorld(boolean deployedToWorld)`: Updates the deployed state.
- `getLastProduced()`: Returns the last production time.
- `setLastProduced(Instant lastProduced)`: Updates the last production time.

## Usage Notes
- `lastProduced` is updated whenever produce is generated for this resident.

## Examples
```java
CoopBlock.CoopResident resident = new CoopBlock.CoopResident();
```
