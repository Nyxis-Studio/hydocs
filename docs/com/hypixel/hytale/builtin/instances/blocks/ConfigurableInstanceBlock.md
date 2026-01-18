**Source Hash:** `d3ccf947b694006a70f84409f42ea20279693aa3d9d3ffe4a9c7db6fa12573f0`

# ConfigurableInstanceBlock

## Overview

## Constructor Descriptions
- `ConfigurableInstanceBlock()`
  - Creates a `ConfigurableInstanceBlock` instance.
- `ConfigurableInstanceBlock(UUID worldUUID, boolean closeOnRemove, String instanceName, String instanceKey, @Nullable Vector3d positionOffset, @Nullable Vector3f rotation, boolean personalReturnPoint, double removeBlockAfter)`
  - Creates a `ConfigurableInstanceBlock` instance.
- `ConfigurableInstanceBlock(this.worldUUID, this.closeOnRemove, this.instanceName, this.instanceKey, this.positionOffset, this.rotation, this.personalReturnPoint, this.removeBlockAfter)`
  - Creates a `ConfigurableInstanceBlock` instance.

## Method Descriptions
- `getComponentType()`: Add description.
  - Executes `getComponentType` behavior.
- `getWorldUUID()`: Add description.
  - Executes `getWorldUUID` behavior.
- `setWorldUUID(UUID worldUUID)`: Add description.
  - Executes `setWorldUUID` behavior.
- `getWorldFuture()`: Add description.
  - Executes `getWorldFuture` behavior.
- `setWorldFuture(CompletableFuture<World> worldFuture)`: Add description.
  - Executes `setWorldFuture` behavior.
- `isCloseOnRemove()`: Add description.
  - Executes `isCloseOnRemove` behavior.
- `setCloseOnRemove(boolean closeOnRemove)`: Add description.
  - Executes `setCloseOnRemove` behavior.
- `getInstanceName()`: Add description.
  - Executes `getInstanceName` behavior.
- `setInstanceName(@Nonnull String instanceName)`: Add description.
  - Executes `setInstanceName` behavior.
- `getInstanceKey()`: Add description.
  - Executes `getInstanceKey` behavior.
- `setInstanceKey(@Nonnull String instanceKey)`: Add description.
  - Executes `setInstanceKey` behavior.
- `getPositionOffset()`: Add description.
  - Executes `getPositionOffset` behavior.
- `setPositionOffset(@Nullable Vector3d positionOffset)`: Add description.
  - Executes `setPositionOffset` behavior.
- `getRotation()`: Add description.
  - Executes `getRotation` behavior.
- `setRotation(@Nullable Vector3f rotation)`: Add description.
  - Executes `setRotation` behavior.
- `isPersonalReturnPoint()`: Add description.
  - Executes `isPersonalReturnPoint` behavior.
- `setPersonalReturnPoint(boolean personalReturnPoint)`: Add description.
  - Executes `setPersonalReturnPoint` behavior.
- `getRemoveBlockAfter()`: Add description.
  - Executes `getRemoveBlockAfter` behavior.
- `setRemoveBlockAfter(double removeBlockAfter)`: Add description.
  - Executes `setRemoveBlockAfter` behavior.
- `clone()`: Add description.
  - Executes `clone` behavior.
- `onEntityAdded(@Nonnull Ref<ChunkStore> ref, @Nonnull AddReason reason, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`: Add description.
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<ChunkStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`: Add description.
  - Executes `onEntityRemove` behavior.
- `getQuery()`: Add description.
  - Executes `getQuery` behavior.

## Notes
- No additional notes.
