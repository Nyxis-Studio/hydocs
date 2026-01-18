# SensorEvent

## Overview
- Documentation for `SensorEvent`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents.world`.

## Constructors
- `SensorEvent(@Nonnull BuilderSensorEvent builder, @Nonnull BuilderSupport support)`
  - Creates a `SensorEvent` instance.

## Methods
- `matches(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, double dt, @Nonnull Store<EntityStore> store)`
  - Executes `matches` behavior.
- `getSensorInfo()`
  - Executes `getSensorInfo` behavior.
- `setTarget(@Nonnull MarkedEntitySupport support, @Nullable Ref<EntityStore> target, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `setTarget` behavior.
- `getPlayerTarget(@Nonnull Ref<EntityStore> var1, @Nonnull Store<EntityStore> var2)`
  - Executes `getPlayerTarget` behavior.
- `getNpcTarget(@Nonnull Ref<EntityStore> var1, @Nonnull Store<EntityStore> var2)`
  - Executes `getNpcTarget` behavior.
- `get()`
  - Executes `get` behavior.

## Notes
- No additional notes.
