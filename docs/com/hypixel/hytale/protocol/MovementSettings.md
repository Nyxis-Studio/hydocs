# MovementSettings

## Overview
- Documentation for `MovementSettings`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `MovementSettings()`
  - Creates a `MovementSettings` instance.
- `MovementSettings(float mass, float dragCoefficient, boolean invertedGravity, float velocityResistance, float jumpForce, float swimJumpForce, float jumpBufferDuration, float jumpBufferMaxYVelocity, float acceleration, float airDragMin, float airDragMax, float airDragMinSpeed, float airDragMaxSpeed, float airFrictionMin, float airFrictionMax, float airFrictionMinSpeed, float airFrictionMaxSpeed, float airSpeedMultiplier, float airControlMinSpeed, float airControlMaxSpeed, float airControlMinMultiplier, float airControlMaxMultiplier, float comboAirSpeedMultiplier, float baseSpeed, float climbSpeed, float climbSpeedLateral, float climbUpSprintSpeed, float climbDownSprintSpeed, float horizontalFlySpeed, float verticalFlySpeed, float maxSpeedMultiplier, float minSpeedMultiplier, float wishDirectionGravityX, float wishDirectionGravityY, float wishDirectionWeightX, float wishDirectionWeightY, boolean canFly, float collisionExpulsionForce, float forwardWalkSpeedMultiplier, float backwardWalkSpeedMultiplier, float strafeWalkSpeedMultiplier, float forwardRunSpeedMultiplier, float backwardRunSpeedMultiplier, float strafeRunSpeedMultiplier, float forwardCrouchSpeedMultiplier, float backwardCrouchSpeedMultiplier, float strafeCrouchSpeedMultiplier, float forwardSprintSpeedMultiplier, float variableJumpFallForce, float fallEffectDuration, float fallJumpForce, float fallMomentumLoss, float autoJumpObstacleSpeedLoss, float autoJumpObstacleSprintSpeedLoss, float autoJumpObstacleEffectDuration, float autoJumpObstacleSprintEffectDuration, float autoJumpObstacleMaxAngle, boolean autoJumpDisableJumping, float minSlideEntrySpeed, float slideExitSpeed, float minFallSpeedToEngageRoll, float maxFallSpeedToEngageRoll, float rollStartSpeedModifier, float rollExitSpeedModifier, float rollTimeToComplete)`
  - Creates a `MovementSettings` instance.
- `MovementSettings(@Nonnull MovementSettings other)`
  - Creates a `MovementSettings` instance.

## Methods
- `deserialize(@Nonnull ByteBuf buf, int offset)`
  - Executes `deserialize` behavior.
- `computeBytesConsumed(@Nonnull ByteBuf buf, int offset)`
  - Executes `computeBytesConsumed` behavior.
- `serialize(@Nonnull ByteBuf buf)`
  - Executes `serialize` behavior.
- `computeSize()`
  - Executes `computeSize` behavior.
- `validateStructure(@Nonnull ByteBuf buffer, int offset)`
  - Executes `validateStructure` behavior.
- `clone()`
  - Executes `clone` behavior.
- `equals(Object obj)`
  - Executes `equals` behavior.
- `hashCode()`
  - Executes `hashCode` behavior.

## Notes
- No additional notes.
