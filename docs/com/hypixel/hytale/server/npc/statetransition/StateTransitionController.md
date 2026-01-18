**Source Hash:** `dc58ca80f55939bfd665939911954256efefc95b061e725948f44f37cd9ecd0a`

# StateTransitionController

## Overview

## Constructor Descriptions
- `StateTransitionController(@Nonnull BuilderStateTransitionController builder, @Nonnull BuilderSupport support)`
  - Creates a `StateTransitionController` instance.

## Method Descriptions
- `registerWithSupport(Role role)`: Add description.
  - Executes `registerWithSupport` behavior.
- `motionControllerChanged(@Nullable Ref<EntityStore> ref, @Nonnull NPCEntity npcComponent, @Nullable MotionController motionController, @Nullable ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `motionControllerChanged` behavior.
- `loaded(Role role)`: Add description.
  - Executes `loaded` behavior.
- `spawned(Role role)`: Add description.
  - Executes `spawned` behavior.
- `unloaded(Role role)`: Add description.
  - Executes `unloaded` behavior.
- `removed(Role role)`: Add description.
  - Executes `removed` behavior.
- `teleported(Role role, World from, World to)`: Add description.
  - Executes `teleported` behavior.
- `clearOnce()`: Add description.
  - Executes `clearOnce` behavior.
- `initiateStateTransition(int fromState, int toState)`: Add description.
  - Executes `initiateStateTransition` behavior.
- `isRunningTransitionActions()`: Add description.
  - Executes `isRunningTransitionActions` behavior.
- `runTransitionActions(Ref<EntityStore> ref, Role role, double dt, Store<EntityStore> store)`: Add description.
  - Executes `runTransitionActions` behavior.
- `registerFactories(@Nonnull BuilderManager builderManager)`: Add description.
  - Executes `registerFactories` behavior.
- `indexStateTransitionEdge(int from, int to)`: Add description.
  - Executes `indexStateTransitionEdge` behavior.
- `canExecute(Ref<EntityStore> var1, Role var2, InfoProvider var3, double var4, Store<EntityStore> var6)`: Add description.
  - Executes `canExecute` behavior.
- `execute(Ref<EntityStore> var1, Role var2, InfoProvider var3, double var4, Store<EntityStore> var6)`: Add description.
  - Executes `execute` behavior.
- `hasCompletedRun()`: Add description.
  - Executes `hasCompletedRun` behavior.
- `PrioritisedActionList(int priority, ActionList actionList)`: Add description.
  - Executes `PrioritisedActionList` behavior.
- `canExecute(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, InfoProvider sensorInfo, double dt, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `canExecute` behavior.
- `execute(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, InfoProvider sensorInfo, double dt, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `execute` behavior.
- `motionControllerChanged(@Nullable Ref<EntityStore> ref, @Nonnull NPCEntity npcComponent, MotionController motionController, @Nullable ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `motionControllerChanged` behavior.
- `addActionList(int priority, ActionList actionList)`: Add description.
  - Executes `addActionList` behavior.

## Notes
- No additional notes.
