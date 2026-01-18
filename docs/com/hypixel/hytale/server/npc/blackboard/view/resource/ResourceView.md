# ResourceView

## Overview
- Documentation for `ResourceView`.
- Declared as a class in `com.hypixel.hytale.server.npc.blackboard.view.resource`.

## Constructors
- `ResourceView(long index)`
  - Creates a `ResourceView` instance.

## Methods
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
- `isBlockReserved(int x, int y, int z)`
  - Executes `isBlockReserved` behavior.
- `reserveBlock(@Nonnull NPCEntity entity, int x, int y, int z)`
  - Executes `reserveBlock` behavior.
- `clearReservation(@Nonnull Ref<EntityStore> ref)`
  - Executes `clearReservation` behavior.
- `getIndex()`
  - Executes `getIndex` behavior.
- `getReservationsByEntity()`
  - Executes `getReservationsByEntity` behavior.
- `getSectionIndex()`
  - Executes `getSectionIndex` behavior.
- `getBlockIndex()`
  - Executes `getBlockIndex` behavior.

## Notes
- No additional notes.
