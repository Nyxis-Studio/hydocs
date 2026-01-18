# StateSupport

## Overview
- Documentation for `StateSupport`.
- Declared as a class in `com.hypixel.hytale.server.npc.role.support`.

## Constructors
- `StateSupport(@Nonnull BuilderRole builder, @Nonnull BuilderSupport support)`
  - Creates a `StateSupport` instance.

## Methods
- `getStateTransitionController()`
  - Executes `getStateTransitionController` behavior.
- `getStateHelper()`
  - Executes `getStateHelper` behavior.
- `postRoleBuilt(@Nonnull BuilderSupport builderSupport)`
  - Executes `postRoleBuilt` behavior.
- `update(@Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `update` behavior.
- `pollNeedClearOnce()`
  - Executes `pollNeedClearOnce` behavior.
- `inState(int state)`
  - Executes `inState` behavior.
- `inSubState(int subState)`
  - Executes `inSubState` behavior.
- `inState(int state, int subState)`
  - Executes `inState` behavior.
- `inState(String state, String subState)`
  - Executes `inState` behavior.
- `getStateName()`
  - Executes `getStateName` behavior.
- `getStateName(int state, int subState)`
  - Executes `getStateName` behavior.
- `getStateIndex()`
  - Executes `getStateIndex` behavior.
- `getSubStateIndex()`
  - Executes `getSubStateIndex` behavior.
- `appendStateName(@Nonnull StringBuilder builder)`
  - Executes `appendStateName` behavior.
- `setState(int state, int subState, boolean clearOnce, boolean skipTransition)`
  - Executes `setState` behavior.
- `setState(@Nonnull Ref<EntityStore> ref, @Nonnull String state, @Nullable String subState, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `setState` behavior.
- `setSubState(String subState)`
  - Executes `setSubState` behavior.
- `isComponentInState(int componentIndex, int targetState)`
  - Executes `isComponentInState` behavior.
- `setComponentState(int componentIndex, int targetState)`
  - Executes `setComponentState` behavior.
- `resetLocalStateMachines()`
  - Executes `resetLocalStateMachines` behavior.
- `flockSetState(Ref<EntityStore> ref, @Nonnull String state, @Nullable String subState, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `flockSetState` behavior.
- `isInBusyState()`
  - Executes `isInBusyState` behavior.
- `addContextualInteraction(@Nonnull Ref<EntityStore> playerRef, @Nonnull String context)`
  - Executes `addContextualInteraction` behavior.
- `hasContextualInteraction(@Nonnull Ref<EntityStore> playerReference, @Nonnull String context)`
  - Executes `hasContextualInteraction` behavior.
- `addInteraction(@Nonnull Player player)`
  - Executes `addInteraction` behavior.
- `consumeInteraction(@Nonnull Ref<EntityStore> playerReference)`
  - Executes `consumeInteraction` behavior.
- `setInteractable(@Nonnull Ref<EntityStore> playerReference, boolean interactable)`
  - Executes `setInteractable` behavior.
- `setInteractable(@Nonnull Ref<EntityStore> entityRef, @Nonnull Ref<EntityStore> playerReference, boolean interactable, @Nullable String hint, boolean showPrompt, @Nonnull Store<EntityStore> store)`
  - Executes `setInteractable` behavior.
- `sendInteractionHintToPlayer(@Nonnull Ref<EntityStore> entityRef, @Nonnull Ref<EntityStore> playerReference, @Nonnull String hint, @Nonnull Store<EntityStore> store)`
  - Executes `sendInteractionHintToPlayer` behavior.
- `setInteractionIterationTarget(@Nullable Ref<EntityStore> playerReference)`
  - Executes `setInteractionIterationTarget` behavior.
- `getInteractionIterationTarget()`
  - Executes `getInteractionIterationTarget` behavior.
- `willInteractWith(@Nonnull Ref<EntityStore> playerReference)`
  - Executes `willInteractWith` behavior.
- `runTransitionActions(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, double dt, @Nonnull Store<EntityStore> store)`
  - Executes `runTransitionActions` behavior.
- `isRunningTransitionActions()`
  - Executes `isRunningTransitionActions` behavior.
- `activate()`
  - Executes `activate` behavior.

## Notes
- No additional notes.
