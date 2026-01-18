# UpdateWorldMap

## Overview
- Documentation for `UpdateWorldMap`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.worldmap`.

## Constructors
- `UpdateWorldMap()`
  - Creates a `UpdateWorldMap` instance.
- `UpdateWorldMap(@Nullable MapChunk[] chunks, @Nullable MapMarker[] addedMarkers, @Nullable String[] removedMarkers)`
  - Creates a `UpdateWorldMap` instance.
- `UpdateWorldMap(@Nonnull UpdateWorldMap other)`
  - Creates a `UpdateWorldMap` instance.

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
