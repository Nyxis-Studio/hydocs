# PhysicsMath

## Overview
- Documentation for `PhysicsMath`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.physics.util`.

## Constructors
- None.

## Methods
- `getAcceleration(double speed, double terminalSpeed)`
  - Executes `getAcceleration` behavior.
- `getTerminalVelocity(double mass, double density, double areaMillimetersSquared, double dragCoefficient)`
  - Executes `getTerminalVelocity` behavior.
- `getRelativeDensity(Vector3d position, Box boundingBox)`
  - Executes `getRelativeDensity` behavior.
- `computeDragCoefficient(double terminalSpeed, double area, double mass, double gravity)`
  - Executes `computeDragCoefficient` behavior.
- `computeTerminalSpeed(double dragCoefficient, double area, double mass, double gravity)`
  - Executes `computeTerminalSpeed` behavior.
- `computeProjectedArea(double x, double y, double z, @Nonnull Box box)`
  - Executes `computeProjectedArea` behavior.
- `computeProjectedArea(@Nonnull Vector3d direction, @Nonnull Box box)`
  - Executes `computeProjectedArea` behavior.
- `volumeOfIntersection(@Nonnull Box a, @Nonnull Vector3d posA, @Nonnull Box b, @Nonnull Vector3d posB)`
  - Executes `volumeOfIntersection` behavior.
- `volumeOfIntersection(@Nonnull Box a, @Nonnull Vector3d posA, @Nonnull Box b, double posBX, double posBY, double posBZ)`
  - Executes `volumeOfIntersection` behavior.
- `lengthOfIntersection(double aMin, double aMax, double bMin, double bMax)`
  - Executes `lengthOfIntersection` behavior.
- `headingFromDirection(double x, double z)`
  - Executes `headingFromDirection` behavior.
- `normalizeAngle(float rad)`
  - Executes `normalizeAngle` behavior.
- `normalizeTurnAngle(float rad)`
  - Executes `normalizeTurnAngle` behavior.
- `pitchFromDirection(double x, double y, double z)`
  - Executes `pitchFromDirection` behavior.
- `vectorFromAngles(float heading, float pitch, @Nonnull Vector3d outDirection)`
  - Executes `vectorFromAngles` behavior.
- `pitchX(float pitch)`
  - Executes `pitchX` behavior.
- `pitchY(float pitch)`
  - Executes `pitchY` behavior.
- `headingX(float heading)`
  - Executes `headingX` behavior.
- `headingZ(float heading)`
  - Executes `headingZ` behavior.

## Notes
- No additional notes.
