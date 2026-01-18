**Source Hash:** `56d69b55d8eb2a11f64e3465d9b35fa0abcc8c1e125c8444581ebddfb2ad59f9`

# ProbeMoveData

## Overview

## Constructor Descriptions
- `ProbeMoveData()`
  - Creates a `ProbeMoveData` instance.

## Method Descriptions
- `setSaveSegments(boolean saveSegments)`: Add description.
  - Executes `setSaveSegments` behavior.
- `isAvoidingBlockDamage()`: Add description.
  - Executes `isAvoidingBlockDamage` behavior.
- `setAvoidingBlockDamage(boolean avoid)`: Add description.
  - Executes `setAvoidingBlockDamage` behavior.
- `isRelaxedMoveConstraints()`: Add description.
  - Executes `isRelaxedMoveConstraints` behavior.
- `setRelaxedMoveConstraints(boolean relaxedMoveConstraints)`: Add description.
  - Executes `setRelaxedMoveConstraints` behavior.
- `setPosition(@Nonnull Vector3d position)`: Add description.
  - Executes `setPosition` behavior.
- `setDirection(@Nonnull Vector3d direction)`: Add description.
  - Executes `setDirection` behavior.
- `setTargetPosition(@Nonnull Vector3d targetPosition)`: Add description.
  - Executes `setTargetPosition` behavior.
- `canAdvance(@Nonnull Ref<EntityStore> ref, @Nonnull MotionController motionController, double threshold, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `canAdvance` behavior.
- `canAdvanceAbs(@Nonnull Ref<EntityStore> ref, @Nonnull MotionController motionController, double requiredDistance, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `canAdvanceAbs` behavior.
- `canMoveTo(@Nonnull Ref<EntityStore> ref, @Nonnull MotionController motionController, double maxDistance, double maxDistanceY, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `canMoveTo` behavior.
- `canMoveTo(@Nonnull Ref<EntityStore> ref, @Nonnull MotionController motionController, double maxDistance, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `canMoveTo` behavior.
- `computePosition(double distance, @Nonnull Vector3d result)`: Add description.
  - Executes `computePosition` behavior.
- `startProbing()`: Add description.
  - Executes `startProbing` behavior.
- `addStartSegment(@Nonnull Vector3d position, boolean onGround)`: Add description.
  - Executes `addStartSegment` behavior.
- `addEndSegment(@Nonnull Vector3d position, boolean onGround, double distance)`: Add description.
  - Executes `addEndSegment` behavior.
- `addBlockedGroundSegment(@Nonnull Vector3d position, double distance, @Nonnull Vector3d normal, int blockId)`: Add description.
  - Executes `addBlockedGroundSegment` behavior.
- `addHitGroundSegment(@Nonnull Vector3d position, double distance, @Nonnull Vector3d normal, int blockId)`: Add description.
  - Executes `addHitGroundSegment` behavior.
- `addHitWallSegment(@Nonnull Vector3d position, boolean onGround, double distance, @Nonnull Vector3d normal, int blockId)`: Add description.
  - Executes `addHitWallSegment` behavior.
- `addMoveSegment(@Nonnull Vector3d position, boolean onGround, double distance)`: Add description.
  - Executes `addMoveSegment` behavior.
- `addClimbSegment(@Nonnull Vector3d position, double distance, int blockId)`: Add description.
  - Executes `addClimbSegment` behavior.
- `addHitEdgeSegment(@Nonnull Vector3d position, double distance)`: Add description.
  - Executes `addHitEdgeSegment` behavior.
- `addDropSegment(@Nonnull Vector3d position, double distance)`: Add description.
  - Executes `addDropSegment` behavior.
- `addBlockedDropSegment(@Nonnull Vector3d position, double distance)`: Add description.
  - Executes `addBlockedDropSegment` behavior.
- `changeSegmentToBlockedWall()`: Add description.
  - Executes `changeSegmentToBlockedWall` behavior.
- `changeSegmentToBlockedEdge()`: Add description.
  - Executes `changeSegmentToBlockedEdge` behavior.
- `getLastDistance()`: Add description.
  - Executes `getLastDistance` behavior.
- `newSegment()`: Add description.
  - Executes `newSegment` behavior.
- `initAsStartSegment(@Nonnull Vector3d position, boolean onGround)`: Add description.
  - Executes `initAsStartSegment` behavior.
- `initAsEndSegment(@Nonnull Vector3d position, boolean onGround, double distance)`: Add description.
  - Executes `initAsEndSegment` behavior.
- `initAsBlockedGroundSegment(@Nonnull Vector3d position, double distance, @Nonnull Vector3d normal, int blockId)`: Add description.
  - Executes `initAsBlockedGroundSegment` behavior.
- `initAsHitGroundSegment(@Nonnull Vector3d position, double distance, @Nonnull Vector3d normal, int blockId)`: Add description.
  - Executes `initAsHitGroundSegment` behavior.
- `initAsHitWallSegment(@Nonnull Vector3d position, boolean onGround, double distance, @Nonnull Vector3d normal, int blockId)`: Add description.
  - Executes `initAsHitWallSegment` behavior.
- `initAsClimbSegment(@Nonnull Vector3d position, double distance, int blockId)`: Add description.
  - Executes `initAsClimbSegment` behavior.
- `initAsMoveSegment(@Nonnull Vector3d position, boolean onGround, double distance)`: Add description.
  - Executes `initAsMoveSegment` behavior.
- `initAsDropSegment(@Nonnull Vector3d position, double distance)`: Add description.
  - Executes `initAsDropSegment` behavior.
- `initAsBlockedDropSegment(@Nonnull Vector3d position, double distance)`: Add description.
  - Executes `initAsBlockedDropSegment` behavior.
- `initAsHitEdgeSegment(@Nonnull Vector3d position, double distance)`: Add description.
  - Executes `initAsHitEdgeSegment` behavior.
- `isBlocked()`: Add description.
  - Executes `isBlocked` behavior.
- `canInterpolate()`: Add description.
  - Executes `canInterpolate` behavior.

## Notes
- No additional notes.
