# BlockSetModule

## Overview
- Documentation for `BlockSetModule`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.blockset`.

## Constructors
- `BlockSetModule(@Nonnull JavaPluginInit module)`
  - Creates a `BlockSetModule` instance.

## Methods
- `setup()`
  - Executes `setup` behavior.
- `onBlockTypesChanged(@Nonnull LoadedAssetsEvent<String, BlockType, BlockTypeAssetMap<String, BlockType>> event)`
  - Executes `onBlockTypesChanged` behavior.
- `onBlockSetsChanged(LoadedAssetsEvent<String, BlockSet, DefaultAssetMap<String, BlockSet>> event)`
  - Executes `onBlockSetsChanged` behavior.
- `flattenBlockSets(@Nonnull BlockSetLookupTable lookupTable)`
  - Executes `flattenBlockSets` behavior.
- `createSet(@Nonnull BlockSet blockSet, @Nonnull BlockSetLookupTable lookupTable, @Nonnull Int2ObjectMap<IntSet> flattenedSets)`
  - Executes `createSet` behavior.
- `consume(@Nullable String[] values, @Nonnull Map<String, IntSet> map, String typeString, @Nonnull Consumer<IntSet> addAll)`
  - Executes `consume` behavior.
- `consume(@Nullable String[][] values, @Nonnull BlockSetLookupTable lookupTable, @Nonnull Consumer<IntSet> addAll)`
  - Executes `consume` behavior.
- `createSet(String name, @Nonnull BlockSetLookupTable lookupTable, @Nonnull Int2ObjectMap<IntSet> flattenedSets)`
  - Executes `createSet` behavior.
- `consumeCategory(@Nullable String[] categories, @Nonnull Consumer<IntSet> predicate, @Nonnull BlockSetLookupTable lookupTable)`
  - Executes `consumeCategory` behavior.
- `consumeEntry(@Nonnull String name, @Nonnull Consumer<IntSet> predicate, @Nonnull Map<String, IntSet> nameIdMap, String typeString)`
  - Executes `consumeEntry` behavior.
- `getBlockSets()`
  - Executes `getBlockSets` behavior.
- `blockInSet(int set, int blockId)`
  - Executes `blockInSet` behavior.
- `blockInSet(int set, @Nullable BlockType blockType)`
  - Executes `blockInSet` behavior.
- `blockInSet(int set, @Nullable String blockTypeKey)`
  - Executes `blockInSet` behavior.
- `getInstance()`
  - Executes `getInstance` behavior.

## Notes
- No additional notes.
