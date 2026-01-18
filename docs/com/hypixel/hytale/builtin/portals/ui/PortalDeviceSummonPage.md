# PortalDeviceSummonPage

## Overview
- Documentation for `PortalDeviceSummonPage`.
- Declared as a class in `com.hypixel.hytale.builtin.portals.ui`.

## Constructors
- `PortalDeviceSummonPage(@Nonnull PlayerRef playerRef, PortalDeviceConfig config, Ref<ChunkStore> blockRef, ItemStack offeredItemStack)`
  - Creates a `PortalDeviceSummonPage` instance.

## Methods
- `build(@Nonnull Ref<EntityStore> ref, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder, @Nonnull Store<EntityStore> store)`
  - Executes `build` behavior.
- `updateCustomPills(UICommandBuilder commandBuilder, PortalType portalType)`
  - Executes `updateCustomPills` behavior.
- `updateBulletList(UICommandBuilder commandBuilder, String selector, String[] messageKeys)`
  - Executes `updateBulletList` behavior.
- `createDescription(PortalType portalType, int timeLimitSeconds)`
  - Executes `createDescription` behavior.
- `formatDurationCrudely(int seconds)`
  - Executes `formatDurationCrudely` behavior.
- `handleDataEvent(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull Data data)`
  - Executes `handleDataEvent` behavior.
- `spawnReturnPortal(World world, PortalWorld portalWorld, UUID sampleUuid, String portalBlockType)`
  - Executes `spawnReturnPortal` behavior.
- `getSpawnTransform(World world, UUID sampleUuid, @Nullable PortalSpawn portalSpawn)`
  - Executes `getSpawnTransform` behavior.
- `computeState(@Nonnull Player player, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `computeState` behavior.
- `decrementItemInHand(Inventory inventory, int amount)`
  - Executes `decrementItemInHand` behavior.
- `CanSpawnPortal(PortalKey portalKey, PortalType portalType, WorldChunk worldChunk, BlockModule.BlockStateInfo blockState, PortalDevice portalDevice, PortalGameplayConfig portalGameplayConfig)`
  - Executes `CanSpawnPortal` behavior.
- `InstanceKeyNotFound(String instanceId)`
  - Executes `InstanceKeyNotFound` behavior.
- `PortalTypeNotFound(String portalTypeId)`
  - Executes `PortalTypeNotFound` behavior.

## Notes
- No additional notes.
