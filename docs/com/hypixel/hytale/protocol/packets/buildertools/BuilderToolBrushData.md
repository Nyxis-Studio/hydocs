# BuilderToolBrushData

## Overview
- Documentation for `BuilderToolBrushData`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.buildertools`.

## Constructors
- `BuilderToolBrushData()`
  - Creates a `BuilderToolBrushData` instance.
- `BuilderToolBrushData(@Nullable BuilderToolIntArg width, @Nullable BuilderToolIntArg height, @Nullable BuilderToolIntArg thickness, @Nullable BuilderToolBoolArg capped, @Nullable BuilderToolBrushShapeArg shape, @Nullable BuilderToolBrushOriginArg origin, @Nullable BuilderToolBoolArg originRotation, @Nullable BuilderToolBrushAxisArg rotationAxis, @Nullable BuilderToolRotationArg rotationAngle, @Nullable BuilderToolBrushAxisArg mirrorAxis, @Nullable BuilderToolBlockArg material, @Nullable BuilderToolBlockArg[] favoriteMaterials, @Nullable BuilderToolMaskArg mask, @Nullable BuilderToolMaskArg maskAbove, @Nullable BuilderToolMaskArg maskNot, @Nullable BuilderToolMaskArg maskBelow, @Nullable BuilderToolMaskArg maskAdjacent, @Nullable BuilderToolMaskArg maskNeighbor, @Nullable BuilderToolStringArg[] maskCommands, @Nullable BuilderToolBoolArg useMaskCommands, @Nullable BuilderToolBoolArg invertMask)`
  - Creates a `BuilderToolBrushData` instance.
- `BuilderToolBrushData(@Nonnull BuilderToolBrushData other)`
  - Creates a `BuilderToolBrushData` instance.

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
