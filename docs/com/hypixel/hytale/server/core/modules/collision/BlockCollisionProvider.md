**Source Hash:** `d960ae5cc9ec4be2c5ca867cdb0a12ab33891867703a44bcc7e087b2c533bbf0`

# BlockCollisionProvider

## Overview

## Constructor Descriptions
- `none()`: No documented methods.

## Method Descriptions
- `setRequestedCollisionMaterials(int requestedCollisionMaterials)`: Add description.
  - Executes `setRequestedCollisionMaterials` behavior.
- `setReportOverlaps(boolean reportOverlaps)`: Add description.
  - Executes `setReportOverlaps` behavior.
- `next()`: Add description.
  - Executes `next` behavior.
- `accept(long x, long y, long z)`: Add description.
  - Executes `accept` behavior.
- `cast(@Nonnull World world, @Nonnull Box collider, @Nonnull Vector3d pos, @Nonnull Vector3d v, @Nonnull IBlockCollisionConsumer collisionConsumer, @Nonnull IBlockTracker activeTriggers, double collisionStop)`: Add description.
  - Executes `cast` behavior.
- `castShortDistance(@Nonnull Box collider, @Nonnull Vector3d pos, @Nonnull Vector3d v)`: Add description.
  - Executes `castShortDistance` behavior.
- `processBlockStatic(int x, int y, int z)`: Add description.
  - Executes `processBlockStatic` behavior.
- `processBlockStaticFluid(int x, int y, int z, @Nonnull Fluid fluid, boolean submergeFluid)`: Add description.
  - Executes `processBlockStaticFluid` behavior.
- `canCollide()`: Add description.
  - Executes `canCollide` behavior.
- `canCollide(int collisionMaterials)`: Add description.
  - Executes `canCollide` behavior.
- `castIterative(@Nonnull Box collider, @Nonnull Vector3d pos, @Nonnull Vector3d v, double collisionStop)`: Add description.
  - Executes `castIterative` behavior.
- `onSliceFinished()`: Add description.
  - Executes `onSliceFinished` behavior.
- `processBlockDynamic(int x, int y, int z)`: Add description.
  - Executes `processBlockDynamic` behavior.
- `processBlockDynamicFluid(int x, int y, int z, @Nonnull Fluid fluid, BlockContactData damageCollisionData, boolean isSubmergeFluid)`: Add description.
  - Executes `processBlockDynamicFluid` behavior.
- `processTriggerDynamic(int blockX, int blockY, int blockZ, @Nullable BlockContactData collisionData)`: Add description.
  - Executes `processTriggerDynamic` behavior.
- `processDamageDynamic(int blockX, int blockY, int blockZ, @Nullable BlockContactData collisionData)`: Add description.
  - Executes `processDamageDynamic` behavior.
- `updateStopDistance(@Nullable IBlockCollisionConsumer.Result result)`: Add description.
  - Executes `updateStopDistance` behavior.
- `generateTriggerExit()`: Add description.
  - Executes `generateTriggerExit` behavior.

## Notes
- No additional notes.
