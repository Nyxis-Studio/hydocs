**Source Hash:** `037a9ae6c08835302dac9323a6a0ca0c891b94dc0b9a5ced05f07639148efbef`

# FlockMembershipSystems

## Overview

## Constructor Descriptions
- `none()`: No documented methods.

## Method Descriptions
- `canJoinFlock(@Nonnull Ref<EntityStore> reference, @Nonnull Ref<EntityStore> flockReference, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `canJoinFlock` behavior.
- `join(@Nonnull Ref<EntityStore> ref, @Nonnull Ref<EntityStore> flockRef, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `join` behavior.
- `canBecomeLeader(@Nonnull Ref<EntityStore> ref)`: Add description.
  - Executes `canBecomeLeader` behavior.
- `markChunkNeedsSaving(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `markChunkNeedsSaving` behavior.
- `getQuery()`: Add description.
  - Executes `getQuery` behavior.
- `getGroup()`: Add description.
  - Executes `getGroup` behavior.
- `onEntityAdd(@Nonnull Holder<EntityStore> holder, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<EntityStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `onEntityRemoved` behavior.
- `handle(int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Damage damage)`: Add description.
  - Executes `handle` behavior.
- `handle(int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Damage danage)`: Add description.
  - Executes `handle` behavior.
- `componentType()`: Add description.
  - Executes `componentType` behavior.
- `onComponentAdded(@Nonnull Ref<EntityStore> ref, @Nonnull FlockMembership component, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `onComponentAdded` behavior.
- `onComponentSet(@Nonnull Ref<EntityStore> ref, FlockMembership oldComponent, @Nonnull FlockMembership newComponent, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `onComponentSet` behavior.
- `onComponentRemoved(@Nonnull Ref<EntityStore> ref, @Nonnull FlockMembership component, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `onComponentRemoved` behavior.
- `doJoin(@Nonnull Ref<EntityStore> ref, @Nonnull FlockMembership membershipComponent, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `doJoin` behavior.
- `doLeave(@Nonnull Ref<EntityStore> ref, @Nonnull FlockMembership membershipComponent, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `doLeave` behavior.
- `setNewLeader(@Nonnull UUID flockId, @Nonnull EntityGroup entityGroup, @Nonnull Flock flock, @Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `setNewLeader` behavior.
- `onEntityAdded(@Nonnull Ref<EntityStore> ref, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `onEntityAdded` behavior.
- `joinOrCreateFlock(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `joinOrCreateFlock` behavior.
- `onEntityRemove(@Nonnull Ref<EntityStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `onEntityRemove` behavior.
- `markNeedsSave(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull Flock flockComponent)`: Add description.
  - Executes `markNeedsSave` behavior.
- `setInterimLeader(@Nonnull Store<EntityStore> store, @Nonnull FlockMembership interimLeaderMembership, @Nonnull EntityGroup entityGroup, Ref<EntityStore> interimLeader, @Nonnull Flock flockComponent, @Nonnull UUID flockId)`: Add description.
  - Executes `setInterimLeader` behavior.

## Notes
- No additional notes.
