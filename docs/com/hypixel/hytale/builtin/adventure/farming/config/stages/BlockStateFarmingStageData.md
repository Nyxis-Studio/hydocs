# BlockStateFarmingStageData

**Overview**
Farming stage that swaps a block to a new state variant.
Uses a block state id to resolve the target block type.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `getState()`: returns the target state string.
- `apply(ComponentAccessor<ChunkStore> commandBuffer, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, int x, int y, int z, FarmingStageData previousStage)`: replaces the block with the resolved state.
- `toString()`: returns a diagnostic string.

**Notes**
- Keeps rotation when swapping the block type.
