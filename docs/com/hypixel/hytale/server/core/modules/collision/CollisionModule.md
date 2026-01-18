**Source Hash:** `aa4bc140caee285f2eb156677d8a3e6134489688e3cfbed6ff8fb7e842f35963`

# CollisionModule

## Overview

## Constructor Descriptions
- `CollisionModule(@Nonnull JavaPluginInit init)`
  - Creates a `CollisionModule` instance.

## Method Descriptions
- `get()`: Add description.
  - Executes `get` behavior.
- `getConfig()`: Add description.
  - Executes `getConfig` behavior.
- `setup()`: Add description.
  - Executes `setup` behavior.
- `getTangiableEntitySpatialComponent()`: Add description.
  - Executes `getTangiableEntitySpatialComponent` behavior.
- `onLoadedAssetsEvent(@Nonnull LoadedAssetsEvent<String, BlockBoundingBoxes, IndexedLookupTableAssetMap<String, BlockBoundingBoxes>> event)`: Add description.
  - Executes `onLoadedAssetsEvent` behavior.
- `handleLoadedHitbox(@Nonnull BlockBoundingBoxes box)`: Add description.
  - Executes `handleLoadedHitbox` behavior.
- `findCollisions(@Nonnull Box collider, @Nonnull Vector3d pos, @Nonnull Vector3d v, @Nonnull CollisionResult result, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `findCollisions` behavior.
- `findCollisions(@Nonnull Box collider, @Nonnull Vector3d pos, @Nonnull Vector3d v, boolean stopOnCollisionFound, @Nonnull CollisionResult result, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `findCollisions` behavior.
- `findBlockCollisionsIterative(@Nonnull World world, @Nonnull Box collider, @Nonnull Vector3d pos, @Nonnull Vector3d v, boolean stopOnCollisionFound, @Nonnull CollisionResult result)`: Add description.
  - Executes `findBlockCollisionsIterative` behavior.
- `findCharacterCollisions(@Nonnull Vector3d pos, @Nonnull Vector3d v, @Nonnull CollisionResult result, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `findCharacterCollisions` behavior.
- `findBlockCollisionsShortDistance(@Nonnull World world, @Nonnull Box collider, @Nonnull Vector3d pos, @Nonnull Vector3d v, @Nonnull CollisionResult result)`: Add description.
  - Executes `findBlockCollisionsShortDistance` behavior.
- `processCollision(@Nonnull CollisionResult result, @Nonnull Vector3d pos, @Nonnull BoxBlockIntersectionEvaluator boxBlockIntersectionEvaluator, boolean haveCollision, int hitboxIndex)`: Add description.
  - Executes `processCollision` behavior.
- `findIntersections(@Nonnull World world, @Nonnull Box collider, @Nonnull Vector3d pos, @Nonnull CollisionResult result, boolean triggerBlocks, boolean intersections)`: Add description.
  - Executes `findIntersections` behavior.
- `validatePosition(@Nonnull World world, @Nonnull Box collider, @Nonnull Vector3d pos, @Nonnull CollisionResult result)`: Add description.
  - Executes `validatePosition` behavior.
- `validatePosition(@Nonnull World world, @Nonnull Box collider, @Nonnull Vector3d pos, int invalidBlockMaterials, T t, @Nonnull CollisionFilter<BoxBlockIntersectionEvaluator, T> predicate, @Nonnull CollisionResult result)`: Add description.
  - Executes `validatePosition` behavior.
- `validatePosition(@Nonnull World world, @Nonnull Box collider, @Nonnull Vector3d pos, T t, @Nonnull CollisionFilter<BoxBlockIntersectionEvaluator, T> predicate, boolean disableDamageBlocks, @Nonnull CollisionResult result)`: Add description.
  - Executes `validatePosition` behavior.
- `addImmediateCollision(@Nonnull Vector3d pos, @Nonnull CollisionResult result, @Nonnull CollisionConfig coll, int i)`: Add description.
  - Executes `addImmediateCollision` behavior.
- `isBelowMovementThreshold(@Nonnull Vector3d v)`: Add description.
  - Executes `isBelowMovementThreshold` behavior.
- `logOverlap(@Nonnull Vector3d pos, @Nonnull Box collider, @Nonnull CollisionConfig coll, @Nonnull Box hitBox, int x, int y, int z, int index, int intersectType)`: Add description.
  - Executes `logOverlap` behavior.

## Notes
- No additional notes.
