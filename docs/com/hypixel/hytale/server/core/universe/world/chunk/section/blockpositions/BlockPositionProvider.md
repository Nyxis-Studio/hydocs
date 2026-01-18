**Source Hash:** `8f9031f20a0d2bc403f9b101966ae032ad1649e6a86fbca20e442ce115c0ddb4`

# BlockPositionProvider

## Overview

## Constructor Descriptions
- `BlockPositionProvider(@Nonnull BitSet blockSets, @Nullable Int2ObjectOpenHashMap<List<IBlockPositionData>> data, short lightChangeCounter)`
  - Creates a `BlockPositionProvider` instance.

## Method Descriptions
- `getComponentType()`: Add description.
  - Executes `getComponentType` behavior.
- `isStale(int currentBlockSet, @Nonnull BlockSection section)`: Add description.
  - Executes `isStale` behavior.
- `findBlocks(@Nonnull List<IBlockPositionData> resultList, int blockSet, double range, double yRange, @Nonnull Ref<EntityStore> ref, @Nullable BiPredicate<IBlockPositionData, T> filter, T obj, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `findBlocks` behavior.
- `getSearchedBlockSets()`: Add description.
  - Executes `getSearchedBlockSets` behavior.
- `forEachBlockSet(@Nonnull IntObjectConsumer<List<IBlockPositionData>> listConsumer)`: Add description.
  - Executes `forEachBlockSet` behavior.
- `clone()`: Add description.
  - Executes `clone` behavior.

## Notes
- No additional notes.
