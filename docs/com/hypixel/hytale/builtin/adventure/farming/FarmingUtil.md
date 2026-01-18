# FarmingUtil

**Overview**
Utility functions for ticking farm stages and handling harvest logic.
Computes growth timing, applies modifiers, and spawns drops.

**Constructors**
- Not applicable. Static utility class.

**Methods**
- `tickFarming(CommandBuffer<ChunkStore> commandBuffer, BlockSection blockSection, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, FarmingBlock farmingBlock, int x, int y, int z, boolean initialTick)`: advances farming stages and schedules ticks.
- `harvest(World world, ComponentAccessor<EntityStore> store, Ref<EntityStore> ref, BlockType blockType, int rotationIndex, Vector3i blockPosition)`: entry point for harvesting with permission checks.
- `generateCapturedNPCMetadata(ComponentAccessor<EntityStore> componentAccessor, Ref<EntityStore> entityRef, int roleIndex)`: builds capture metadata for NPCs.
- `harvest0(ComponentAccessor<EntityStore> store, Ref<EntityStore> ref, BlockType blockType, int rotationIndex, Vector3i blockPosition)`: harvests and optionally re-seeds a block.
- `giveDrops(ComponentAccessor<EntityStore> store, Ref<EntityStore> ref, Vector3d origin, BlockType blockType)`: delivers harvest drops to a player.

**Notes**
- Uses growth modifiers to scale stage duration.
