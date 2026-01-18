# RoleChangeSystem

## Overview
- Documentation for `RoleChangeSystem`.
- Declared as a class in `com.hypixel.hytale.server.npc.systems`.

## Constructors
- `RoleChangeSystem(@Nonnull ResourceType<EntityStore, RoleChangeQueue> roleChangeQueueResourceType, @Nonnull ComponentType<EntityStore, BeaconSupport> beaconSupportComponentType, @Nonnull ComponentType<EntityStore, PlayerBlockEventSupport> playerBlockEventSupportComponentType, @Nonnull ComponentType<EntityStore, NPCBlockEventSupport> npcBlockEventSupportComponentType, @Nonnull ComponentType<EntityStore, PlayerEntityEventSupport> playerEntityEventSupportComponentType, @Nonnull ComponentType<EntityStore, NPCEntityEventSupport> npcEntityEventSupportComponentType, @Nonnull ComponentType<EntityStore, Timers> timersComponentType, @Nonnull ComponentType<EntityStore, StateEvaluator> stateEvaluatorComponentType, @Nonnull ComponentType<EntityStore, ValueStore> valueStoreComponentType)`
  - Creates a `RoleChangeSystem` instance.

## Methods
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `tick(float dt, int systemIndex, @Nonnull Store<EntityStore> store)`
  - Executes `tick` behavior.
- `requestRoleChange(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, int roleIndex, boolean changeAppearance, @Nonnull Store<EntityStore> store)`
  - Executes `requestRoleChange` behavior.
- `requestRoleChange(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, int roleIndex, boolean changeAppearance, @Nullable String state, @Nullable String subState, @Nonnull ComponentAccessor<EntityStore> store)`
  - Executes `requestRoleChange` behavior.
- `getResourceType()`
  - Executes `getResourceType` behavior.
- `clone()`
  - Executes `clone` behavior.

## Notes
- No additional notes.
