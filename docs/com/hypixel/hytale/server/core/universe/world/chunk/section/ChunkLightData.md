# ChunkLightData

## Overview
- Documentation for `ChunkLightData`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.chunk.section`.

## Constructors
- `ChunkLightData(null, 0)`
  - Creates a `ChunkLightData` instance.
- `ChunkLightData(ByteBuf light, short changeId)`
  - Creates a `ChunkLightData` instance.
- `ChunkLightData(buffer.copy()`
  - Creates a `ChunkLightData` instance.
- `ChunkLightData(null, changeId)`
  - Creates a `ChunkLightData` instance.

## Methods
- `getChangeId()`
  - Executes `getChangeId` behavior.
- `getRedBlockLight(int x, int y, int z)`
  - Executes `getRedBlockLight` behavior.
- `getRedBlockLight(int index)`
  - Executes `getRedBlockLight` behavior.
- `getGreenBlockLight(int x, int y, int z)`
  - Executes `getGreenBlockLight` behavior.
- `getGreenBlockLight(int index)`
  - Executes `getGreenBlockLight` behavior.
- `getBlueBlockLight(int x, int y, int z)`
  - Executes `getBlueBlockLight` behavior.
- `getBlueBlockLight(int index)`
  - Executes `getBlueBlockLight` behavior.
- `getBlockLightIntensity(int x, int y, int z)`
  - Executes `getBlockLightIntensity` behavior.
- `getBlockLightIntensity(int index)`
  - Executes `getBlockLightIntensity` behavior.
- `getBlockLight(int x, int y, int z)`
  - Executes `getBlockLight` behavior.
- `getBlockLight(int index)`
  - Executes `getBlockLight` behavior.
- `getSkyLight(int x, int y, int z)`
  - Executes `getSkyLight` behavior.
- `getSkyLight(int index)`
  - Executes `getSkyLight` behavior.
- `getLight(int index, int channel)`
  - Executes `getLight` behavior.
- `getLightRaw(int x, int y, int z)`
  - Executes `getLightRaw` behavior.
- `getLightRaw(int index)`
  - Executes `getLightRaw` behavior.
- `getTraverse(@Nonnull ByteBuf local, int index, int pointer, int depth)`
  - Executes `getTraverse` behavior.
- `serialize(@Nonnull ByteBuf buf)`
  - Executes `serialize` behavior.
- `serializeOctree(@Nonnull ByteBuf buf, int position)`
  - Executes `serializeOctree` behavior.
- `serializeForPacket(@Nonnull ByteBuf buf)`
  - Executes `serializeForPacket` behavior.
- `serializeOctreeForPacket(@Nonnull ByteBuf buf, int position)`
  - Executes `serializeOctreeForPacket` behavior.
- `deserialize(@Nonnull ByteBuf buf, int version)`
  - Executes `deserialize` behavior.
- `deserializeOctree(@Nonnull ByteBuf from, @Nonnull ByteBuf to, int position, int segmentIndex)`
  - Executes `deserializeOctree` behavior.
- `octreeToString()`
  - Executes `octreeToString` behavior.
- `combineLightValues(byte red, byte green, byte blue, byte sky)`
  - Executes `combineLightValues` behavior.
- `combineLightValues(byte red, byte green, byte blue)`
  - Executes `combineLightValues` behavior.
- `getLightValue(short value, int channel)`
  - Executes `getLightValue` behavior.

## Notes
- No additional notes.
