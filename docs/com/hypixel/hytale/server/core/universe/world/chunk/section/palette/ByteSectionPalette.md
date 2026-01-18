# ByteSectionPalette

## Overview
- Documentation for `ByteSectionPalette`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.chunk.section.palette`.

## Constructors
- `ByteSectionPalette()`
  - Creates a `ByteSectionPalette` instance.
- `ByteSectionPalette(Int2ByteMap externalToInternal, Byte2IntMap internalToExternal, BitSet internalIdSet, Byte2ShortMap internalIdCount, byte[] blocks)`
  - Creates a `ByteSectionPalette` instance.
- `ByteSectionPalette(@Nonnull int[] data, int[] unique, int count)`
  - Creates a `ByteSectionPalette` instance.

## Methods
- `getPaletteType()`
  - Executes `getPaletteType` behavior.
- `get0(int idx)`
  - Executes `get0` behavior.
- `set0(int idx, byte b)`
  - Executes `set0` behavior.
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
- `fromHalfBytePalette(@Nonnull HalfByteSectionPalette section)`
  - Executes `fromHalfBytePalette` behavior.
- `fromShortPalette(@Nonnull ShortSectionPalette section)`
  - Executes `fromShortPalette` behavior.

## Notes
- No additional notes.
