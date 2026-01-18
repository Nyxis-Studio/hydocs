# PhysicsBodyStateUpdater

## Overview
- Documentation for `PhysicsBodyStateUpdater`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.physics.util`.

## Constructors
- None.

## Methods
- `update(@Nonnull PhysicsBodyState before, @Nonnull PhysicsBodyState after, double mass, double dt, boolean onGround, @Nonnull ForceProvider[] forceProvider)`
  - Executes `update` behavior.
- `updatePositionBeforeVelocity(@Nonnull PhysicsBodyState before, @Nonnull PhysicsBodyState after, double dt)`
  - Executes `updatePositionBeforeVelocity` behavior.
- `updatePositionAfterVelocity(@Nonnull PhysicsBodyState before, @Nonnull PhysicsBodyState after, double dt)`
  - Executes `updatePositionAfterVelocity` behavior.
- `updateAndClampVelocity(@Nonnull PhysicsBodyState before, @Nonnull PhysicsBodyState after, double dt)`
  - Executes `updateAndClampVelocity` behavior.
- `updateVelocity(@Nonnull PhysicsBodyState before, @Nonnull PhysicsBodyState after, double dt)`
  - Executes `updateVelocity` behavior.
- `computeAcceleration(double mass)`
  - Executes `computeAcceleration` behavior.
- `computeAcceleration(@Nonnull PhysicsBodyState state, boolean onGround, @Nonnull ForceProvider[] forceProviders, double mass, double timeStep)`
  - Executes `computeAcceleration` behavior.
- `assignAcceleration(@Nonnull PhysicsBodyState state)`
  - Executes `assignAcceleration` behavior.
- `addAcceleration(@Nonnull PhysicsBodyState state, double scale)`
  - Executes `addAcceleration` behavior.
- `addAcceleration(@Nonnull PhysicsBodyState state)`
  - Executes `addAcceleration` behavior.
- `convertAccelerationToVelocity(@Nonnull PhysicsBodyState before, @Nonnull PhysicsBodyState after, double scale)`
  - Executes `convertAccelerationToVelocity` behavior.

## Notes
- No additional notes.
