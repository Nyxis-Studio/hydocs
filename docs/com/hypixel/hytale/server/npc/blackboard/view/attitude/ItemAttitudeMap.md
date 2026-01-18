# ItemAttitudeMap

## Overview
- Documentation for `ItemAttitudeMap`.
- Declared as a class in `com.hypixel.hytale.server.npc.blackboard.view.attitude`.

## Constructors
- `ItemAttitudeMap(Map<String, Attitude>[] map)`
  - Creates a `ItemAttitudeMap` instance.
- `ItemAttitudeMap(this.map)`
  - Creates a `ItemAttitudeMap` instance.

## Methods
- `getAttitude(@Nonnull NPCEntity parent, @Nullable ItemStack item)`
  - Executes `getAttitude` behavior.
- `getAttitudeGroupCount()`
  - Executes `getAttitudeGroupCount` behavior.
- `updateAttitudeGroup(int id, @Nonnull ItemAttitudeGroup group)`
  - Executes `updateAttitudeGroup` behavior.
- `addAttitudeGroups(@Nonnull Map<String, ItemAttitudeGroup> groups)`
  - Executes `addAttitudeGroups` behavior.
- `addAttitudeGroup(@Nonnull ItemAttitudeGroup group)`
  - Executes `addAttitudeGroup` behavior.
- `createGroupMap(@Nonnull ItemAttitudeGroup group)`
  - Executes `createGroupMap` behavior.
- `putGroups(@Nullable String[] group, Attitude targetAttitude, @Nonnull HashMap<String, Attitude> targetMap)`
  - Executes `putGroups` behavior.
- `build()`
  - Executes `build` behavior.

## Notes
- No additional notes.
