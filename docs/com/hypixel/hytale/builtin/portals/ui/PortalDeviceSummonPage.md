**Source Hash:** `16d1bb6e2590fcccdaadb9bf14ff1afa17dd5e5a7c9102f5332af6d6d4a52d26`

# PortalDeviceSummonPage

## Overview

## Constructor Descriptions
- `PortalDeviceSummonPage(@Nonnull PlayerRef playerRef, PortalDeviceConfig config, Ref<ChunkStore> blockRef, ItemStack offeredItemStack)`
  - Creates a `PortalDeviceSummonPage` instance.

## Method Descriptions
- `build(@Nonnull Ref<EntityStore> ref, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `build` behavior.
- `updateCustomPills(UICommandBuilder commandBuilder, PortalType portalType)`: Add description.
  - Executes `updateCustomPills` behavior.
- `updateBulletList(UICommandBuilder commandBuilder, String selector, String[] messageKeys)`: Add description.
  - Executes `updateBulletList` behavior.
- `createDescription(PortalType portalType, int timeLimitSeconds)`: Add description.
  - Executes `createDescription` behavior.
- `formatDurationCrudely(int seconds)`: Add description.
  - Executes `formatDurationCrudely` behavior.
- `handleDataEvent(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull Data data)`: Add description.
  - Executes `handleDataEvent` behavior.
- `spawnReturnPortal(World world, PortalWorld portalWorld, UUID sampleUuid, String portalBlockType)`: Add description.
  - Executes `spawnReturnPortal` behavior.
- `getSpawnTransform(World world, UUID sampleUuid, @Nullable PortalSpawn portalSpawn)`: Add description.
  - Executes `getSpawnTransform` behavior.
- `computeState(@Nonnull Player player, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `computeState` behavior.
- `decrementItemInHand(Inventory inventory, int amount)`: Add description.
  - Executes `decrementItemInHand` behavior.
- `CanSpawnPortal(PortalKey portalKey, PortalType portalType, WorldChunk worldChunk, BlockModule.BlockStateInfo blockState, PortalDevice portalDevice, PortalGameplayConfig portalGameplayConfig)`: Add description.
  - Executes `CanSpawnPortal` behavior.
- `InstanceKeyNotFound(String instanceId)`: Add description.
  - Executes `InstanceKeyNotFound` behavior.
- `PortalTypeNotFound(String portalTypeId)`: Add description.
  - Executes `PortalTypeNotFound` behavior.

## Notes
- No additional notes.
