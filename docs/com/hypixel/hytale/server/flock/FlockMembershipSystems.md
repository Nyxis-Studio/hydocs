# FlockMembershipSystems

## Overview
- Documentation for `FlockMembershipSystems`.
- Declared as a class in `com.hypixel.hytale.server.flock`.

## Constructors
- None.

## Methods
- `canJoinFlock(@Nonnull Ref<EntityStore> reference, @Nonnull Ref<EntityStore> flockReference, @Nonnull Store<EntityStore> store)`
  - Executes `canJoinFlock` behavior.
- `join(@Nonnull Ref<EntityStore> ref, @Nonnull Ref<EntityStore> flockRef, @Nonnull Store<EntityStore> store)`
  - Executes `join` behavior.
- `canBecomeLeader(@Nonnull Ref<EntityStore> ref)`
  - Executes `canBecomeLeader` behavior.
- `markChunkNeedsSaving(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store)`
  - Executes `markChunkNeedsSaving` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `getGroup()`
  - Executes `getGroup` behavior.
- `onEntityAdd(@Nonnull Holder<EntityStore> holder, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<EntityStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityRemoved` behavior.
- `handle(int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Damage damage)`
  - Executes `handle` behavior.
- `handle(int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Damage danage)`
  - Executes `handle` behavior.
- `componentType()`
  - Executes `componentType` behavior.
- `onComponentAdded(@Nonnull Ref<EntityStore> ref, @Nonnull FlockMembership component, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentAdded` behavior.
- `onComponentSet(@Nonnull Ref<EntityStore> ref, FlockMembership oldComponent, @Nonnull FlockMembership newComponent, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentSet` behavior.
- `onComponentRemoved(@Nonnull Ref<EntityStore> ref, @Nonnull FlockMembership component, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentRemoved` behavior.
- `doJoin(@Nonnull Ref<EntityStore> ref, @Nonnull FlockMembership membershipComponent, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `doJoin` behavior.
- `doLeave(@Nonnull Ref<EntityStore> ref, @Nonnull FlockMembership membershipComponent, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `doLeave` behavior.
- `setNewLeader(@Nonnull UUID flockId, @Nonnull EntityGroup entityGroup, @Nonnull Flock flock, @Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `setNewLeader` behavior.
- `onEntityAdded(@Nonnull Ref<EntityStore> ref, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityAdded` behavior.
- `joinOrCreateFlock(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store)`
  - Executes `joinOrCreateFlock` behavior.
- `onEntityRemove(@Nonnull Ref<EntityStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityRemove` behavior.
- `markNeedsSave(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull Flock flockComponent)`
  - Executes `markNeedsSave` behavior.
- `setInterimLeader(@Nonnull Store<EntityStore> store, @Nonnull FlockMembership interimLeaderMembership, @Nonnull EntityGroup entityGroup, Ref<EntityStore> interimLeader, @Nonnull Flock flockComponent, @Nonnull UUID flockId)`
  - Executes `setInterimLeader` behavior.

## Notes
- No additional notes.
