**Source Hash:** `e7c01516253fb68317da47cad11e8fec0a91a939dd7bc92e1dfb1f48ce7642b2`

# BlockSetModule

## Overview

## Constructor Descriptions
- `BlockSetModule(@Nonnull JavaPluginInit module)`
  - Creates a `BlockSetModule` instance.

## Method Descriptions
- `setup()`: Add description.
  - Executes `setup` behavior.
- `onBlockTypesChanged(@Nonnull LoadedAssetsEvent<String, BlockType, BlockTypeAssetMap<String, BlockType>> event)`: Add description.
  - Executes `onBlockTypesChanged` behavior.
- `onBlockSetsChanged(LoadedAssetsEvent<String, BlockSet, DefaultAssetMap<String, BlockSet>> event)`: Add description.
  - Executes `onBlockSetsChanged` behavior.
- `flattenBlockSets(@Nonnull BlockSetLookupTable lookupTable)`: Add description.
  - Executes `flattenBlockSets` behavior.
- `createSet(@Nonnull BlockSet blockSet, @Nonnull BlockSetLookupTable lookupTable, @Nonnull Int2ObjectMap<IntSet> flattenedSets)`: Add description.
  - Executes `createSet` behavior.
- `consume(@Nullable String[] values, @Nonnull Map<String, IntSet> map, String typeString, @Nonnull Consumer<IntSet> addAll)`: Add description.
  - Executes `consume` behavior.
- `consume(@Nullable String[][] values, @Nonnull BlockSetLookupTable lookupTable, @Nonnull Consumer<IntSet> addAll)`: Add description.
  - Executes `consume` behavior.
- `createSet(String name, @Nonnull BlockSetLookupTable lookupTable, @Nonnull Int2ObjectMap<IntSet> flattenedSets)`: Add description.
  - Executes `createSet` behavior.
- `consumeCategory(@Nullable String[] categories, @Nonnull Consumer<IntSet> predicate, @Nonnull BlockSetLookupTable lookupTable)`: Add description.
  - Executes `consumeCategory` behavior.
- `consumeEntry(@Nonnull String name, @Nonnull Consumer<IntSet> predicate, @Nonnull Map<String, IntSet> nameIdMap, String typeString)`: Add description.
  - Executes `consumeEntry` behavior.
- `getBlockSets()`: Add description.
  - Executes `getBlockSets` behavior.
- `blockInSet(int set, int blockId)`: Add description.
  - Executes `blockInSet` behavior.
- `blockInSet(int set, @Nullable BlockType blockType)`: Add description.
  - Executes `blockInSet` behavior.
- `blockInSet(int set, @Nullable String blockTypeKey)`: Add description.
  - Executes `blockInSet` behavior.
- `getInstance()`: Add description.
  - Executes `getInstance` behavior.

## Notes
- No additional notes.
