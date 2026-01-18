# PhysicsConfig

## Overview
- Documentation for `PhysicsConfig`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `PhysicsConfig()`
  - Creates a `PhysicsConfig` instance.
- `PhysicsConfig(@Nonnull PhysicsType type, double density, double gravity, double bounciness, int bounceCount, double bounceLimit, boolean sticksVertically, boolean computeYaw, boolean computePitch, @Nonnull RotationMode rotationMode, double moveOutOfSolidSpeed, double terminalVelocityAir, double densityAir, double terminalVelocityWater, double densityWater, double hitWaterImpulseLoss, double rotationForce, float speedRotationFactor, double swimmingDampingFactor, boolean allowRolling, double rollingFrictionFactor, float rollingSpeed)`
  - Creates a `PhysicsConfig` instance.
- `PhysicsConfig(@Nonnull PhysicsConfig other)`
  - Creates a `PhysicsConfig` instance.

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
