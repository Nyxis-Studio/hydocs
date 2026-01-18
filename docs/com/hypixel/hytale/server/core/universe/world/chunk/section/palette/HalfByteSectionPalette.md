# HalfByteSectionPalette

## Overview
- Documentation for `HalfByteSectionPalette`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.chunk.section.palette`.

## Constructors
- `HalfByteSectionPalette()`
  - Creates a `HalfByteSectionPalette` instance.
- `HalfByteSectionPalette(Int2ByteMap externalToInternal, Byte2IntMap internalToExternal, BitSet internalIdSet, Byte2ShortMap internalIdCount, byte[] blocks)`
  - Creates a `HalfByteSectionPalette` instance.
- `HalfByteSectionPalette(@Nonnull int[] data, int[] unique, int count)`
  - Creates a `HalfByteSectionPalette` instance.

## Methods
- `getPaletteType()`
  - Executes `getPaletteType` behavior.
- `set0(int idx, byte b)`
  - Executes `set0` behavior.
- `get0(int idx)`
  - Executes `get0` behavior.
- `shouldDemote()`
  - Executes `shouldDemote` behavior.
- `demote()`
  - Executes `demote` behavior.
- `promote()`
  - Executes `promote` behavior.
- `isValidInternalId(int internalId)`
  - Executes `isValidInternalId` behavior.
- `unsignedInternalId(byte internalId)`
  - Executes `unsignedInternalId` behavior.
- `sUnsignedInternalId(byte internalId)`
  - Executes `sUnsignedInternalId` behavior.
- `fromBytePalette(@Nonnull ByteSectionPalette section)`
  - Executes `fromBytePalette` behavior.

## Notes
- No additional notes.
