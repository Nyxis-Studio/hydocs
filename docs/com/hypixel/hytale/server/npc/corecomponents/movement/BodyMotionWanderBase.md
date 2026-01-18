# BodyMotionWanderBase

## Overview
- Documentation for `BodyMotionWanderBase`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents.movement`.

## Constructors
- `BodyMotionWanderBase(@Nonnull BuilderBodyMotionWanderBase builder, @Nonnull BuilderSupport builderSupport)`
  - Creates a `BodyMotionWanderBase` instance.

## Methods
- `activate(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `activate` behavior.
- `deactivate(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `deactivate` behavior.
- `motionControllerChanged(@Nullable Ref<EntityStore> ref, @Nonnull NPCEntity npcComponent, @Nonnull MotionController motionController, @Nullable ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `motionControllerChanged` behavior.
- `computeSteering(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nullable InfoProvider sensorInfo, double dt, @Nonnull Steering desiredSteering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `computeSteering` behavior.
- `findBestDirection(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `findBestDirection` behavior.
- `constrainMove(@Nonnull Ref<EntityStore> var1, @Nonnull Role var2, @Nonnull Vector3d var3, @Nonnull Vector3d var4, double var5, @Nonnull ComponentAccessor<EntityStore> var7)`
  - Executes `constrainMove` behavior.
- `restartSearch(@Nullable Ref<EntityStore> ref, @Nonnull NPCEntity npcComponent, @Nonnull MotionController activeMotionController, @Nullable ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `restartSearch` behavior.
- `computeHeightRange(@Nonnull Ref<EntityStore> ref, @Nonnull MotionController motionController, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `computeHeightRange` behavior.
- `probeDirection(@Nonnull Ref<EntityStore> ref, int dirIndex, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `probeDirection` behavior.
- `computeTargetPosition(@Nonnull Ref<EntityStore> ref, float heading, double distance, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `computeTargetPosition` behavior.
- `toAngle(@Nonnull Ref<EntityStore> ref, int direction, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `toAngle` behavior.
- `addPreOrderedDirection(int direction, int count)`
  - Executes `addPreOrderedDirection` behavior.

## Notes
- No additional notes.
