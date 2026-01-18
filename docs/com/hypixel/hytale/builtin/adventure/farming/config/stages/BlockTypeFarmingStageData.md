# BlockTypeFarmingStageData

**Overview**
Farming stage that replaces the block with a specific block type.
Uses a block id reference and validates it against the asset registry.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `getBlock()`: returns the block id string.
- `apply(ComponentAccessor<ChunkStore> commandBuffer, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, int x, int y, int z, FarmingStageData previousStage)`: replaces the block with the target type.
- `toString()`: returns a diagnostic string.

**Notes**
- Validates block ids using `BlockType.VALIDATOR_CACHE`.
