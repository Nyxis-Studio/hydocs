**Source Hash:** `dd7dece02754521cd03f01c59c48a6ef48d597ad7603dcc391f80d9bd4086872`

# RoleChangeSystem

## Overview

## Constructor Descriptions
- `RoleChangeSystem(@Nonnull ResourceType<EntityStore, RoleChangeQueue> roleChangeQueueResourceType, @Nonnull ComponentType<EntityStore, BeaconSupport> beaconSupportComponentType, @Nonnull ComponentType<EntityStore, PlayerBlockEventSupport> playerBlockEventSupportComponentType, @Nonnull ComponentType<EntityStore, NPCBlockEventSupport> npcBlockEventSupportComponentType, @Nonnull ComponentType<EntityStore, PlayerEntityEventSupport> playerEntityEventSupportComponentType, @Nonnull ComponentType<EntityStore, NPCEntityEventSupport> npcEntityEventSupportComponentType, @Nonnull ComponentType<EntityStore, Timers> timersComponentType, @Nonnull ComponentType<EntityStore, StateEvaluator> stateEvaluatorComponentType, @Nonnull ComponentType<EntityStore, ValueStore> valueStoreComponentType)`
  - Creates a `RoleChangeSystem` instance.

## Method Descriptions
- `getDependencies()`: Add description.
  - Executes `getDependencies` behavior.
- `tick(float dt, int systemIndex, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `tick` behavior.
- `requestRoleChange(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, int roleIndex, boolean changeAppearance, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `requestRoleChange` behavior.
- `requestRoleChange(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, int roleIndex, boolean changeAppearance, @Nullable String state, @Nullable String subState, @Nonnull ComponentAccessor<EntityStore> store)`: Add description.
  - Executes `requestRoleChange` behavior.
- `getResourceType()`: Add description.
  - Executes `getResourceType` behavior.
- `clone()`: Add description.
  - Executes `clone` behavior.

## Notes
- No additional notes.
