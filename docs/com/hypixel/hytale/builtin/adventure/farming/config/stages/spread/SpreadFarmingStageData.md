# SpreadFarmingStageData

**Overview**
Farming stage that executes one or more spread behaviors multiple times.
Tracks execution limits and decay of spread rate for spawned blocks.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `getExecutions()`: returns execution range.
- `getSpreadDecayPercent()`: returns decay range.
- `getSpreadGrowthBehaviours()`: returns the behavior array.
- `implementsShouldStop()`: signals that `shouldStop` is supported.
- `shouldStop(ComponentAccessor<ChunkStore> commandBuffer, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, int x, int y, int z)`: checks whether the stage should stop executing.
- `apply(ComponentAccessor<ChunkStore> commandBuffer, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, int x, int y, int z, FarmingStageData previousStage)`: runs behaviors and updates execution count.
- `remove(ComponentAccessor<ChunkStore> commandBuffer, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, int x, int y, int z)`: no additional removal logic.
- `toString()`: returns a diagnostic string.

**Notes**
- Validates execution and decay ranges during decode.
