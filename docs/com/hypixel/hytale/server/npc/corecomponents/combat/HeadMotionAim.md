# HeadMotionAim

## Overview
- Documentation for `HeadMotionAim`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents.combat`.

## Constructors
- `HeadMotionAim(@Nonnull BuilderHeadMotionAim builder, @Nonnull BuilderSupport support)`
  - Creates a `HeadMotionAim` instance.

## Methods
- `preComputeSteering(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nullable InfoProvider sensorInfo, @Nonnull Store<EntityStore> store)`
  - Executes `preComputeSteering` behavior.
- `activate(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `activate` behavior.
- `computeSteering(@Nonnull Ref<EntityStore> ref, @Nonnull Role support, @Nullable InfoProvider sensorInfo, double dt, @Nonnull Steering desiredSteering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `computeSteering` behavior.

## Notes
- No additional notes.
