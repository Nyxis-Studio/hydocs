# CoopResidentComponent

**Overview**
Component that tracks an entity's coop location and despawn state.
Used by farming systems to bind residents to coop positions.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `getComponentType()`: returns the component type from `FarmingPlugin`.
- `setCoopLocation(Vector3i coopLocation)`: updates the coop location.
- `getCoopLocation()`: returns the coop location.
- `setMarkedForDespawn(boolean markedForDespawn)`: sets the despawn flag.
- `getMarkedForDespawn()`: returns the despawn flag.
- `clone()`: copies the component including location and despawn state.

**Notes**
- Stores the location as a `Vector3i`.
