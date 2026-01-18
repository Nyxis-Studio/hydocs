# AStarNode

## Overview
- Documentation for `AStarNode`.
- Declared as a class in `com.hypixel.hytale.server.npc.navigation`.

## Constructors
- `AStarNode(0)`
  - Creates a `AStarNode` instance.
- `AStarNode(int numDirections)`
  - Creates a `AStarNode` instance.

## Methods
- `getPositionIndex()`
  - Executes `getPositionIndex` behavior.
- `getSuccessors()`
  - Executes `getSuccessors` behavior.
- `getSuccessor(int index)`
  - Executes `getSuccessor` behavior.
- `setSuccessor(int directionIndex, @Nonnull AStarNode node, int inverseDirectionIndex, float cost)`
  - Executes `setSuccessor` behavior.
- `getPredecessor()`
  - Executes `getPredecessor` behavior.
- `getNextPathNode()`
  - Executes `getNextPathNode` behavior.
- `setNextNode(AStarNode next, int length)`
  - Executes `setNextNode` behavior.
- `getTravelCost()`
  - Executes `getTravelCost` behavior.
- `getEstimateToGoal()`
  - Executes `getEstimateToGoal` behavior.
- `getTotalCost()`
  - Executes `getTotalCost` behavior.
- `getPredecessorDirection()`
  - Executes `getPredecessorDirection` behavior.
- `close()`
  - Executes `close` behavior.
- `isOpen()`
  - Executes `isOpen` behavior.
- `isInvalid()`
  - Executes `isInvalid` behavior.
- `getLength()`
  - Executes `getLength` behavior.
- `next()`
  - Executes `next` behavior.
- `getPosition()`
  - Executes `getPosition` behavior.
- `advance(int skip)`
  - Executes `advance` behavior.
- `initAsStartNode(@Nonnull Vector3d position, long positionIndex, float cost, float estimateCost)`
  - Executes `initAsStartNode` behavior.
- `initWithPredecessor(@Nonnull AStarNode predecessor, int directionIndex, @Nonnull Vector3d position, long positionIndex, int inverseDirectionIndex, float travelCost, float estimateCost)`
  - Executes `initWithPredecessor` behavior.
- `initAsInvalid(@Nonnull Vector3d position, long positionIndex)`
  - Executes `initAsInvalid` behavior.
- `adjustOptimalPath(AStarNode parentNode, float deltaCost, int direction)`
  - Executes `adjustOptimalPath` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
