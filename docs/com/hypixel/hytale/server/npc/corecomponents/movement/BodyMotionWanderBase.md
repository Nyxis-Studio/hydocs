**Source Hash:** `eb41ad18aaaee053ef6670f0b0caade26bafd17089413dbf00e68b0969b3b198`

# BodyMotionWanderBase

## Overview

## Constructor Descriptions
- `BodyMotionWanderBase(@Nonnull BuilderBodyMotionWanderBase builder, @Nonnull BuilderSupport builderSupport)`
  - Creates a `BodyMotionWanderBase` instance.

## Method Descriptions
- `activate(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `activate` behavior.
- `deactivate(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `deactivate` behavior.
- `motionControllerChanged(@Nullable Ref<EntityStore> ref, @Nonnull NPCEntity npcComponent, @Nonnull MotionController motionController, @Nullable ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `motionControllerChanged` behavior.
- `computeSteering(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nullable InfoProvider sensorInfo, double dt, @Nonnull Steering desiredSteering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `computeSteering` behavior.
- `findBestDirection(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `findBestDirection` behavior.
- `constrainMove(@Nonnull Ref<EntityStore> var1, @Nonnull Role var2, @Nonnull Vector3d var3, @Nonnull Vector3d var4, double var5, @Nonnull ComponentAccessor<EntityStore> var7)`: Add description.
  - Executes `constrainMove` behavior.
- `restartSearch(@Nullable Ref<EntityStore> ref, @Nonnull NPCEntity npcComponent, @Nonnull MotionController activeMotionController, @Nullable ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `restartSearch` behavior.
- `computeHeightRange(@Nonnull Ref<EntityStore> ref, @Nonnull MotionController motionController, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `computeHeightRange` behavior.
- `probeDirection(@Nonnull Ref<EntityStore> ref, int dirIndex, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `probeDirection` behavior.
- `computeTargetPosition(@Nonnull Ref<EntityStore> ref, float heading, double distance, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `computeTargetPosition` behavior.
- `toAngle(@Nonnull Ref<EntityStore> ref, int direction, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `toAngle` behavior.
- `addPreOrderedDirection(int direction, int count)`: Add description.
  - Executes `addPreOrderedDirection` behavior.

## Notes
- No additional notes.
