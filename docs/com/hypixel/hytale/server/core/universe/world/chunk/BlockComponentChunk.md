# BlockComponentChunk

## Overview
- Documentation for `BlockComponentChunk`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.chunk`.

## Constructors
- `BlockComponentChunk()`
  - Creates a `BlockComponentChunk` instance.
- `BlockComponentChunk(@Nonnull Int2ObjectMap<Holder<ChunkStore>> entityHolders, @Nonnull Int2ObjectMap<Ref<ChunkStore>> entityReferences)`
  - Creates a `BlockComponentChunk` instance.
- `BlockComponentChunk(entityHoldersClone, new Int2ObjectOpenHashMap<Ref<ChunkStore>>()`
  - Creates a `BlockComponentChunk` instance.

## Methods
- `getComponentType()`
  - Executes `getComponentType` behavior.
- `clone()`
  - Executes `clone` behavior.
- `cloneSerializable()`
  - Executes `cloneSerializable` behavior.
- `getEntityHolders()`
  - Executes `getEntityHolders` behavior.
- `getEntityHolder(int index)`
  - Executes `getEntityHolder` behavior.
- `addEntityHolder(int index, @Nonnull Holder<ChunkStore> holder)`
  - Executes `addEntityHolder` behavior.
- `storeEntityHolder(int index, @Nonnull Holder<ChunkStore> holder)`
  - Executes `storeEntityHolder` behavior.
- `removeEntityHolder(int index)`
  - Executes `removeEntityHolder` behavior.
- `getEntityReferences()`
  - Executes `getEntityReferences` behavior.
- `getEntityReference(int index)`
  - Executes `getEntityReference` behavior.
- `addEntityReference(int index, @Nonnull Ref<ChunkStore> reference)`
  - Executes `addEntityReference` behavior.
- `loadEntityReference(int index, @Nonnull Ref<ChunkStore> reference)`
  - Executes `loadEntityReference` behavior.
- `removeEntityReference(int index, Ref<ChunkStore> reference)`
  - Executes `removeEntityReference` behavior.
- `unloadEntityReference(int index, Ref<ChunkStore> reference)`
  - Executes `unloadEntityReference` behavior.
- `takeEntityHolders()`
  - Executes `takeEntityHolders` behavior.
- `takeEntityReferences()`
  - Executes `takeEntityReferences` behavior.
- `getComponent(int index, @Nonnull ComponentType<ChunkStore, T> componentType)`
  - Executes `getComponent` behavior.
- `hasComponents(int index)`
  - Executes `hasComponents` behavior.
- `getNeedsSaving()`
  - Executes `getNeedsSaving` behavior.
- `markNeedsSaving()`
  - Executes `markNeedsSaving` behavior.
- `consumeNeedsSaving()`
  - Executes `consumeNeedsSaving` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `fetch(int index, @Nonnull ArchetypeChunk<ChunkStore> archetypeChunk, @Nonnull Store<ChunkStore> store, CommandBuffer<ChunkStore> commandBuffer, PlayerRef player, @Nonnull List<Packet> results)`
  - Executes `fetch` behavior.
- `componentType()`
  - Executes `componentType` behavior.
- `onComponentAdded(@Nonnull Ref<ChunkStore> ref, @Nonnull NonTicking<ChunkStore> component, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `onComponentAdded` behavior.
- `onComponentSet(@Nonnull Ref<ChunkStore> ref, NonTicking<ChunkStore> oldComponent, @Nonnull NonTicking<ChunkStore> newComponent, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `onComponentSet` behavior.
- `onComponentRemoved(@Nonnull Ref<ChunkStore> ref, @Nonnull NonTicking<ChunkStore> component, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `onComponentRemoved` behavior.

## Notes
- No additional notes.
