# BlockTypeView

## Overview
- Documentation for `BlockTypeView`.
- Declared as a class in `com.hypixel.hytale.server.npc.blackboard.view.blocktype`.

## Constructors
- `BlockTypeView(long index, Blackboard blackboard, BlockPositionEntryGenerator generator)`
  - Creates a `BlockTypeView` instance.

## Methods
- `getIndex()`
  - Executes `getIndex` behavior.
- `isOutdated(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store)`
  - Executes `isOutdated` behavior.
- `getUpdatedView(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getUpdatedView` behavior.
- `initialiseEntity(@Nonnull Ref<EntityStore> ref, @Nonnull NPCEntity npcComponent)`
  - Executes `initialiseEntity` behavior.
- `cleanup()`
  - Executes `cleanup` behavior.
- `onWorldRemoved()`
  - Executes `onWorldRemoved` behavior.
- `addSearchedBlockSets(@Nonnull Ref<EntityStore> ref, @Nonnull NPCEntity entity, @Nonnull IntList blockSets)`
  - Executes `addSearchedBlockSets` behavior.
- `addSearchedBlockSet(int blockSet)`
  - Executes `addSearchedBlockSet` behavior.
- `removeSearchedBlockSets(@Nonnull Ref<EntityStore> ref, @Nonnull NPCEntity npcComponent, @Nonnull IntList blockSets)`
  - Executes `removeSearchedBlockSets` behavior.
- `removeSearchedBlockSet(int blockSet)`
  - Executes `removeSearchedBlockSet` behavior.
- `findBlock(int blockSet, double range, double yMax, boolean pickRandom, @Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `findBlock` behavior.
- `getEntities()`
  - Executes `getEntities` behavior.
- `getAllBlockSets()`
  - Executes `getAllBlockSets` behavior.
- `getBlockSetCounts()`
  - Executes `getBlockSetCounts` behavior.
- `rebuildBlockTypeAggregate(@Nonnull IntArrayList aggregate, @Nonnull BitSet searchedBlockSets)`
  - Executes `rebuildBlockTypeAggregate` behavior.

## Notes
- No additional notes.
