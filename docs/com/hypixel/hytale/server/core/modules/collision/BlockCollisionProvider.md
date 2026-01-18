# BlockCollisionProvider

## Overview
- Documentation for `BlockCollisionProvider`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.collision`.

## Constructors
- None.

## Methods
- `setRequestedCollisionMaterials(int requestedCollisionMaterials)`
  - Executes `setRequestedCollisionMaterials` behavior.
- `setReportOverlaps(boolean reportOverlaps)`
  - Executes `setReportOverlaps` behavior.
- `next()`
  - Executes `next` behavior.
- `accept(long x, long y, long z)`
  - Executes `accept` behavior.
- `cast(@Nonnull World world, @Nonnull Box collider, @Nonnull Vector3d pos, @Nonnull Vector3d v, @Nonnull IBlockCollisionConsumer collisionConsumer, @Nonnull IBlockTracker activeTriggers, double collisionStop)`
  - Executes `cast` behavior.
- `castShortDistance(@Nonnull Box collider, @Nonnull Vector3d pos, @Nonnull Vector3d v)`
  - Executes `castShortDistance` behavior.
- `processBlockStatic(int x, int y, int z)`
  - Executes `processBlockStatic` behavior.
- `processBlockStaticFluid(int x, int y, int z, @Nonnull Fluid fluid, boolean submergeFluid)`
  - Executes `processBlockStaticFluid` behavior.
- `canCollide()`
  - Executes `canCollide` behavior.
- `canCollide(int collisionMaterials)`
  - Executes `canCollide` behavior.
- `castIterative(@Nonnull Box collider, @Nonnull Vector3d pos, @Nonnull Vector3d v, double collisionStop)`
  - Executes `castIterative` behavior.
- `onSliceFinished()`
  - Executes `onSliceFinished` behavior.
- `processBlockDynamic(int x, int y, int z)`
  - Executes `processBlockDynamic` behavior.
- `processBlockDynamicFluid(int x, int y, int z, @Nonnull Fluid fluid, BlockContactData damageCollisionData, boolean isSubmergeFluid)`
  - Executes `processBlockDynamicFluid` behavior.
- `processTriggerDynamic(int blockX, int blockY, int blockZ, @Nullable BlockContactData collisionData)`
  - Executes `processTriggerDynamic` behavior.
- `processDamageDynamic(int blockX, int blockY, int blockZ, @Nullable BlockContactData collisionData)`
  - Executes `processDamageDynamic` behavior.
- `updateStopDistance(@Nullable IBlockCollisionConsumer.Result result)`
  - Executes `updateStopDistance` behavior.
- `generateTriggerExit()`
  - Executes `generateTriggerExit` behavior.

## Notes
- No additional notes.
