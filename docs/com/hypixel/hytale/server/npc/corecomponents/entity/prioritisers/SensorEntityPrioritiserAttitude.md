# SensorEntityPrioritiserAttitude

## Overview
- Documentation for `SensorEntityPrioritiserAttitude`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents.entity.prioritisers`.

## Constructors
- `SensorEntityPrioritiserAttitude(@Nonnull BuilderSensorEntityPrioritiserAttitude builder, @Nonnull BuilderSupport support)`
  - Creates a `SensorEntityPrioritiserAttitude` instance.

## Methods
- `registerWithSupport(@Nonnull Role role)`
  - Executes `registerWithSupport` behavior.
- `getNPCPrioritiser()`
  - Executes `getNPCPrioritiser` behavior.
- `getPlayerPrioritiser()`
  - Executes `getPlayerPrioritiser` behavior.
- `pickTarget(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull Vector3d position, @Nonnull Ref<EntityStore> playerRef, @Nonnull Ref<EntityStore> npcRef, boolean useProjectedDistance, @Nonnull Store<EntityStore> store)`
  - Executes `pickTarget` behavior.
- `providesFilters()`
  - Executes `providesFilters` behavior.
- `buildProvidedFilters(@Nonnull List<IEntityFilter> filters)`
  - Executes `buildProvidedFilters` behavior.
- `getPriority(@Nonnull Ref<EntityStore> ref, @Nonnull WorldSupport support, @Nonnull Ref<EntityStore> targetRef, @Nonnull Store<EntityStore> store)`
  - Executes `getPriority` behavior.
- `init(@Nonnull Role role)`
  - Executes `init` behavior.
- `test(@Nonnull Ref<EntityStore> ref, @Nonnull Ref<EntityStore> targetRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `test` behavior.
- `getHighestPriorityTarget()`
  - Executes `getHighestPriorityTarget` behavior.
- `cleanup()`
  - Executes `cleanup` behavior.

## Notes
- No additional notes.
