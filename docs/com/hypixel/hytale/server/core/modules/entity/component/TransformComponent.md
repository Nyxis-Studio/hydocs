# TransformComponent

## Overview
- Documentation for `TransformComponent`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entity.component`.

## Constructors
- `TransformComponent()`
  - Creates a `TransformComponent` instance.
- `TransformComponent(@Nonnull Vector3d position, @Nonnull Vector3f rotation)`
  - Creates a `TransformComponent` instance.
- `TransformComponent(this.position, this.rotation)`
  - Creates a `TransformComponent` instance.

## Methods
- `getComponentType()`
  - Executes `getComponentType` behavior.
- `getPosition()`
  - Executes `getPosition` behavior.
- `setPosition(@Nonnull Vector3d position)`
  - Executes `setPosition` behavior.
- `teleportPosition(@Nonnull Vector3d position)`
  - Executes `teleportPosition` behavior.
- `getRotation()`
  - Executes `getRotation` behavior.
- `setRotation(@Nonnull Vector3f rotation)`
  - Executes `setRotation` behavior.
- `getTransform()`
  - Executes `getTransform` behavior.
- `teleportRotation(@Nonnull Vector3f rotation)`
  - Executes `teleportRotation` behavior.
- `getSentTransform()`
  - Executes `getSentTransform` behavior.
- `getChunk()`
  - Executes `getChunk` behavior.
- `getChunkRef()`
  - Executes `getChunkRef` behavior.
- `markChunkDirty(@Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `markChunkDirty` behavior.
- `setChunkLocation(@Nullable Ref<ChunkStore> chunkRef, @Nullable WorldChunk chunk)`
  - Executes `setChunkLocation` behavior.
- `clone()`
  - Executes `clone` behavior.

## Notes
- No additional notes.
