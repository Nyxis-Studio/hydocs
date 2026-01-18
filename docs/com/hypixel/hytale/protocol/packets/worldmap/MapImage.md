# MapImage

## Overview
- Documentation for `MapImage`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.worldmap`.

## Constructors
- `MapImage()`
  - Creates a `MapImage` instance.
- `MapImage(int width, int height, @Nullable int[] data)`
  - Creates a `MapImage` instance.
- `MapImage(@Nonnull MapImage other)`
  - Creates a `MapImage` instance.

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
