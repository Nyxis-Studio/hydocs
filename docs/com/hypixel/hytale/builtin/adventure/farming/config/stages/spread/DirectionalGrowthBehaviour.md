# DirectionalGrowthBehaviour

**Overview**
Spread growth behavior that places blocks in horizontal/vertical ranges.
Uses weighted block types and directional vertical spread.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `getBlockTypes()`: returns weighted block types.
- `getHorizontalRange()`: returns horizontal range.
- `getVerticalRange()`: returns vertical range.
- `getVerticalDirection()`: returns the vertical direction mode.
- `execute(ComponentAccessor<ChunkStore> commandBuffer, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, int worldX, int worldY, int worldZ, float newSpreadRate)`: tries to place blocks and decays spread.
- `toString()`: returns a diagnostic string.

**Notes**
- Uses physics checks to validate placement.

---

# DirectionalGrowthBehaviour.VerticalDirection

**Overview**
Enum defining vertical spread direction.

**Methods**
- `getValue()`: returns the direction multiplier.

---

# DirectionalGrowthBehaviour.BlockTypeWeight

**Overview**
Weighted entry that maps to a block type for spreading.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `getWeight()`: returns the weight.
- `getBlockTypeKey()`: returns the block type id.
- `toString()`: returns a diagnostic string.
