# InstanceBlock

## Overview
- Documentation for `InstanceBlock`.
- Declared as a class in `com.hypixel.hytale.builtin.instances.blocks`.

## Constructors
- `InstanceBlock()`
  - Creates a `InstanceBlock` instance.
- `InstanceBlock(UUID worldUUID, boolean closeOnRemove)`
  - Creates a `InstanceBlock` instance.
- `InstanceBlock(this.worldUUID, this.closeOnRemove)`
  - Creates a `InstanceBlock` instance.

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
