# EditorSelection

## Overview
- Documentation for `EditorSelection`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.interface_`.

## Constructors
- `EditorSelection()`
  - Creates a `EditorSelection` instance.
- `EditorSelection(int minX, int minY, int minZ, int maxX, int maxY, int maxZ)`
  - Creates a `EditorSelection` instance.
- `EditorSelection(@Nonnull EditorSelection other)`
  - Creates a `EditorSelection` instance.

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
