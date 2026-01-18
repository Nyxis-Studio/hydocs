**Source Hash:** `4199539fe3e8a466bb0618ad5e75e46840b156c847a14ce4473d5388132d2219`

# EntityChunk

## Overview

## Constructor Descriptions
- `EntityChunk()`
  - Creates a `EntityChunk` instance.
- `EntityChunk(@Nonnull List<Holder<EntityStore>> entityHolders, @Nonnull Set<Ref<EntityStore>> entityReferences)`
  - Creates a `EntityChunk` instance.
- `EntityChunk(entityHoldersClone, new HashSet<Ref<EntityStore>>()`
  - Creates a `EntityChunk` instance.

## Method Descriptions
- `getComponentType()`: Add description.
  - Executes `getComponentType` behavior.
- `clone()`: Add description.
  - Executes `clone` behavior.
- `cloneSerializable()`: Add description.
  - Executes `cloneSerializable` behavior.
- `getEntityHolders()`: Add description.
  - Executes `getEntityHolders` behavior.
- `addEntityHolder(@Nonnull Holder<EntityStore> holder)`: Add description.
  - Executes `addEntityHolder` behavior.
- `storeEntityHolder(@Nonnull Holder<EntityStore> holder)`: Add description.
  - Executes `storeEntityHolder` behavior.
- `getEntityReferences()`: Add description.
  - Executes `getEntityReferences` behavior.
- `addEntityReference(@Nonnull Ref<EntityStore> reference)`: Add description.
  - Executes `addEntityReference` behavior.
- `loadEntityReference(@Nonnull Ref<EntityStore> reference)`: Add description.
  - Executes `loadEntityReference` behavior.
- `removeEntityReference(@Nonnull Ref<EntityStore> reference)`: Add description.
  - Executes `removeEntityReference` behavior.
- `unloadEntityReference(@Nonnull Ref<EntityStore> reference)`: Add description.
  - Executes `unloadEntityReference` behavior.
- `takeEntityHolders()`: Add description.
  - Executes `takeEntityHolders` behavior.
- `takeEntityReferences()`: Add description.
  - Executes `takeEntityReferences` behavior.
- `getNeedsSaving()`: Add description.
  - Executes `getNeedsSaving` behavior.
- `markNeedsSaving()`: Add description.
  - Executes `markNeedsSaving` behavior.
- `consumeNeedsSaving()`: Add description.
  - Executes `consumeNeedsSaving` behavior.
- `getEntities()`: Add description.
  - Executes `getEntities` behavior.
- `hasNext()`: Add description.
  - Executes `hasNext` behavior.
- `next()`: Add description.
  - Executes `next` behavior.
- `getQuery()`: Add description.
  - Executes `getQuery` behavior.
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
