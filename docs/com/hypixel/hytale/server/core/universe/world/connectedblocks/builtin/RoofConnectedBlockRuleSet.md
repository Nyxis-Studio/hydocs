# RoofConnectedBlockRuleSet

## Overview
- Documentation for `RoofConnectedBlockRuleSet`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.connectedblocks.builtin`.

## Constructors
- `RoofConnectedBlockRuleSet()`
  - Creates a `RoofConnectedBlockRuleSet` instance.

## Methods
- `isWidthFulfilled(World world, Vector3i coordinate, Vector3i mutablePos, StairConnectedBlockRuleSet.StairConnection backConnection, Rotation currentYaw, int blockId, int width)`
  - Executes `isWidthFulfilled` behavior.
- `isTopperConnectionCompatible(RotationTuple rotation, ObjectIntPair<StairConnectedBlockRuleSet.StairType> otherStair, Rotation yawOffset)`
  - Executes `isTopperConnectionCompatible` behavior.
- `canBeTopper(World world, Vector3i coordinate, StairLikeConnectedBlockRuleSet currentRuleSet, RotationTuple rotation, Vector3i mutablePos)`
  - Executes `canBeTopper` behavior.
- `isValleyConnectionCompatible(RotationTuple rotation, ObjectIntPair<StairConnectedBlockRuleSet.StairType> otherStair, Rotation yawOffset, boolean inverted)`
  - Executes `isValleyConnectionCompatible` behavior.
- `onlyUpdateOnPlacement()`
  - Executes `onlyUpdateOnPlacement` behavior.
- `updateCachedBlockTypes(BlockType baseBlockType, BlockTypeAssetMap<String, BlockType> assetMap)`
  - Executes `updateCachedBlockTypes` behavior.
- `getMaterialName()`
  - Executes `getMaterialName` behavior.

## Notes
- No additional notes.
