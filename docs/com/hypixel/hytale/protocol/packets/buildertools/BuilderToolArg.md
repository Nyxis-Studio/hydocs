# BuilderToolArg

## Overview
- Documentation for `BuilderToolArg`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.buildertools`.

## Constructors
- `BuilderToolArg()`
  - Creates a `BuilderToolArg` instance.
- `BuilderToolArg(boolean required, @Nonnull BuilderToolArgType argType, @Nullable BuilderToolBoolArg boolArg, @Nullable BuilderToolFloatArg floatArg, @Nullable BuilderToolIntArg intArg, @Nullable BuilderToolStringArg stringArg, @Nullable BuilderToolBlockArg blockArg, @Nullable BuilderToolMaskArg maskArg, @Nullable BuilderToolBrushShapeArg brushShapeArg, @Nullable BuilderToolBrushOriginArg brushOriginArg, @Nullable BuilderToolBrushAxisArg brushAxisArg, @Nullable BuilderToolRotationArg rotationArg, @Nullable BuilderToolOptionArg optionArg)`
  - Creates a `BuilderToolArg` instance.
- `BuilderToolArg(@Nonnull BuilderToolArg other)`
  - Creates a `BuilderToolArg` instance.

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
