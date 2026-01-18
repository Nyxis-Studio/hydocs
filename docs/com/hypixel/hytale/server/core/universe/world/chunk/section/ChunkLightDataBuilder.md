# ChunkLightDataBuilder

## Overview
- Documentation for `ChunkLightDataBuilder`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.chunk.section`.

## Constructors
- `ChunkLightDataBuilder(short changeId)`
  - Creates a `ChunkLightDataBuilder` instance.
- `ChunkLightDataBuilder(@Nonnull ChunkLightData lightData, short changeId)`
  - Creates a `ChunkLightDataBuilder` instance.

## Methods
- `findSegments(@Nonnull ByteBuf light, int position, @Nonnull BitSet currentSegments)`
  - Executes `findSegments` behavior.
- `setBlockLight(int x, int y, int z, byte red, byte green, byte blue)`
  - Executes `setBlockLight` behavior.
- `setBlockLight(int index, byte red, byte green, byte blue)`
  - Executes `setBlockLight` behavior.
- `setSkyLight(int x, int y, int z, byte light)`
  - Executes `setSkyLight` behavior.
- `setSkyLight(int index, byte light)`
  - Executes `setSkyLight` behavior.
- `setLight(int index, int channel, byte value)`
  - Executes `setLight` behavior.
- `setLightRaw(int index, short value)`
  - Executes `setLightRaw` behavior.
- `build()`
  - Executes `build` behavior.
- `serializeOctree(@Nonnull ByteBuf to, int position, int segmentIndex)`
  - Executes `serializeOctree` behavior.
- `setTraverse(@Nonnull ByteBuf local, @Nonnull BitSet currentSegments, int index, int pointer, int depth, short value)`
  - Executes `setTraverse` behavior.
- `growSegment(@Nonnull ByteBuf local, @Nonnull BitSet currentSegments, short val)`
  - Executes `growSegment` behavior.
- `toStringOctree()`
  - Executes `toStringOctree` behavior.
- `octreeToString(@Nonnull ByteBuf buffer)`
  - Executes `octreeToString` behavior.
- `octreeToString(@Nonnull ByteBuf buffer, int pointer, @Nonnull StringBuffer out, int recursion)`
  - Executes `octreeToString` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
