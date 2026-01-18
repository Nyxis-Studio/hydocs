# SetBlockCmd

## Overview
- Documentation for `SetBlockCmd`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.world`.

## Constructors
- `SetBlockCmd()`
  - Creates a `SetBlockCmd` instance.
- `SetBlockCmd(short index, int blockId, short filler, byte rotation)`
  - Creates a `SetBlockCmd` instance.
- `SetBlockCmd(@Nonnull SetBlockCmd other)`
  - Creates a `SetBlockCmd` instance.

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
