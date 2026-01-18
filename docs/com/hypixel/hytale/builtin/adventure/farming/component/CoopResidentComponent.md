**Source Hash:** `ddbc062d5ac2fdca8f90c4cef1008a16bdf2e8a0fe0193635ad5490f1c8ad241`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# CoopResidentComponent

## Overview
Component that tracks an entity's coop location and despawn state. Used by farming systems to bind residents to coop positions.

## Field Descriptions
- `CODEC`: Builder codec for coop resident components.
- `coopLocation`: Location of the associated coop block.
- `markedForDespawn`: Whether the resident should be removed.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `getComponentType()`: Returns the component type registered by `FarmingPlugin`.
- `setCoopLocation(Vector3i coopLocation)`: Updates the coop location.
- `getCoopLocation()`: Returns the coop location.
- `setMarkedForDespawn(boolean markedForDespawn)`: Sets the despawn flag.
- `getMarkedForDespawn()`: Returns the despawn flag.
- `clone()`: Copies the component with the same coop location and despawn flag.

## Usage Notes
- `clone()` assigns the vector contents rather than sharing the instance.

## Examples
```java
CoopResidentComponent component = new CoopResidentComponent();
component.setMarkedForDespawn(true);
```
