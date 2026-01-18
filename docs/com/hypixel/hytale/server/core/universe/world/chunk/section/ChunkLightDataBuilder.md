**Source Hash:** `89282f51a6f937633a43245657cb4609e1f2450e85bbf316a0edb32e2a49dc75`

# ChunkLightDataBuilder

## Overview

## Constructor Descriptions
- `ChunkLightDataBuilder(short changeId)`
  - Creates a `ChunkLightDataBuilder` instance.
- `ChunkLightDataBuilder(@Nonnull ChunkLightData lightData, short changeId)`
  - Creates a `ChunkLightDataBuilder` instance.

## Method Descriptions
- `findSegments(@Nonnull ByteBuf light, int position, @Nonnull BitSet currentSegments)`: Add description.
  - Executes `findSegments` behavior.
- `setBlockLight(int x, int y, int z, byte red, byte green, byte blue)`: Add description.
  - Executes `setBlockLight` behavior.
- `setBlockLight(int index, byte red, byte green, byte blue)`: Add description.
  - Executes `setBlockLight` behavior.
- `setSkyLight(int x, int y, int z, byte light)`: Add description.
  - Executes `setSkyLight` behavior.
- `setSkyLight(int index, byte light)`: Add description.
  - Executes `setSkyLight` behavior.
- `setLight(int index, int channel, byte value)`: Add description.
  - Executes `setLight` behavior.
- `setLightRaw(int index, short value)`: Add description.
  - Executes `setLightRaw` behavior.
- `build()`: Add description.
  - Executes `build` behavior.
- `serializeOctree(@Nonnull ByteBuf to, int position, int segmentIndex)`: Add description.
  - Executes `serializeOctree` behavior.
- `setTraverse(@Nonnull ByteBuf local, @Nonnull BitSet currentSegments, int index, int pointer, int depth, short value)`: Add description.
  - Executes `setTraverse` behavior.
- `growSegment(@Nonnull ByteBuf local, @Nonnull BitSet currentSegments, short val)`: Add description.
  - Executes `growSegment` behavior.
- `toStringOctree()`: Add description.
  - Executes `toStringOctree` behavior.
- `octreeToString(@Nonnull ByteBuf buffer)`: Add description.
  - Executes `octreeToString` behavior.
- `octreeToString(@Nonnull ByteBuf buffer, int pointer, @Nonnull StringBuffer out, int recursion)`: Add description.
  - Executes `octreeToString` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.

## Notes
- No additional notes.
