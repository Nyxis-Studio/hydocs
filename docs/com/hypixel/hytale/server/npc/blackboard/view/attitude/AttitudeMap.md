# AttitudeMap

## Overview
- Documentation for `AttitudeMap`.
- Declared as a class in `com.hypixel.hytale.server.npc.blackboard.view.attitude`.

## Constructors
- `AttitudeMap(Int2ObjectMap<Attitude>[] map)`
  - Creates a `AttitudeMap` instance.
- `AttitudeMap(this.map)`
  - Creates a `AttitudeMap` instance.

## Methods
- `getAttitude(@Nonnull Role role, @Nonnull Ref<EntityStore> target, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getAttitude` behavior.
- `getAttitudeGroupCount()`
  - Executes `getAttitudeGroupCount` behavior.
- `updateAttitudeGroup(int id, @Nonnull AttitudeGroup group)`
  - Executes `updateAttitudeGroup` behavior.
- `addAttitudeGroups(@Nonnull Map<String, AttitudeGroup> groups)`
  - Executes `addAttitudeGroups` behavior.
- `addAttitudeGroup(@Nonnull AttitudeGroup group)`
  - Executes `addAttitudeGroup` behavior.
- `createGroupMap(@Nonnull AttitudeGroup group)`
  - Executes `createGroupMap` behavior.
- `putGroups(String attitudeGroup, @Nonnull TagSetPlugin.TagSetLookup npcGroupLookup, @Nullable String[] group, Attitude targetAttitude, @Nonnull Int2ObjectMap<Attitude> targetMap)`
  - Executes `putGroups` behavior.
- `build()`
  - Executes `build` behavior.

## Notes
- No additional notes.
