**Source Hash:** `6e69a71cd9e0f998ab5fa4f7cd36dd1c2e28b9e18493e9306a96ca31eeb3f91f`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# FarmingUtil

## Overview
Utility functions for ticking farm stages and handling harvest logic. Computes growth timing, applies modifiers, and spawns drops.

## Field Descriptions
- `MAX_SECONDS_BETWEEN_TICKS`: Upper bound for scheduling farm ticks.
- `BETWEEN_RANDOM`: Randomization window for capped tick scheduling.

## Constructor Descriptions
- None. Static utility class.

## Method Descriptions
- `tickFarming(CommandBuffer<ChunkStore> commandBuffer, BlockSection blockSection, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, FarmingBlock farmingBlock, int x, int y, int z, boolean initialTick)`: Advances farming stages, applies growth modifiers, schedules the next tick, and updates stage progress.
- `harvest(World world, ComponentAccessor<EntityStore> store, Ref<EntityStore> ref, BlockType blockType, int rotationIndex, Vector3i blockPosition)`: Harvests a block when gathering is allowed by gameplay config.
- `generateCapturedNPCMetadata(ComponentAccessor<EntityStore> componentAccessor, Ref<EntityStore> entityRef, int roleIndex)`: Creates captured NPC metadata using the entity's persistent model.
- `harvest0(ComponentAccessor<EntityStore> store, Ref<EntityStore> ref, BlockType blockType, int rotationIndex, Vector3i blockPosition)`: Handles harvesting, drop payout, and re-seeding or block break based on farming config.
- `giveDrops(ComponentAccessor<EntityStore> store, Ref<EntityStore> ref, Vector3d origin, BlockType blockType)`: Delivers harvest drops to the player via interactive pickup.

## Usage Notes
- Growth time scales with `GrowthModifierAsset` multipliers and per-stage ranges.

## Examples
```java
FarmingUtil.harvest(world, store, ref, blockType, rotationIndex, blockPos);
```
