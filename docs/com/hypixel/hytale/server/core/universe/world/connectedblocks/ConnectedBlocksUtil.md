# ConnectedBlocksUtil

## Overview
- Documentation for `ConnectedBlocksUtil`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.connectedblocks`.

## Constructors
- None.

## Methods
- `setConnectedBlockAndNotifyNeighbors(int blockTypeId, @Nonnull RotationTuple blockTypeRotation, @Nonnull Vector3i placementNormal, @Nonnull Vector3i blockPosition, @Nonnull WorldChunk worldChunkComponent, @Nonnull BlockChunk blockChunkComponent)`
  - Executes `setConnectedBlockAndNotifyNeighbors` behavior.
- `updateNeighborsWithDepth(@Nonnull WorldChunk worldChunkComponent, @Nonnull Vector3i startCoordinate, @Nonnull Vector3i placementNormal, int settings)`
  - Executes `updateNeighborsWithDepth` behavior.
- `notifyNeighborsAndCollectChanges(@Nonnull World world, @Nonnull Vector3i origin, @Nonnull Map<Vector3i, ConnectedBlockResult> desiredChanges, Vector3i placementNormal)`
  - Executes `notifyNeighborsAndCollectChanges` behavior.
- `getDesiredConnectedBlockType(@Nonnull World world, @Nonnull Vector3i coordinate, @Nonnull BlockType currentBlockType, int currentRotation, @Nonnull Vector3i placementNormal, boolean isPlacement)`
  - Executes `getDesiredConnectedBlockType` behavior.
- `blockTypeKey()`
  - Executes `blockTypeKey` behavior.
- `rotationIndex()`
  - Executes `rotationIndex` behavior.
- `getAdditionalConnectedBlocks()`
  - Executes `getAdditionalConnectedBlocks` behavior.
- `addAdditionalBlock(@Nonnull Vector3i offset, @Nonnull String blockTypeKey, int rotationIndex)`
  - Executes `addAdditionalBlock` behavior.
- `equals(Object obj)`
  - Executes `equals` behavior.
- `hashCode()`
  - Executes `hashCode` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
