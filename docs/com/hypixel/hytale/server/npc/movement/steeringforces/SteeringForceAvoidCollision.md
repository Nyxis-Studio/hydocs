# SteeringForceAvoidCollision

## Overview
- Documentation for `SteeringForceAvoidCollision`.
- Declared as a class in `com.hypixel.hytale.server.npc.movement.steeringforces`.

## Constructors
- None.

## Methods
- `setDebug(boolean debug)`
  - Executes `setDebug` behavior.
- `setAvoidanceMode(Role.AvoidanceMode avoidanceMode)`
  - Executes `setAvoidanceMode` behavior.
- `setSelf(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d position, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `setSelf` behavior.
- `setSelf(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d position, @Nullable Vector3d velocity, double radius, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `setSelf` behavior.
- `reset()`
  - Executes `reset` behavior.
- `compute(@Nonnull Steering output)`
  - Executes `compute` behavior.
- `add(@Nonnull Ref<EntityStore> ref, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `add` behavior.
- `setVelocityFromEntity(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `setVelocityFromEntity` behavior.
- `setRadiusFromEntity(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `setRadiusFromEntity` behavior.
- `setMaxDistance(double distance)`
  - Executes `setMaxDistance` behavior.
- `setFalloff(double falloff)`
  - Executes `setFalloff` behavior.
- `setSelfVelocity(@Nonnull Vector3d selfVelocity)`
  - Executes `setSelfVelocity` behavior.
- `getSelfVelocity()`
  - Executes `getSelfVelocity` behavior.
- `getSelfRadius()`
  - Executes `getSelfRadius` behavior.
- `setSelfRadius(double selfRadius)`
  - Executes `setSelfRadius` behavior.
- `getStrength()`
  - Executes `getStrength` behavior.
- `setStrength(double strength)`
  - Executes `setStrength` behavior.
- `getLastSteeringDirection()`
  - Executes `getLastSteeringDirection` behavior.

## Notes
- No additional notes.
