**Source Hash:** `6100022cf4cf60187968fb73b54aace9745b4626c2184962a763933230523151`

# BlockComponentChunk

## Overview

## Constructor Descriptions
- `BlockComponentChunk()`
  - Creates a `BlockComponentChunk` instance.
- `BlockComponentChunk(@Nonnull Int2ObjectMap<Holder<ChunkStore>> entityHolders, @Nonnull Int2ObjectMap<Ref<ChunkStore>> entityReferences)`
  - Creates a `BlockComponentChunk` instance.
- `BlockComponentChunk(entityHoldersClone, new Int2ObjectOpenHashMap<Ref<ChunkStore>>()`
  - Creates a `BlockComponentChunk` instance.

## Method Descriptions
- `getComponentType()`: Add description.
  - Executes `getComponentType` behavior.
- `clone()`: Add description.
  - Executes `clone` behavior.
- `cloneSerializable()`: Add description.
  - Executes `cloneSerializable` behavior.
- `getEntityHolders()`: Add description.
  - Executes `getEntityHolders` behavior.
- `getEntityHolder(int index)`: Add description.
  - Executes `getEntityHolder` behavior.
- `addEntityHolder(int index, @Nonnull Holder<ChunkStore> holder)`: Add description.
  - Executes `addEntityHolder` behavior.
- `storeEntityHolder(int index, @Nonnull Holder<ChunkStore> holder)`: Add description.
  - Executes `storeEntityHolder` behavior.
- `removeEntityHolder(int index)`: Add description.
  - Executes `removeEntityHolder` behavior.
- `getEntityReferences()`: Add description.
  - Executes `getEntityReferences` behavior.
- `getEntityReference(int index)`: Add description.
  - Executes `getEntityReference` behavior.
- `addEntityReference(int index, @Nonnull Ref<ChunkStore> reference)`: Add description.
  - Executes `addEntityReference` behavior.
- `loadEntityReference(int index, @Nonnull Ref<ChunkStore> reference)`: Add description.
  - Executes `loadEntityReference` behavior.
- `removeEntityReference(int index, Ref<ChunkStore> reference)`: Add description.
  - Executes `removeEntityReference` behavior.
- `unloadEntityReference(int index, Ref<ChunkStore> reference)`: Add description.
  - Executes `unloadEntityReference` behavior.
- `takeEntityHolders()`: Add description.
  - Executes `takeEntityHolders` behavior.
- `takeEntityReferences()`: Add description.
  - Executes `takeEntityReferences` behavior.
- `getComponent(int index, @Nonnull ComponentType<ChunkStore, T> componentType)`: Add description.
  - Executes `getComponent` behavior.
- `hasComponents(int index)`: Add description.
  - Executes `hasComponents` behavior.
- `getNeedsSaving()`: Add description.
  - Executes `getNeedsSaving` behavior.
- `markNeedsSaving()`: Add description.
  - Executes `markNeedsSaving` behavior.
- `consumeNeedsSaving()`: Add description.
  - Executes `consumeNeedsSaving` behavior.
- `getQuery()`: Add description.
  - Executes `getQuery` behavior.
- `fetch(int index, @Nonnull ArchetypeChunk<ChunkStore> archetypeChunk, @Nonnull Store<ChunkStore> store, CommandBuffer<ChunkStore> commandBuffer, PlayerRef player, @Nonnull List<Packet> results)`: Add description.
  - Executes `fetch` behavior.
- `componentType()`: Add description.
  - Executes `componentType` behavior.
- `onComponentAdded(@Nonnull Ref<ChunkStore> ref, @Nonnull NonTicking<ChunkStore> component, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`: Add description.
  - Executes `onComponentAdded` behavior.
- `onComponentSet(@Nonnull Ref<ChunkStore> ref, NonTicking<ChunkStore> oldComponent, @Nonnull NonTicking<ChunkStore> newComponent, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`: Add description.
  - Executes `onComponentSet` behavior.
- `onComponentRemoved(@Nonnull Ref<ChunkStore> ref, @Nonnull NonTicking<ChunkStore> component, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`: Add description.
  - Executes `onComponentRemoved` behavior.

## Notes
- No additional notes.
