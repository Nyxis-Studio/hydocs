# TargetUtil

## Overview
- Documentation for `TargetUtil`.
- Declared as a class in `com.hypixel.hytale.server.core.util`.

## Constructors
- None.

## Methods
- `getTargetBlock(@Nonnull World world, @Nonnull BiIntPredicate blockIdPredicate, double originX, double originY, double originZ, double directionX, double directionY, double directionZ, double maxDistance)`
  - Executes `getTargetBlock` behavior.
- `getTargetLocation(@Nonnull World world, @Nonnull IntPredicate blockIdPredicate, double originX, double originY, double originZ, double directionX, double directionY, double directionZ, double maxDistance)`
  - Executes `getTargetLocation` behavior.
- `getTargetBlockAvoidLocations(@Nonnull World world, @Nonnull IntPredicate blockIdPredicate, double originX, double originY, double originZ, double directionX, double directionY, double directionZ, double maxDistance, @Nonnull LinkedList<LongOpenHashSet> blocksToIgnore)`
  - Executes `getTargetBlockAvoidLocations` behavior.
- `getTargetBlock(@Nonnull Ref<EntityStore> ref, double maxDistance, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getTargetBlock` behavior.
- `getTargetBlock(@Nonnull Ref<EntityStore> ref, @Nonnull IntPredicate blockIdPredicate, double maxDistance, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getTargetBlock` behavior.
- `getTargetLocation(@Nonnull Ref<EntityStore> ref, double maxDistance, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getTargetLocation` behavior.
- `getTargetLocation(@Nonnull Ref<EntityStore> ref, @Nonnull IntPredicate blockIdPredicate, double maxDistance, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getTargetLocation` behavior.
- `getTargetLocation(@Nonnull Transform transform, @Nonnull IntPredicate blockIdPredicate, double maxDistance, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getTargetLocation` behavior.
- `getAllEntitiesInSphere(@Nonnull Vector3d position, double radius, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getAllEntitiesInSphere` behavior.
- `getAllEntitiesInCylinder(@Nonnull Vector3d position, double radius, double height, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getAllEntitiesInCylinder` behavior.
- `getAllEntitiesInBox(@Nonnull Vector3d min, @Nonnull Vector3d max, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getAllEntitiesInBox` behavior.
- `getTargetEntity(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getTargetEntity` behavior.
- `getTargetEntity(@Nonnull Ref<EntityStore> ref, float radius, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getTargetEntity` behavior.
- `getLook(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getLook` behavior.
- `isHitByRay(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d rayStart, @Nonnull Vector3d rayDir, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `isHitByRay` behavior.
- `updateChunk(int blockX, int blockZ)`
  - Executes `updateChunk` behavior.

## Notes
- No additional notes.
