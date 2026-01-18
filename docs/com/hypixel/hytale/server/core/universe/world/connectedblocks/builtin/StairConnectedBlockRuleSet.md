# StairConnectedBlockRuleSet

## Overview
- Documentation for `StairConnectedBlockRuleSet`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.connectedblocks.builtin`.

## Constructors
- `StairConnectedBlockRuleSet()`
  - Creates a `StairConnectedBlockRuleSet` instance.

## Methods
- `onlyUpdateOnPlacement()`
  - Executes `onlyUpdateOnPlacement` behavior.
- `updateCachedBlockTypes(BlockType baseBlockType, BlockTypeAssetMap<String, BlockType> assetMap)`
  - Executes `updateCachedBlockTypes` behavior.
- `getStairData(World world, Vector3i coordinate, @Nullable String requiredMaterialName)`
  - Executes `getStairData` behavior.
- `getStairType(int blockId)`
  - Executes `getStairType` behavior.
- `getMaterialName()`
  - Executes `getMaterialName` behavior.
- `getStairBlockType(StairType stairType)`
  - Executes `getStairBlockType` behavior.
- `getCornerConnection(World world, StairLikeConnectedBlockRuleSet currentRuleSet, Vector3i coordinate, Vector3i mutablePos, int rotation, Rotation currentYaw, boolean upsideDown, int width)`
  - Executes `getCornerConnection` behavior.
- `getInvertedCornerConnection(World world, StairLikeConnectedBlockRuleSet currentRuleSet, Vector3i coordinate, Vector3i mutablePos, Rotation currentYaw, boolean upsideDown)`
  - Executes `getInvertedCornerConnection` behavior.
- `canConnectTo(Rotation currentYaw, Rotation otherYaw, boolean upsideDown, boolean otherUpsideDown)`
  - Executes `canConnectTo` behavior.
- `getConnection(Rotation currentYaw, Rotation otherYaw, StairType otherStairType, boolean inverted)`
  - Executes `getConnection` behavior.
- `getBlockIdForStairType(StairType stairType, BlockTypeAssetMap<String, BlockType> assetMap)`
  - Executes `getBlockIdForStairType` behavior.
- `corner(boolean right)`
  - Executes `corner` behavior.
- `invertedCorner(boolean right)`
  - Executes `invertedCorner` behavior.
- `isCorner()`
  - Executes `isCorner` behavior.
- `isInvertedCorner()`
  - Executes `isInvertedCorner` behavior.
- `isLeft()`
  - Executes `isLeft` behavior.
- `isRight()`
  - Executes `isRight` behavior.
- `getStairType(boolean inverted)`
  - Executes `getStairType` behavior.

## Notes
- No additional notes.
