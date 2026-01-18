# BlockChange

## Overview
- Documentation for `BlockChange`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.interface_`.

## Constructors
- `BlockChange()`
  - Creates a `BlockChange` instance.
- `BlockChange(int x, int y, int z, int block, byte rotation)`
  - Creates a `BlockChange` instance.
- `BlockChange(@Nonnull BlockChange other)`
  - Creates a `BlockChange` instance.

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
