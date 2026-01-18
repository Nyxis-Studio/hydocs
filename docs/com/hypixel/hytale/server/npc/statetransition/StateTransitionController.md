# StateTransitionController

## Overview
- Documentation for `StateTransitionController`.
- Declared as a class in `com.hypixel.hytale.server.npc.statetransition`.

## Constructors
- `StateTransitionController(@Nonnull BuilderStateTransitionController builder, @Nonnull BuilderSupport support)`
  - Creates a `StateTransitionController` instance.

## Methods
- `registerWithSupport(Role role)`
  - Executes `registerWithSupport` behavior.
- `motionControllerChanged(@Nullable Ref<EntityStore> ref, @Nonnull NPCEntity npcComponent, @Nullable MotionController motionController, @Nullable ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `motionControllerChanged` behavior.
- `loaded(Role role)`
  - Executes `loaded` behavior.
- `spawned(Role role)`
  - Executes `spawned` behavior.
- `unloaded(Role role)`
  - Executes `unloaded` behavior.
- `removed(Role role)`
  - Executes `removed` behavior.
- `teleported(Role role, World from, World to)`
  - Executes `teleported` behavior.
- `clearOnce()`
  - Executes `clearOnce` behavior.
- `initiateStateTransition(int fromState, int toState)`
  - Executes `initiateStateTransition` behavior.
- `isRunningTransitionActions()`
  - Executes `isRunningTransitionActions` behavior.
- `runTransitionActions(Ref<EntityStore> ref, Role role, double dt, Store<EntityStore> store)`
  - Executes `runTransitionActions` behavior.
- `registerFactories(@Nonnull BuilderManager builderManager)`
  - Executes `registerFactories` behavior.
- `indexStateTransitionEdge(int from, int to)`
  - Executes `indexStateTransitionEdge` behavior.
- `canExecute(Ref<EntityStore> var1, Role var2, InfoProvider var3, double var4, Store<EntityStore> var6)`
  - Executes `canExecute` behavior.
- `execute(Ref<EntityStore> var1, Role var2, InfoProvider var3, double var4, Store<EntityStore> var6)`
  - Executes `execute` behavior.
- `hasCompletedRun()`
  - Executes `hasCompletedRun` behavior.
- `PrioritisedActionList(int priority, ActionList actionList)`
  - Executes `PrioritisedActionList` behavior.
- `canExecute(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, InfoProvider sensorInfo, double dt, @Nonnull Store<EntityStore> store)`
  - Executes `canExecute` behavior.
- `execute(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, InfoProvider sensorInfo, double dt, @Nonnull Store<EntityStore> store)`
  - Executes `execute` behavior.
- `motionControllerChanged(@Nullable Ref<EntityStore> ref, @Nonnull NPCEntity npcComponent, MotionController motionController, @Nullable ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `motionControllerChanged` behavior.
- `addActionList(int priority, ActionList actionList)`
  - Executes `addActionList` behavior.

## Notes
- No additional notes.
