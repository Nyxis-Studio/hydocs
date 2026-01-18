# GroupSteeringAccumulator

## Overview
- Documentation for `GroupSteeringAccumulator`.
- Declared as a class in `com.hypixel.hytale.server.npc.movement`.

## Constructors
- None.

## Methods
- `begin(double x, double y, double z, double xViewDirection, double yViewDirection, double zViewDirection)`
  - Executes `begin` behavior.
- `begin(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `begin` behavior.
- `processEntity(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `processEntity` behavior.
- `processEntity(@Nonnull Ref<EntityStore> ref, double distanceWeight, double positionWeight, double velocityWeight, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `processEntity` behavior.
- `end()`
  - Executes `end` behavior.
- `setComponentSelector(Vector3d componentSelector)`
  - Executes `setComponentSelector` behavior.
- `setMaxRange(double maxRange)`
  - Executes `setMaxRange` behavior.
- `setViewConeHalfAngleCosine(float collisionViewHalfAngleCosine)`
  - Executes `setViewConeHalfAngleCosine` behavior.
- `getSumOfVelocities()`
  - Executes `getSumOfVelocities` behavior.
- `getSumOfDistances()`
  - Executes `getSumOfDistances` behavior.
- `getSumOfPositions()`
  - Executes `getSumOfPositions` behavior.
- `getCount()`
  - Executes `getCount` behavior.

## Notes
- No additional notes.
