# ConfigurableInstanceBlock

## Overview
- Documentation for `ConfigurableInstanceBlock`.
- Declared as a class in `com.hypixel.hytale.builtin.instances.blocks`.

## Constructors
- `ConfigurableInstanceBlock()`
  - Creates a `ConfigurableInstanceBlock` instance.
- `ConfigurableInstanceBlock(UUID worldUUID, boolean closeOnRemove, String instanceName, String instanceKey, @Nullable Vector3d positionOffset, @Nullable Vector3f rotation, boolean personalReturnPoint, double removeBlockAfter)`
  - Creates a `ConfigurableInstanceBlock` instance.
- `ConfigurableInstanceBlock(this.worldUUID, this.closeOnRemove, this.instanceName, this.instanceKey, this.positionOffset, this.rotation, this.personalReturnPoint, this.removeBlockAfter)`
  - Creates a `ConfigurableInstanceBlock` instance.

## Methods
- `getComponentType()`
  - Executes `getComponentType` behavior.
- `getWorldUUID()`
  - Executes `getWorldUUID` behavior.
- `setWorldUUID(UUID worldUUID)`
  - Executes `setWorldUUID` behavior.
- `getWorldFuture()`
  - Executes `getWorldFuture` behavior.
- `setWorldFuture(CompletableFuture<World> worldFuture)`
  - Executes `setWorldFuture` behavior.
- `isCloseOnRemove()`
  - Executes `isCloseOnRemove` behavior.
- `setCloseOnRemove(boolean closeOnRemove)`
  - Executes `setCloseOnRemove` behavior.
- `getInstanceName()`
  - Executes `getInstanceName` behavior.
- `setInstanceName(@Nonnull String instanceName)`
  - Executes `setInstanceName` behavior.
- `getInstanceKey()`
  - Executes `getInstanceKey` behavior.
- `setInstanceKey(@Nonnull String instanceKey)`
  - Executes `setInstanceKey` behavior.
- `getPositionOffset()`
  - Executes `getPositionOffset` behavior.
- `setPositionOffset(@Nullable Vector3d positionOffset)`
  - Executes `setPositionOffset` behavior.
- `getRotation()`
  - Executes `getRotation` behavior.
- `setRotation(@Nullable Vector3f rotation)`
  - Executes `setRotation` behavior.
- `isPersonalReturnPoint()`
  - Executes `isPersonalReturnPoint` behavior.
- `setPersonalReturnPoint(boolean personalReturnPoint)`
  - Executes `setPersonalReturnPoint` behavior.
- `getRemoveBlockAfter()`
  - Executes `getRemoveBlockAfter` behavior.
- `setRemoveBlockAfter(double removeBlockAfter)`
  - Executes `setRemoveBlockAfter` behavior.
- `clone()`
  - Executes `clone` behavior.
- `onEntityAdded(@Nonnull Ref<ChunkStore> ref, @Nonnull AddReason reason, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<ChunkStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `onEntityRemove` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.

## Notes
- No additional notes.
