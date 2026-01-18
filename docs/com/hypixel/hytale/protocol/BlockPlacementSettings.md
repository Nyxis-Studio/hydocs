# BlockPlacementSettings

## Overview
- Documentation for `BlockPlacementSettings`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `BlockPlacementSettings()`
  - Creates a `BlockPlacementSettings` instance.
- `BlockPlacementSettings(boolean allowRotationKey, boolean placeInEmptyBlocks, @Nonnull BlockPreviewVisibility previewVisibility, @Nonnull BlockPlacementRotationMode rotationMode, int wallPlacementOverrideBlockId, int floorPlacementOverrideBlockId, int ceilingPlacementOverrideBlockId)`
  - Creates a `BlockPlacementSettings` instance.
- `BlockPlacementSettings(@Nonnull BlockPlacementSettings other)`
  - Creates a `BlockPlacementSettings` instance.

## Methods
- `deserialize(@Nonnull ByteBuf buf, int offset)`
  - Executes `deserialize` behavior.
- `computeBytesConsumed(@Nonnull ByteBuf buf, int offset)`
  - Executes `computeBytesConsumed` behavior.
- `serialize(@Nonnull ByteBuf buf)`
  - Executes `serialize` behavior.
- `computeSize()`
  - Executes `computeSize` behavior.
- `validateStructure(@Nonnull ByteBuf buffer, int offset)`
  - Executes `validateStructure` behavior.
- `clone()`
  - Executes `clone` behavior.
- `equals(Object obj)`
  - Executes `equals` behavior.
- `hashCode()`
  - Executes `hashCode` behavior.

## Notes
- No additional notes.
