# ActionBeacon

## Overview
- Documentation for `ActionBeacon`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents.entity`.

## Constructors
- `ActionBeacon(@Nonnull BuilderActionBeacon builderActionBeacon, @Nonnull BuilderSupport support)`
  - Creates a `ActionBeacon` instance.

## Methods
- `registerWithSupport(@Nonnull Role role)`
  - Executes `registerWithSupport` behavior.
- `canExecute(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, InfoProvider sensorInfo, double dt, @Nonnull Store<EntityStore> store)`
  - Executes `canExecute` behavior.
- `execute(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, InfoProvider sensorInfo, double dt, @Nonnull Store<EntityStore> store)`
  - Executes `execute` behavior.
- `filterNPCs(@Nonnull Ref<EntityStore> ref, @Nonnull ActionBeacon _this, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `filterNPCs` behavior.
- `sendNPCMessage(@Nonnull Ref<EntityStore> self, @Nonnull Ref<EntityStore> targetRef, @Nonnull Ref<EntityStore> target, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `sendNPCMessage` behavior.

## Notes
- No additional notes.
