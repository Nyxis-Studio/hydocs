# BodyMotionTeleport

## Overview
- Documentation for `BodyMotionTeleport`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents.movement`.

## Constructors
- `BodyMotionTeleport(@Nonnull BuilderBodyMotionTeleport builder)`
  - Creates a `BodyMotionTeleport` instance.

## Methods
- `activate(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `activate` behavior.
- `computeSteering(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nullable InfoProvider sensorInfo, double dt, @Nonnull Steering desiredSteering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `computeSteering` behavior.
- `tickCooldown(double dt)`
  - Executes `tickCooldown` behavior.
- `get()`
  - Executes `get` behavior.

## Notes
- No additional notes.
