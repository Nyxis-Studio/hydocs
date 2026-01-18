**Source Hash:** `cefcd78b9ce53e1229e764b170c844ace537e4106427a632f00868bdaaa18569`

# ConnectedBlocksUtil

## Overview

## Constructor Descriptions
- `none()`: No documented methods.

## Method Descriptions
- `setConnectedBlockAndNotifyNeighbors(int blockTypeId, @Nonnull RotationTuple blockTypeRotation, @Nonnull Vector3i placementNormal, @Nonnull Vector3i blockPosition, @Nonnull WorldChunk worldChunkComponent, @Nonnull BlockChunk blockChunkComponent)`: Add description.
  - Executes `setConnectedBlockAndNotifyNeighbors` behavior.
- `updateNeighborsWithDepth(@Nonnull WorldChunk worldChunkComponent, @Nonnull Vector3i startCoordinate, @Nonnull Vector3i placementNormal, int settings)`: Add description.
  - Executes `updateNeighborsWithDepth` behavior.
- `notifyNeighborsAndCollectChanges(@Nonnull World world, @Nonnull Vector3i origin, @Nonnull Map<Vector3i, ConnectedBlockResult> desiredChanges, Vector3i placementNormal)`: Add description.
  - Executes `notifyNeighborsAndCollectChanges` behavior.
- `getDesiredConnectedBlockType(@Nonnull World world, @Nonnull Vector3i coordinate, @Nonnull BlockType currentBlockType, int currentRotation, @Nonnull Vector3i placementNormal, boolean isPlacement)`: Add description.
  - Executes `getDesiredConnectedBlockType` behavior.
- `blockTypeKey()`: Add description.
  - Executes `blockTypeKey` behavior.
- `rotationIndex()`: Add description.
  - Executes `rotationIndex` behavior.
- `getAdditionalConnectedBlocks()`: Add description.
  - Executes `getAdditionalConnectedBlocks` behavior.
- `addAdditionalBlock(@Nonnull Vector3i offset, @Nonnull String blockTypeKey, int rotationIndex)`: Add description.
  - Executes `addAdditionalBlock` behavior.
- `equals(Object obj)`: Add description.
  - Executes `equals` behavior.
- `hashCode()`: Add description.
  - Executes `hashCode` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.

## Notes
- No additional notes.
