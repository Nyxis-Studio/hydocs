**Source Hash:** `d39e174d8c7d6007f75d0e76caf4247485db411252817035e8329f7cae9dd2b2`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# MemoriesGameplayConfig

## Overview
Gameplay configuration for the memories feature, defining level thresholds, particle effects, and the catch-item ID used when recording memories.

## Field Descriptions
- `ID`: Gameplay config ID used for plugin registration.
- `CODEC`: Builder codec for loading configuration values.
- `memoriesAmountPerLevel`: Array of memory counts needed to reach each level.
- `memoriesRecordParticles`: Particle effect ID played when recording memories.
- `memoriesCatchItemId`: Item ID given when a memory is captured.

## Constructor Descriptions
- `MemoriesGameplayConfig()`: Creates the configuration instance used by the codec.

## Method Descriptions
- `get(GameplayConfig config)`: Returns the memories gameplay config from the gameplay config, if present.
- `getMemoriesAmountPerLevel()`: Returns the level threshold array.
- `getMemoriesRecordParticles()`: Returns the particle effect ID.
- `getMemoriesCatchItemId()`: Returns the catch-item ID.

## Usage Notes
- The level threshold array is used by `MemoriesPlugin` to compute current and next levels.

## Examples
```java
MemoriesGameplayConfig config = MemoriesGameplayConfig.get(gameplayConfig);
```
