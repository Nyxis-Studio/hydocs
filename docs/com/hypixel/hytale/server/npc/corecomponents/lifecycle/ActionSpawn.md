# ActionSpawn

## Overview
- Documentation for `ActionSpawn`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents.lifecycle`.

## Constructors
- `ActionSpawn(@Nonnull BuilderActionSpawn builderActionSpawn, @Nonnull BuilderSupport builderSupport)`
  - Creates a `ActionSpawn` instance.

## Methods
- `canExecute(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nullable InfoProvider sensorInfo, double dt, @Nonnull Store<EntityStore> store)`
  - Executes `canExecute` behavior.
- `execute(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull InfoProvider sensorInfo, double dt, @Nonnull Store<EntityStore> store)`
  - Executes `execute` behavior.
- `trySpawn(@Nonnull Ref<EntityStore> ref, @Nonnull SpawningContext spawningContext, @Nonnull Store<EntityStore> store)`
  - Executes `trySpawn` behavior.
- `postSpawn(@Nonnull NPCEntity npcComponent, @Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store)`
  - Executes `postSpawn` behavior.
- `joinFlock(@Nonnull Ref<EntityStore> targetRef, @Nonnull Store<EntityStore> store)`
  - Executes `joinFlock` behavior.
- `launchAtTarget(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store)`
  - Executes `launchAtTarget` behavior.
- `deferredSpawning(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, double dt, @Nonnull Store<EntityStore> store)`
  - Executes `deferredSpawning` behavior.

## Notes
- No additional notes.
