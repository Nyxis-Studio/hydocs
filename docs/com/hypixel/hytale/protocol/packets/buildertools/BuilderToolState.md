# BuilderToolState

## Overview
- Documentation for `BuilderToolState`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.buildertools`.

## Constructors
- `BuilderToolState()`
  - Creates a `BuilderToolState` instance.
- `BuilderToolState(@Nullable String id, boolean isBrush, @Nullable BuilderToolBrushData brushData, @Nullable Map<String, BuilderToolArg> args)`
  - Creates a `BuilderToolState` instance.
- `BuilderToolState(@Nonnull BuilderToolState other)`
  - Creates a `BuilderToolState` instance.

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
