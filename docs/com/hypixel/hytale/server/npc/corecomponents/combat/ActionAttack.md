# ActionAttack

## Overview
- Documentation for `ActionAttack`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents.combat`.

## Constructors
- `ActionAttack(@Nonnull BuilderActionAttack builderActionAttack, @Nonnull BuilderSupport builderSupport)`
  - Creates a `ActionAttack` instance.

## Methods
- `canExecute(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, InfoProvider sensorInfo, double dt, @Nonnull Store<EntityStore> store)`
  - Executes `canExecute` behavior.
- `execute(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nullable InfoProvider sensorInfo, double dt, @Nonnull Store<EntityStore> store)`
  - Executes `execute` behavior.
- `activate(Role role, @Nullable InfoProvider infoProvider)`
  - Executes `activate` behavior.
- `deactivate(Role role, @Nullable InfoProvider infoProvider)`
  - Executes `deactivate` behavior.
- `hasTimeForAiming(double dt)`
  - Executes `hasTimeForAiming` behavior.
- `newAimingTime()`
  - Executes `newAimingTime` behavior.
- `newAttackPause()`
  - Executes `newAttackPause` behavior.
- `getInteractionVars(InteractionContext c)`
  - Executes `getInteractionVars` behavior.
- `get()`
  - Executes `get` behavior.
- `getInteractionType()`
  - Executes `getInteractionType` behavior.

## Notes
- No additional notes.
