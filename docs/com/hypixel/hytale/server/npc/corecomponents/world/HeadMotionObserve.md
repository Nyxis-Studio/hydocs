# HeadMotionObserve

## Overview
- Documentation for `HeadMotionObserve`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents.world`.

## Constructors
- `HeadMotionObserve(@Nonnull BuilderHeadMotionObserve builder, @Nonnull BuilderSupport support)`
  - Creates a `HeadMotionObserve` instance.

## Methods
- `activate(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `activate` behavior.
- `computeSteering(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nullable InfoProvider sensorInfo, double dt, @Nonnull Steering desiredSteering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `computeSteering` behavior.
- `tickPreDelay(double dt)`
  - Executes `tickPreDelay` behavior.
- `tickDelay(double dt)`
  - Executes `tickDelay` behavior.
- `pickNextAngle(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `pickNextAngle` behavior.

## Notes
- No additional notes.
