# CollisionModule

## Overview
- Documentation for `CollisionModule`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.collision`.

## Constructors
- `CollisionModule(@Nonnull JavaPluginInit init)`
  - Creates a `CollisionModule` instance.

## Methods
- `get()`
  - Executes `get` behavior.
- `getConfig()`
  - Executes `getConfig` behavior.
- `setup()`
  - Executes `setup` behavior.
- `getTangiableEntitySpatialComponent()`
  - Executes `getTangiableEntitySpatialComponent` behavior.
- `onLoadedAssetsEvent(@Nonnull LoadedAssetsEvent<String, BlockBoundingBoxes, IndexedLookupTableAssetMap<String, BlockBoundingBoxes>> event)`
  - Executes `onLoadedAssetsEvent` behavior.
- `handleLoadedHitbox(@Nonnull BlockBoundingBoxes box)`
  - Executes `handleLoadedHitbox` behavior.
- `findCollisions(@Nonnull Box collider, @Nonnull Vector3d pos, @Nonnull Vector3d v, @Nonnull CollisionResult result, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `findCollisions` behavior.
- `findCollisions(@Nonnull Box collider, @Nonnull Vector3d pos, @Nonnull Vector3d v, boolean stopOnCollisionFound, @Nonnull CollisionResult result, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `findCollisions` behavior.
- `findBlockCollisionsIterative(@Nonnull World world, @Nonnull Box collider, @Nonnull Vector3d pos, @Nonnull Vector3d v, boolean stopOnCollisionFound, @Nonnull CollisionResult result)`
  - Executes `findBlockCollisionsIterative` behavior.
- `findCharacterCollisions(@Nonnull Vector3d pos, @Nonnull Vector3d v, @Nonnull CollisionResult result, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `findCharacterCollisions` behavior.
- `findBlockCollisionsShortDistance(@Nonnull World world, @Nonnull Box collider, @Nonnull Vector3d pos, @Nonnull Vector3d v, @Nonnull CollisionResult result)`
  - Executes `findBlockCollisionsShortDistance` behavior.
- `processCollision(@Nonnull CollisionResult result, @Nonnull Vector3d pos, @Nonnull BoxBlockIntersectionEvaluator boxBlockIntersectionEvaluator, boolean haveCollision, int hitboxIndex)`
  - Executes `processCollision` behavior.
- `findIntersections(@Nonnull World world, @Nonnull Box collider, @Nonnull Vector3d pos, @Nonnull CollisionResult result, boolean triggerBlocks, boolean intersections)`
  - Executes `findIntersections` behavior.
- `validatePosition(@Nonnull World world, @Nonnull Box collider, @Nonnull Vector3d pos, @Nonnull CollisionResult result)`
  - Executes `validatePosition` behavior.
- `validatePosition(@Nonnull World world, @Nonnull Box collider, @Nonnull Vector3d pos, int invalidBlockMaterials, T t, @Nonnull CollisionFilter<BoxBlockIntersectionEvaluator, T> predicate, @Nonnull CollisionResult result)`
  - Executes `validatePosition` behavior.
- `validatePosition(@Nonnull World world, @Nonnull Box collider, @Nonnull Vector3d pos, T t, @Nonnull CollisionFilter<BoxBlockIntersectionEvaluator, T> predicate, boolean disableDamageBlocks, @Nonnull CollisionResult result)`
  - Executes `validatePosition` behavior.
- `addImmediateCollision(@Nonnull Vector3d pos, @Nonnull CollisionResult result, @Nonnull CollisionConfig coll, int i)`
  - Executes `addImmediateCollision` behavior.
- `isBelowMovementThreshold(@Nonnull Vector3d v)`
  - Executes `isBelowMovementThreshold` behavior.
- `logOverlap(@Nonnull Vector3d pos, @Nonnull Box collider, @Nonnull CollisionConfig coll, @Nonnull Box hitBox, int x, int y, int z, int index, int intersectType)`
  - Executes `logOverlap` behavior.

## Notes
- No additional notes.
