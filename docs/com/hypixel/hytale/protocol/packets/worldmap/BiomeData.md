# BiomeData

## Overview
- Documentation for `BiomeData`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.worldmap`.

## Constructors
- `BiomeData()`
  - Creates a `BiomeData` instance.
- `BiomeData(int zoneId, @Nullable String zoneName, @Nullable String biomeName, int biomeColor)`
  - Creates a `BiomeData` instance.
- `BiomeData(@Nonnull BiomeData other)`
  - Creates a `BiomeData` instance.

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
