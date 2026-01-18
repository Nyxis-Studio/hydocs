**Source Hash:** `3a10dec227de6e5c1069ce93aef0bcc036ac26979733e5d7241b0617cc940204`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# DirectionalGrowthBehaviour

## Overview
Spread growth behavior that places blocks within horizontal and vertical ranges. Uses weighted block types and directional vertical spread.

## Field Descriptions
- `CODEC`: Builder codec for directional growth.
- `PLACE_BLOCK_TRIES`: Number of attempts to place a block per execution.
- `blockTypes`: Weighted block type entries used for placement.
- `horizontalRange`: Horizontal spread range.
- `verticalRange`: Vertical spread range.
- `verticalDirection`: Direction setting for vertical spread.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `getBlockTypes()`: Returns weighted block types.
- `getHorizontalRange()`: Returns horizontal range.
- `getVerticalRange()`: Returns vertical range.
- `getVerticalDirection()`: Returns the vertical direction mode.
- `execute(ComponentAccessor<ChunkStore> commandBuffer, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, int worldX, int worldY, int worldZ, float newSpreadRate)`: Chooses a target location within ranges, validates placement with block physics, places the block, and decays spread on the spawned block.
- `toString()`: Returns a diagnostic string.

## Usage Notes
- Uses block physics checks and replacement rules to validate placement.

## Examples
```java
behaviour.execute(buffer, sectionRef, blockRef, worldX, worldY, worldZ, 0.5f);
```

---

# DirectionalGrowthBehaviour.VerticalDirection

## Overview
Enum defining vertical spread direction.

## Field Descriptions
- `DOWNWARDS`: Spread downward with value -1.
- `BOTH`: Allow both upward and downward spread.
- `UPWARDS`: Spread upward with value 1.

## Method Descriptions
- `getValue()`: Returns the direction multiplier.

---

# DirectionalGrowthBehaviour.BlockTypeWeight

## Overview
Weighted entry that maps to a block type for spreading.

## Field Descriptions
- `CODEC`: Builder codec for block type weights.
- `weight`: Weight for random selection.
- `blockTypeKey`: Block type id to place.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `getWeight()`: Returns the weight.
- `getBlockTypeKey()`: Returns the block type id.
- `toString()`: Returns a diagnostic string.
