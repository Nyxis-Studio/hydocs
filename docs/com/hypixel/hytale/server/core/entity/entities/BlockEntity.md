# BlockEntity

## Overview
- Documentation for `BlockEntity`.
- Declared as a class in `com.hypixel.hytale.server.core.entity.entities`.

## Constructors
- `BlockEntity()`
  - Creates a `BlockEntity` instance.
- `BlockEntity(String blockTypeKey)`
  - Creates a `BlockEntity` instance.
- `BlockEntity(blockTypeKey)`
  - Creates a `BlockEntity` instance.
- `BlockEntity(this.blockTypeKey)`
  - Creates a `BlockEntity` instance.

## Methods
- `getComponentType()`
  - Executes `getComponentType` behavior.
- `assembleDefaultBlockEntity(@Nonnull TimeResource time, String blockTypeKey, @Nonnull Vector3d position)`
  - Executes `assembleDefaultBlockEntity` behavior.
- `initPhysics(@Nonnull BoundingBox boundingBox)`
  - Executes `initPhysics` behavior.
- `updateHitbox(@Nonnull Ref<EntityStore> ref, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `updateHitbox` behavior.
- `createBoundingBoxComponent()`
  - Executes `createBoundingBoxComponent` behavior.
- `setBlockTypeKey(String blockTypeKey, @Nonnull Ref<EntityStore> ref, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `setBlockTypeKey` behavior.
- `getSimplePhysicsProvider()`
  - Executes `getSimplePhysicsProvider` behavior.
- `getBlockTypeKey()`
  - Executes `getBlockTypeKey` behavior.
- `addForce(float x, float y, float z)`
  - Executes `addForce` behavior.
- `addForce(@Nonnull Vector3d force)`
  - Executes `addForce` behavior.
- `consumeBlockIdNetworkOutdated()`
  - Executes `consumeBlockIdNetworkOutdated` behavior.
- `clone()`
  - Executes `clone` behavior.

## Notes
- No additional notes.
