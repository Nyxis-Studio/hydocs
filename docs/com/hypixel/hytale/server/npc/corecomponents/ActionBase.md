# ActionBase

## Overview
- Documentation for `ActionBase`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents`.

## Constructors
- `ActionBase(@Nonnull BuilderActionBase builderActionBase)`
  - Creates a `ActionBase` instance.

## Methods
- `canExecute(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, InfoProvider sensorInfo, double dt, @Nonnull Store<EntityStore> store)`
  - Executes `canExecute` behavior.
- `execute(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, InfoProvider sensorInfo, double dt, @Nonnull Store<EntityStore> store)`
  - Executes `execute` behavior.
- `activate(Role role, InfoProvider infoProvider)`
  - Executes `activate` behavior.
- `deactivate(Role role, InfoProvider infoProvider)`
  - Executes `deactivate` behavior.
- `isActivated()`
  - Executes `isActivated` behavior.
- `isTriggered()`
  - Executes `isTriggered` behavior.
- `clearOnce()`
  - Executes `clearOnce` behavior.
- `setOnce()`
  - Executes `setOnce` behavior.
- `processDelay(float dt)`
  - Executes `processDelay` behavior.

## Notes
- No additional notes.
