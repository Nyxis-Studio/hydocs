**Source Hash:** `6efd459b006020cd057d9935f68ef86d26741758202bdab686e918ea34855ab2`

# RoofConnectedBlockRuleSet

## Overview

## Constructor Descriptions
- `RoofConnectedBlockRuleSet()`
  - Creates a `RoofConnectedBlockRuleSet` instance.

## Method Descriptions
- `isWidthFulfilled(World world, Vector3i coordinate, Vector3i mutablePos, StairConnectedBlockRuleSet.StairConnection backConnection, Rotation currentYaw, int blockId, int width)`: Add description.
  - Executes `isWidthFulfilled` behavior.
- `isTopperConnectionCompatible(RotationTuple rotation, ObjectIntPair<StairConnectedBlockRuleSet.StairType> otherStair, Rotation yawOffset)`: Add description.
  - Executes `isTopperConnectionCompatible` behavior.
- `canBeTopper(World world, Vector3i coordinate, StairLikeConnectedBlockRuleSet currentRuleSet, RotationTuple rotation, Vector3i mutablePos)`: Add description.
  - Executes `canBeTopper` behavior.
- `isValleyConnectionCompatible(RotationTuple rotation, ObjectIntPair<StairConnectedBlockRuleSet.StairType> otherStair, Rotation yawOffset, boolean inverted)`: Add description.
  - Executes `isValleyConnectionCompatible` behavior.
- `onlyUpdateOnPlacement()`: Add description.
  - Executes `onlyUpdateOnPlacement` behavior.
- `updateCachedBlockTypes(BlockType baseBlockType, BlockTypeAssetMap<String, BlockType> assetMap)`: Add description.
  - Executes `updateCachedBlockTypes` behavior.
- `getMaterialName()`: Add description.
  - Executes `getMaterialName` behavior.

## Notes
- No additional notes.
