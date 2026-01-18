# ApplyForceInteraction

## Overview
- Documentation for `ApplyForceInteraction`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ApplyForceInteraction()`
  - Creates a `ApplyForceInteraction` instance.
- `ApplyForceInteraction(@Nonnull WaitForDataFrom waitForDataFrom, @Nullable InteractionEffects effects, float horizontalSpeedMultiplier, float runTime, boolean cancelOnItemChange, @Nullable Map<GameMode, InteractionSettings> settings, @Nullable InteractionRules rules, @Nullable int[] tags, @Nullable InteractionCameraSettings camera, int next, int failed, @Nullable VelocityConfig velocityConfig, @Nonnull ChangeVelocityType changeVelocityType, @Nullable AppliedForce[] forces, float duration, @Nullable FloatRange verticalClamp, boolean waitForGround, boolean waitForCollision, float groundCheckDelay, float collisionCheckDelay, int groundNext, int collisionNext, float raycastDistance, float raycastHeightOffset, @Nonnull RaycastMode raycastMode)`
  - Creates a `ApplyForceInteraction` instance.
- `ApplyForceInteraction(@Nonnull ApplyForceInteraction other)`
  - Creates a `ApplyForceInteraction` instance.

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
