# BlockPositionProvider

## Overview
- Documentation for `BlockPositionProvider`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.chunk.section.blockpositions`.

## Constructors
- `BlockPositionProvider(@Nonnull BitSet blockSets, @Nullable Int2ObjectOpenHashMap<List<IBlockPositionData>> data, short lightChangeCounter)`
  - Creates a `BlockPositionProvider` instance.

## Methods
- `getComponentType()`
  - Executes `getComponentType` behavior.
- `isStale(int currentBlockSet, @Nonnull BlockSection section)`
  - Executes `isStale` behavior.
- `findBlocks(@Nonnull List<IBlockPositionData> resultList, int blockSet, double range, double yRange, @Nonnull Ref<EntityStore> ref, @Nullable BiPredicate<IBlockPositionData, T> filter, T obj, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `findBlocks` behavior.
- `getSearchedBlockSets()`
  - Executes `getSearchedBlockSets` behavior.
- `forEachBlockSet(@Nonnull IntObjectConsumer<List<IBlockPositionData>> listConsumer)`
  - Executes `forEachBlockSet` behavior.
- `clone()`
  - Executes `clone` behavior.

## Notes
- No additional notes.
