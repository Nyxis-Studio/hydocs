**Source Hash:** `0e1dde768a200c05ef938f08a919f78669f62e552d185ea065774f7529e36270`

# AStarNode

## Overview

## Constructor Descriptions
- `AStarNode(0)`
  - Creates a `AStarNode` instance.
- `AStarNode(int numDirections)`
  - Creates a `AStarNode` instance.

## Method Descriptions
- `getPositionIndex()`: Add description.
  - Executes `getPositionIndex` behavior.
- `getSuccessors()`: Add description.
  - Executes `getSuccessors` behavior.
- `getSuccessor(int index)`: Add description.
  - Executes `getSuccessor` behavior.
- `setSuccessor(int directionIndex, @Nonnull AStarNode node, int inverseDirectionIndex, float cost)`: Add description.
  - Executes `setSuccessor` behavior.
- `getPredecessor()`: Add description.
  - Executes `getPredecessor` behavior.
- `getNextPathNode()`: Add description.
  - Executes `getNextPathNode` behavior.
- `setNextNode(AStarNode next, int length)`: Add description.
  - Executes `setNextNode` behavior.
- `getTravelCost()`: Add description.
  - Executes `getTravelCost` behavior.
- `getEstimateToGoal()`: Add description.
  - Executes `getEstimateToGoal` behavior.
- `getTotalCost()`: Add description.
  - Executes `getTotalCost` behavior.
- `getPredecessorDirection()`: Add description.
  - Executes `getPredecessorDirection` behavior.
- `close()`: Add description.
  - Executes `close` behavior.
- `isOpen()`: Add description.
  - Executes `isOpen` behavior.
- `isInvalid()`: Add description.
  - Executes `isInvalid` behavior.
- `getLength()`: Add description.
  - Executes `getLength` behavior.
- `next()`: Add description.
  - Executes `next` behavior.
- `getPosition()`: Add description.
  - Executes `getPosition` behavior.
- `advance(int skip)`: Add description.
  - Executes `advance` behavior.
- `initAsStartNode(@Nonnull Vector3d position, long positionIndex, float cost, float estimateCost)`: Add description.
  - Executes `initAsStartNode` behavior.
- `initWithPredecessor(@Nonnull AStarNode predecessor, int directionIndex, @Nonnull Vector3d position, long positionIndex, int inverseDirectionIndex, float travelCost, float estimateCost)`: Add description.
  - Executes `initWithPredecessor` behavior.
- `initAsInvalid(@Nonnull Vector3d position, long positionIndex)`: Add description.
  - Executes `initAsInvalid` behavior.
- `adjustOptimalPath(AStarNode parentNode, float deltaCost, int direction)`: Add description.
  - Executes `adjustOptimalPath` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.

## Notes
- No additional notes.
