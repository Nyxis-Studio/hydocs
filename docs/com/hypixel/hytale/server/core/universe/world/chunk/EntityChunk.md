# EntityChunk

## Overview
- Documentation for `EntityChunk`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.chunk`.

## Constructors
- `EntityChunk()`
  - Creates a `EntityChunk` instance.
- `EntityChunk(@Nonnull List<Holder<EntityStore>> entityHolders, @Nonnull Set<Ref<EntityStore>> entityReferences)`
  - Creates a `EntityChunk` instance.
- `EntityChunk(entityHoldersClone, new HashSet<Ref<EntityStore>>()`
  - Creates a `EntityChunk` instance.

## Methods
- `getComponentType()`
  - Executes `getComponentType` behavior.
- `clone()`
  - Executes `clone` behavior.
- `cloneSerializable()`
  - Executes `cloneSerializable` behavior.
- `getEntityHolders()`
  - Executes `getEntityHolders` behavior.
- `addEntityHolder(@Nonnull Holder<EntityStore> holder)`
  - Executes `addEntityHolder` behavior.
- `storeEntityHolder(@Nonnull Holder<EntityStore> holder)`
  - Executes `storeEntityHolder` behavior.
- `getEntityReferences()`
  - Executes `getEntityReferences` behavior.
- `addEntityReference(@Nonnull Ref<EntityStore> reference)`
  - Executes `addEntityReference` behavior.
- `loadEntityReference(@Nonnull Ref<EntityStore> reference)`
  - Executes `loadEntityReference` behavior.
- `removeEntityReference(@Nonnull Ref<EntityStore> reference)`
  - Executes `removeEntityReference` behavior.
- `unloadEntityReference(@Nonnull Ref<EntityStore> reference)`
  - Executes `unloadEntityReference` behavior.
- `takeEntityHolders()`
  - Executes `takeEntityHolders` behavior.
- `takeEntityReferences()`
  - Executes `takeEntityReferences` behavior.
- `getNeedsSaving()`
  - Executes `getNeedsSaving` behavior.
- `markNeedsSaving()`
  - Executes `markNeedsSaving` behavior.
- `consumeNeedsSaving()`
  - Executes `consumeNeedsSaving` behavior.
- `getEntities()`
  - Executes `getEntities` behavior.
- `hasNext()`
  - Executes `hasNext` behavior.
- `next()`
  - Executes `next` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
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
