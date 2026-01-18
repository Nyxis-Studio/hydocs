**Source Hash:** `fb0976bbe6bbed0b47799230b0dd36eecff7ee1448f8b5583afa6377ff4bd44f`

# ChunkLightData

## Overview

## Constructor Descriptions
- `ChunkLightData(null, 0)`
  - Creates a `ChunkLightData` instance.
- `ChunkLightData(ByteBuf light, short changeId)`
  - Creates a `ChunkLightData` instance.
- `ChunkLightData(buffer.copy()`
  - Creates a `ChunkLightData` instance.
- `ChunkLightData(null, changeId)`
  - Creates a `ChunkLightData` instance.

## Method Descriptions
- `getChangeId()`: Add description.
  - Executes `getChangeId` behavior.
- `getRedBlockLight(int x, int y, int z)`: Add description.
  - Executes `getRedBlockLight` behavior.
- `getRedBlockLight(int index)`: Add description.
  - Executes `getRedBlockLight` behavior.
- `getGreenBlockLight(int x, int y, int z)`: Add description.
  - Executes `getGreenBlockLight` behavior.
- `getGreenBlockLight(int index)`: Add description.
  - Executes `getGreenBlockLight` behavior.
- `getBlueBlockLight(int x, int y, int z)`: Add description.
  - Executes `getBlueBlockLight` behavior.
- `getBlueBlockLight(int index)`: Add description.
  - Executes `getBlueBlockLight` behavior.
- `getBlockLightIntensity(int x, int y, int z)`: Add description.
  - Executes `getBlockLightIntensity` behavior.
- `getBlockLightIntensity(int index)`: Add description.
  - Executes `getBlockLightIntensity` behavior.
- `getBlockLight(int x, int y, int z)`: Add description.
  - Executes `getBlockLight` behavior.
- `getBlockLight(int index)`: Add description.
  - Executes `getBlockLight` behavior.
- `getSkyLight(int x, int y, int z)`: Add description.
  - Executes `getSkyLight` behavior.
- `getSkyLight(int index)`: Add description.
  - Executes `getSkyLight` behavior.
- `getLight(int index, int channel)`: Add description.
  - Executes `getLight` behavior.
- `getLightRaw(int x, int y, int z)`: Add description.
  - Executes `getLightRaw` behavior.
- `getLightRaw(int index)`: Add description.
  - Executes `getLightRaw` behavior.
- `getTraverse(@Nonnull ByteBuf local, int index, int pointer, int depth)`: Add description.
  - Executes `getTraverse` behavior.
- `serialize(@Nonnull ByteBuf buf)`: Add description.
  - Executes `serialize` behavior.
- `serializeOctree(@Nonnull ByteBuf buf, int position)`: Add description.
  - Executes `serializeOctree` behavior.
- `serializeForPacket(@Nonnull ByteBuf buf)`: Add description.
  - Executes `serializeForPacket` behavior.
- `serializeOctreeForPacket(@Nonnull ByteBuf buf, int position)`: Add description.
  - Executes `serializeOctreeForPacket` behavior.
- `deserialize(@Nonnull ByteBuf buf, int version)`: Add description.
  - Executes `deserialize` behavior.
- `deserializeOctree(@Nonnull ByteBuf from, @Nonnull ByteBuf to, int position, int segmentIndex)`: Add description.
  - Executes `deserializeOctree` behavior.
- `octreeToString()`: Add description.
  - Executes `octreeToString` behavior.
- `combineLightValues(byte red, byte green, byte blue, byte sky)`: Add description.
  - Executes `combineLightValues` behavior.
- `combineLightValues(byte red, byte green, byte blue)`: Add description.
  - Executes `combineLightValues` behavior.
- `getLightValue(short value, int channel)`: Add description.
  - Executes `getLightValue` behavior.

## Notes
- No additional notes.
