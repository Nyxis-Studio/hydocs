# ShortSectionPalette

## Overview
- Documentation for `ShortSectionPalette`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.chunk.section.palette`.

## Constructors
- `ShortSectionPalette()`
  - Creates a `ShortSectionPalette` instance.
- `ShortSectionPalette(Int2ShortMap externalToInternal, Short2IntMap internalToExternal, BitSet internalIdSet, Short2ShortMap internalIdCount, short[] blocks)`
  - Creates a `ShortSectionPalette` instance.
- `ShortSectionPalette(@Nonnull int[] data, int[] unique, int count)`
  - Creates a `ShortSectionPalette` instance.
- `ShortSectionPalette(shortExternalToInternal, shortInternalToExternal, shortInternalIdSet, shortInternalIdCount, shortBlocks)`
  - Creates a `ShortSectionPalette` instance.

## Methods
- `getPaletteType()`
  - Executes `getPaletteType` behavior.
- `get0(int idx)`
  - Executes `get0` behavior.
- `set0(int idx, short s)`
  - Executes `set0` behavior.
- `shouldDemote()`
  - Executes `shouldDemote` behavior.
- `demote()`
  - Executes `demote` behavior.
- `promote()`
  - Executes `promote` behavior.
- `isValidInternalId(int internalId)`
  - Executes `isValidInternalId` behavior.
- `fromBytePalette(@Nonnull ByteSectionPalette section)`
  - Executes `fromBytePalette` behavior.

## Notes
- No additional notes.
