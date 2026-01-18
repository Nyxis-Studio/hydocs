**Source Hash:** `c078f135a161488c055933940f0d3c8bb7a7d53d3485a78ab7f7b877e003e903`

# StateSupport

## Overview

## Constructor Descriptions
- `StateSupport(@Nonnull BuilderRole builder, @Nonnull BuilderSupport support)`
  - Creates a `StateSupport` instance.

## Method Descriptions
- `getStateTransitionController()`: Add description.
  - Executes `getStateTransitionController` behavior.
- `getStateHelper()`: Add description.
  - Executes `getStateHelper` behavior.
- `postRoleBuilt(@Nonnull BuilderSupport builderSupport)`: Add description.
  - Executes `postRoleBuilt` behavior.
- `update(@Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `update` behavior.
- `pollNeedClearOnce()`: Add description.
  - Executes `pollNeedClearOnce` behavior.
- `inState(int state)`: Add description.
  - Executes `inState` behavior.
- `inSubState(int subState)`: Add description.
  - Executes `inSubState` behavior.
- `inState(int state, int subState)`: Add description.
  - Executes `inState` behavior.
- `inState(String state, String subState)`: Add description.
  - Executes `inState` behavior.
- `getStateName()`: Add description.
  - Executes `getStateName` behavior.
- `getStateName(int state, int subState)`: Add description.
  - Executes `getStateName` behavior.
- `getStateIndex()`: Add description.
  - Executes `getStateIndex` behavior.
- `getSubStateIndex()`: Add description.
  - Executes `getSubStateIndex` behavior.
- `appendStateName(@Nonnull StringBuilder builder)`: Add description.
  - Executes `appendStateName` behavior.
- `setState(int state, int subState, boolean clearOnce, boolean skipTransition)`: Add description.
  - Executes `setState` behavior.
- `setState(@Nonnull Ref<EntityStore> ref, @Nonnull String state, @Nullable String subState, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `setState` behavior.
- `setSubState(String subState)`: Add description.
  - Executes `setSubState` behavior.
- `isComponentInState(int componentIndex, int targetState)`: Add description.
  - Executes `isComponentInState` behavior.
- `setComponentState(int componentIndex, int targetState)`: Add description.
  - Executes `setComponentState` behavior.
- `resetLocalStateMachines()`: Add description.
  - Executes `resetLocalStateMachines` behavior.
- `flockSetState(Ref<EntityStore> ref, @Nonnull String state, @Nullable String subState, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `flockSetState` behavior.
- `isInBusyState()`: Add description.
  - Executes `isInBusyState` behavior.
- `addContextualInteraction(@Nonnull Ref<EntityStore> playerRef, @Nonnull String context)`: Add description.
  - Executes `addContextualInteraction` behavior.
- `hasContextualInteraction(@Nonnull Ref<EntityStore> playerReference, @Nonnull String context)`: Add description.
  - Executes `hasContextualInteraction` behavior.
- `addInteraction(@Nonnull Player player)`: Add description.
  - Executes `addInteraction` behavior.
- `consumeInteraction(@Nonnull Ref<EntityStore> playerReference)`: Add description.
  - Executes `consumeInteraction` behavior.
- `setInteractable(@Nonnull Ref<EntityStore> playerReference, boolean interactable)`: Add description.
  - Executes `setInteractable` behavior.
- `setInteractable(@Nonnull Ref<EntityStore> entityRef, @Nonnull Ref<EntityStore> playerReference, boolean interactable, @Nullable String hint, boolean showPrompt, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `setInteractable` behavior.
- `sendInteractionHintToPlayer(@Nonnull Ref<EntityStore> entityRef, @Nonnull Ref<EntityStore> playerReference, @Nonnull String hint, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `sendInteractionHintToPlayer` behavior.
- `setInteractionIterationTarget(@Nullable Ref<EntityStore> playerReference)`: Add description.
  - Executes `setInteractionIterationTarget` behavior.
- `getInteractionIterationTarget()`: Add description.
  - Executes `getInteractionIterationTarget` behavior.
- `willInteractWith(@Nonnull Ref<EntityStore> playerReference)`: Add description.
  - Executes `willInteractWith` behavior.
- `runTransitionActions(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, double dt, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `runTransitionActions` behavior.
- `isRunningTransitionActions()`: Add description.
  - Executes `isRunningTransitionActions` behavior.
- `activate()`: Add description.
  - Executes `activate` behavior.

## Notes
- No additional notes.
