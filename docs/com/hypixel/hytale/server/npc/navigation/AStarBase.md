**Source Hash:** `534629653313da5d235f5626707c5b60f069d20296b1bec2563d95fb8e8499b7`

# AStarBase

## Overview

## Constructor Descriptions
- `none()`: No documented methods.

## Method Descriptions
- `setCanMoveDiagonal(boolean canMoveDiagonal)`: Add description.
  - Executes `setCanMoveDiagonal` behavior.
- `setMaxPathLength(int maxPathLength)`: Add description.
  - Executes `setMaxPathLength` behavior.
- `setOpenNodesLimit(int openNodesLimit)`: Add description.
  - Executes `setOpenNodesLimit` behavior.
- `setTotalNodesLimit(int totalNodesLimit)`: Add description.
  - Executes `setTotalNodesLimit` behavior.
- `setStartPosition(@Nonnull Vector3d position)`: Add description.
  - Executes `setStartPosition` behavior.
- `getStartPosition()`: Add description.
  - Executes `getStartPosition` behavior.
- `setOptimizedBuildPath(boolean optimizedBuildPath)`: Add description.
  - Executes `setOptimizedBuildPath` behavior.
- `getEvaluator()`: Add description.
  - Executes `getEvaluator` behavior.
- `getOpenNodes()`: Add description.
  - Executes `getOpenNodes` behavior.
- `getOpenCount()`: Add description.
  - Executes `getOpenCount` behavior.
- `getVisitedBlocks()`: Add description.
  - Executes `getVisitedBlocks` behavior.
- `getStartPositionIndex()`: Add description.
  - Executes `getStartPositionIndex` behavior.
- `getPath()`: Add description.
  - Executes `getPath` behavior.
- `getPosition()`: Add description.
  - Executes `getPosition` behavior.
- `getLength()`: Add description.
  - Executes `getLength` behavior.
- `getIterations()`: Add description.
  - Executes `getIterations` behavior.
- `getEndPosition()`: Add description.
  - Executes `getEndPosition` behavior.
- `clearPath()`: Add description.
  - Executes `clearPath` behavior.
- `initComputePath(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d start, AStarEvaluator evaluator, @Nonnull MotionController motionController, @Nonnull ProbeMoveData probeMoveData, @Nonnull AStarNodePoolProvider nodePoolProvider, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `initComputePath` behavior.
- `computePath(@Nonnull Ref<EntityStore> ref, @Nonnull MotionController motionController, @Nonnull ProbeMoveData probeMoveData, int nodesToProcess, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `computePath` behavior.
- `getProgress()`: Add description.
  - Executes `getProgress` behavior.
- `isComputing()`: Add description.
  - Executes `isComputing` behavior.
- `buildLongestPath()`: Add description.
  - Executes `buildLongestPath` behavior.
- `buildFurthestPath()`: Add description.
  - Executes `buildFurthestPath` behavior.
- `buildBestPath(@Nonnull ToFloatFunction<AStarNode> weight, @Nonnull BiFloatPredicate predicate, float initialValue)`: Add description.
  - Executes `buildBestPath` behavior.
- `findBestVisitedNode(@Nonnull ToFloatFunction<AStarNode> weight, @Nonnull BiFloatPredicate predicate, float initialValue)`: Add description.
  - Executes `findBestVisitedNode` behavior.
- `buildBestPath(@Nonnull BiToFloatFunction<AStarNode, T> weight, @Nonnull BiFloatPredicate predicate, float initialValue, T obj)`: Add description.
  - Executes `buildBestPath` behavior.
- `findBestVisitedNode(@Nonnull BiToFloatFunction<AStarNode, T> weight, @Nonnull BiFloatPredicate predicate, float initialValue, T obj)`: Add description.
  - Executes `findBestVisitedNode` behavior.
- `createDebugHelper(@Nonnull HytaleLogger logger)`: Add description.
  - Executes `createDebugHelper` behavior.
- `indexFromXYZ(long dx, long dy, long dz)`: Add description.
  - Executes `indexFromXYZ` behavior.
- `zFromIndex(long index)`: Add description.
  - Executes `zFromIndex` behavior.
- `yFromIndex(long index)`: Add description.
  - Executes `yFromIndex` behavior.
- `xFromIndex(long index)`: Add description.
  - Executes `xFromIndex` behavior.
- `positionIndexToString(long index)`: Add description.
  - Executes `positionIndexToString` behavior.
- `setProgress(Progress progress)`: Add description.
  - Executes `setProgress` behavior.
- `canAdvance(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d startPosition, @Nonnull Vector3d destination, @Nonnull MotionController motionController, @Nonnull ProbeMoveData probeMoveData, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `canAdvance` behavior.
- `addStartNode(Vector3d startPosition, @Nonnull Vector3d position, @Nonnull MotionController motionController)`: Add description.
  - Executes `addStartNode` behavior.
- `addOpenNode(@Nonnull AStarNode parentNode, int directionIndex, @Nonnull Vector3d position, long positionIndex, float cost, MotionController motionController)`: Add description.
  - Executes `addOpenNode` behavior.
- `addOpenNode(@Nonnull AStarNode node, long index)`: Add description.
  - Executes `addOpenNode` behavior.
- `updateNode(@Nonnull AStarNode node, int directionIndex, @Nonnull AStarNode targetNode, @Nonnull MotionController motionController)`: Add description.
  - Executes `updateNode` behavior.
- `addOrUpdateNode(@Nonnull AStarNode node, int directionIndex, @Nonnull Vector3d position, @Nonnull MotionController motionController, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `addOrUpdateNode` behavior.
- `updateNodeCost(@Nonnull AStarNode node, int directionIndex, @Nonnull AStarNode targetNode, float stepCost)`: Add description.
  - Executes `updateNodeCost` behavior.
- `positionToIndex(@Nonnull Vector3d position)`: Add description.
  - Executes `positionToIndex` behavior.
- `measureWalkCost(Vector3d fromPosition, Vector3d toPosition, @Nonnull MotionController motionController)`: Add description.
  - Executes `measureWalkCost` behavior.
- `buildPath(@Nullable AStarNode endNode)`: Add description.
  - Executes `buildPath` behavior.
- `addOffsetToIndex(long index, long xSteps, long ySteps, long zSteps)`: Add description.
  - Executes `addOffsetToIndex` behavior.

## Notes
- No additional notes.
