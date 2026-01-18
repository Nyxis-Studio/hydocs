# BlockPlaceUtils

## Overview
- Documentation for `BlockPlaceUtils`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.interaction`.

## Constructors
- None.

## Methods
- `placeBlock(@Nonnull Ref<EntityStore> ref, @Nonnull ItemStack itemStack, @Nullable String blockTypeKey, @Nonnull ItemContainer itemContainer, @Nonnull Vector3i placementNormal, @Nonnull Vector3i blockPosition, @Nonnull BlockRotation blockRotation, @Nullable Inventory inventory, byte activeSlot, boolean removeItemInHand, @Nonnull Ref<ChunkStore> chunkReference, @Nonnull ComponentAccessor<ChunkStore> chunkStore, @Nonnull ComponentAccessor<EntityStore> entityStore)`
  - Executes `placeBlock` behavior.
- `onPlaceBlockFailure(@Nullable ItemStack itemStack, @Nullable Inventory inventory, byte activeSlot, @Nullable Player playerComponent, @Nonnull BlockSection blockSection, @Nonnull Vector3i blockPosition)`
  - Executes `onPlaceBlockFailure` behavior.
- `onPlaceBlockSuccess(@Nullable ItemStack itemStack, @Nonnull WorldChunk worldChunkComponent, @Nonnull Vector3i blockPosition)`
  - Executes `onPlaceBlockSuccess` behavior.
- `validateBlockToPlace(@Nullable String blockTypeKey, @Nullable PlayerRef playerRefComponent)`
  - Executes `validateBlockToPlace` behavior.
- `validateAndPlacePrefab(@Nonnull Vector3i blockPosition, @Nonnull String prefabListAssetId, @Nullable PlayerRef playerRefComponent, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `validateAndPlacePrefab` behavior.
- `tryPlaceBlock(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3i placementNormal, @Nonnull Vector3i blockPosition, @Nonnull String blockTypeKey, @Nonnull RotationTuple rotation, @Nonnull WorldChunk worldChunkComponent, @Nonnull BlockChunk blockChunkComponent, @Nonnull Ref<ChunkStore> chunkReference, @Nonnull ComponentAccessor<ChunkStore> chunkStore, @Nonnull ComponentAccessor<EntityStore> entityStore)`
  - Executes `tryPlaceBlock` behavior.
- `breakAndDropReplacedBlock(@Nonnull Vector3i blockPosition, @Nonnull WorldChunk worldChunkComponent, @Nonnull Ref<ChunkStore> chunkReference, @Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<ChunkStore> chunkStore, @Nonnull ComponentAccessor<EntityStore> entityStore)`
  - Executes `breakAndDropReplacedBlock` behavior.
- `canPlaceBlock(@Nonnull BlockType blockType, @Nonnull String placedBlockTypeKey)`
  - Executes `canPlaceBlock` behavior.

## Notes
- No additional notes.
