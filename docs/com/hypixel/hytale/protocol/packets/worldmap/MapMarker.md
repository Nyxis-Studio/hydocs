# MapMarker

## Overview
- Documentation for `MapMarker`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.worldmap`.

## Constructors
- `MapMarker()`
  - Creates a `MapMarker` instance.
- `MapMarker(@Nullable String id, @Nullable String name, @Nullable String markerImage, @Nullable Transform transform, @Nullable ContextMenuItem[] contextMenuItems)`
  - Creates a `MapMarker` instance.
- `MapMarker(@Nonnull MapMarker other)`
  - Creates a `MapMarker` instance.

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
