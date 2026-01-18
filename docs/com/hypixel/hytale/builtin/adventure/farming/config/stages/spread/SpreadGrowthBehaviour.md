**Source Hash:** `d21a58d7e704596e0adf23789ee9b84a9a2974f76f78c9bef66382d1cc57bb1a`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# SpreadGrowthBehaviour

## Overview
Abstract base for spread growth behaviors. Defines optional world location conditions and a polymorphic codec map.

## Field Descriptions
- `CODEC`: Codec map keyed by the `Type` field for polymorphic decoding.
- `BASE_CODEC`: Base codec that supports location conditions.
- `worldLocationConditions`: Optional location conditions required for placement.

## Constructor Descriptions
- None. Use subclass codecs via `CODEC`.

## Method Descriptions
- `execute(ComponentAccessor<ChunkStore> commandBuffer, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, int worldX, int worldY, int worldZ, float newSpreadRate)`: Executes the spread behavior at the given location.
- `validatePosition(World world, int worldX, int worldY, int worldZ)`: Returns true when all configured location conditions pass.

## Usage Notes
- `validatePosition` returns true when no conditions are configured.

## Examples
```java
boolean ok = behaviour.validatePosition(world, x, y, z);
```
