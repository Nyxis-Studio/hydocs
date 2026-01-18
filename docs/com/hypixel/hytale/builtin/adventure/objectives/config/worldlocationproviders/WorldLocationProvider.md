**Source Hash:** `d72f66c402b0f9220c0fef44b66ffbf57bba90ba19685d0486a6c8c7deace226`
**Last Updated:** 2026-01-18T19:03:47-03:00

# WorldLocationProvider

## Overview
Abstract base class for providers that determine valid world locations for objective tasks. These providers implement various algorithms to find suitable locations in the world based on different criteria like block types, height constraints, or proximity to other features. They are used by the objective system to dynamically determine where tasks can occur.

## Field Descriptions
- `CODEC`: CodecMapCodec that manages registration and serialization of different WorldLocationProvider types. Uses "Type" as the discriminator key for polymorphic deserialization.
- `BASE_CODEC`: BuilderCodec for the abstract base class, providing common serialization functionality for all provider implementations.

## Constructor Descriptions
No public constructors - this is an abstract base class instantiated through specific implementations.

## Method Descriptions
- `runCondition(World var1, Vector3i var2)`: Abstract method that evaluates a location in the world and returns a potentially modified location or null if the condition is not met. The Vector3i parameter represents the input location to evaluate.
- `equals(Object var1)`: Abstract method that subclasses must implement to provide value equality comparison for provider instances.
- `hashCode()`: Abstract method that subclasses must implement to provide consistent hash codes for provider instances.
- `toString()`: Returns a basic string representation for debugging. Subclasses should override to provide more specific information.

## Registered Provider Types
The static initializer registers three concrete provider implementations:
- **LookBlocksBelow**: Checks blocks below the given location
- **LocationRadius**: Validates locations within a radius of a reference point  
- **TagBlockHeight**: Checks for blocks with specific tags at certain heights

## Usage Notes
- Providers are polymorphically serialized/deserialized using the CODEC system
- Each provider type implements specific location validation logic
- Providers can modify the input location or return null to reject it
- Used by objective tasks to find valid spawning or interaction locations
- Providers should be stateless to ensure consistent behavior

## Examples
```java
// Providers are typically configured in asset files:
{
  "Type": "LocationRadius",
  "Location": [100, 64, 200],
  "Radius": 50
}

// Or used programmatically in objective systems:
Vector3i validLocation = provider.runCondition(world, candidateLocation);
if (validLocation != null) {
    // Use the validated/modified location for objective task
}
```
