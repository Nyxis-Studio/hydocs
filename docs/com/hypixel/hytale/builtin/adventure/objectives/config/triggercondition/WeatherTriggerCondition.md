**Source Hash:** `cbac9ddf6abf8f378d278d5ba9d6a6dcd5a6d6788602cb9dd3e82c8e69e43db3`
**Last Updated:** 2026-01-18T19:27:21-03:00

# WeatherTriggerCondition

## Overview
Trigger condition that activates objectives based on specific weather conditions at the player's location. This class extends ObjectiveLocationTriggerCondition to check if the current weather matches any of the configured weather types, enabling weather-dependent objective triggers like "collect rainwater during thunderstorms" or "build snowmen during blizzards."

## Field Descriptions
- `CODEC`: BuilderCodec for serializing and deserializing instances. Validates weather IDs and converts them to efficient integer indexes after decoding for fast lookups.
- `WEATHER_RESOURCE_RESOURCE_TYPE`: Resource type for accessing weather data from the world component system.
- `TRANSFORM_COMPONENT_TYPE`: Component type for accessing entity position information needed for weather checks.
- `weatherIds`: Array of weather asset IDs that satisfy this condition. Must be non-empty and contain valid weather asset names.
- `weatherIndexes`: Integer array of weather indexes created from weatherIds for efficient binary search lookups during condition evaluation.

## Constructor Descriptions
- `WeatherTriggerCondition()`: Protected default constructor used by codec for deserialization. Weather IDs are configured through codec and converted to indexes automatically.

## Method Descriptions
- `isConditionMet(@Nonnull ComponentAccessor<EntityStore> componentAccessor, @Nonnull Ref<EntityStore> ref, ObjectiveLocationMarker objectiveLocationMarker)`: Checks if the current weather at the entity's location matches any of the configured weather types. Uses binary search on sorted weather indexes for efficient lookup.
- `toString()`: Returns string representation including weather IDs array and parent class information for debugging.

## Usage Notes
- Weather indexes are pre-computed and sorted for efficient binary search during evaluation
- The condition checks weather at the entity's chunk location for accuracy
- Invalid chunk references return false to handle edge cases safely
- Weather is determined by the environment type at the specific position
- Multiple weather types can be specified for flexible triggering

## Examples
```java
// Configuration in asset file:
{
  "Type": "Weather",
  "WeatherIds": ["thunderstorm", "heavy_rain"],
  "Location": [100, 64, 200],
  "Radius": 50
}

// The condition will trigger when weather is either thunderstorm or heavy rain
// at the specified location within the radius
```
