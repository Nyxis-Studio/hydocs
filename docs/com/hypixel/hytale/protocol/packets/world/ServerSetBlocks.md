# ServerSetBlocks

## Overview
- Documentation for `ServerSetBlocks`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.world`.

## Constructors
- `ServerSetBlocks()`
  - Creates a `ServerSetBlocks` instance.
- `ServerSetBlocks(int x, int y, int z, @Nonnull SetBlockCmd[] cmds)`
  - Creates a `ServerSetBlocks` instance.
- `ServerSetBlocks(@Nonnull ServerSetBlocks other)`
  - Creates a `ServerSetBlocks` instance.

## Methods
- `getId()`
  - Executes `getId` behavior.
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
