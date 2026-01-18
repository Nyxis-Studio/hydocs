# BlockState

## Overview
- Documentation for `BlockState`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.meta`.

## Constructors
- None.

## Methods
- `setReference(Ref<ChunkStore> reference)`
  - Executes `setReference` behavior.
- `getReference()`
  - Executes `getReference` behavior.
- `unloadFromWorld()`
  - Executes `unloadFromWorld` behavior.
- `initialize(BlockType blockType)`
  - Executes `initialize` behavior.
- `onUnload()`
  - Executes `onUnload` behavior.
- `validateInitialized()`
  - Executes `validateInitialized` behavior.
- `getIndex()`
  - Executes `getIndex` behavior.
- `setPosition(WorldChunk chunk, @Nullable Vector3i position)`
  - Executes `setPosition` behavior.
- `setPosition(@Nonnull Vector3i position)`
  - Executes `setPosition` behavior.
- `getPosition()`
  - Executes `getPosition` behavior.
- `__internal_getPosition()`
  - Executes `__internal_getPosition` behavior.
- `getBlockX()`
  - Executes `getBlockX` behavior.
- `getBlockY()`
  - Executes `getBlockY` behavior.
- `getBlockZ()`
  - Executes `getBlockZ` behavior.
- `getBlockPosition()`
  - Executes `getBlockPosition` behavior.
- `getCenteredBlockPosition()`
  - Executes `getCenteredBlockPosition` behavior.
- `getChunk()`
  - Executes `getChunk` behavior.
- `getBlockType()`
  - Executes `getBlockType` behavior.
- `getRotationIndex()`
  - Executes `getRotationIndex` behavior.
- `invalidate()`
  - Executes `invalidate` behavior.
- `markNeedsSave()`
  - Executes `markNeedsSave` behavior.
- `saveToDocument()`
  - Executes `saveToDocument` behavior.
- `clone()`
  - Executes `clone` behavior.
- `toHolder()`
  - Executes `toHolder` behavior.
- `load(BsonDocument doc, @Nonnull WorldChunk chunk, @Nonnull Vector3i pos)`
  - Executes `load` behavior.
- `load(BsonDocument doc, @Nullable WorldChunk chunk, Vector3i pos, BlockType blockType)`
  - Executes `load` behavior.
- `ensureState(@Nonnull WorldChunk worldChunk, int x, int y, int z)`
  - Executes `ensureState` behavior.
- `getBlockState(@Nullable Ref<ChunkStore> reference, @Nonnull ComponentAccessor<ChunkStore> componentAccessor)`
  - Executes `getBlockState` behavior.
- `getBlockState(int index, @Nonnull ArchetypeChunk<ChunkStore> archetypeChunk)`
  - Executes `getBlockState` behavior.
- `getBlockState(@Nonnull Holder<ChunkStore> holder)`
  - Executes `getBlockState` behavior.
- `findComponentType(@Nonnull Archetype<ChunkStore> archetype, @Nonnull Class<C> entityClass)`
  - Executes `findComponentType` behavior.

## Notes
- No additional notes.
