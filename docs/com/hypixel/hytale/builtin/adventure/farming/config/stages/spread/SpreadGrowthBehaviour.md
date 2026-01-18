# SpreadGrowthBehaviour

**Overview**
Abstract base for spread growth behaviors.
Defines optional world location conditions and a polymorphic codec map.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `execute(ComponentAccessor<ChunkStore> commandBuffer, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, int worldX, int worldY, int worldZ, float newSpreadRate)`: executes the spread behavior.
- `validatePosition(World world, int worldX, int worldY, int worldZ)`: checks all location conditions.

**Notes**
- `CODEC` is keyed by the `Type` field for polymorphic decoding.
