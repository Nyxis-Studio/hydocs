# UpdateWorldMapSettings

## Overview
- Documentation for `UpdateWorldMapSettings`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.worldmap`.

## Constructors
- `UpdateWorldMapSettings()`
  - Creates a `UpdateWorldMapSettings` instance.
- `UpdateWorldMapSettings(boolean enabled, @Nullable Map<Short, BiomeData> biomeDataMap, boolean allowTeleportToCoordinates, boolean allowTeleportToMarkers, float defaultScale, float minScale, float maxScale)`
  - Creates a `UpdateWorldMapSettings` instance.
- `UpdateWorldMapSettings(@Nonnull UpdateWorldMapSettings other)`
  - Creates a `UpdateWorldMapSettings` instance.

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
