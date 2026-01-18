**Source Hash:** `92b7fa6096f13de9fbb1e34aacfa169decd52f2bd50e5ed66f27aab58d27b950`

# TagSetLookupTable

## Overview

## Constructor Descriptions
- `TagSetLookupTable(@Nonnull Map<String, T> tagSetMap, @Nonnull Object2IntMap<String> tagSetIndexMap, @Nonnull Object2IntMap<String> tagIndexMap)`
  - Creates a `TagSetLookupTable` instance.

## Method Descriptions
- `createTagMap(@Nonnull Map<String, T> tagSetMap, @Nonnull Object2IntMap<String> tagSetIndexMap, @Nonnull Object2IntMap<String> tagIndexMap)`: Add description.
  - Executes `createTagMap` behavior.
- `createTagSet(@Nonnull T tagSet, @Nonnull Map<String, T> tagSetMap, @Nonnull Object2IntMap<String> tagSetIndexMap, @Nonnull Object2IntMap<String> tagIndexMap, @Nonnull IntArrayList path)`: Add description.
  - Executes `createTagSet` behavior.
- `consumeSet(String tag, @Nonnull Map<String, T> tagSetMap, @Nonnull Object2IntMap<String> tagSetIndexMap, @Nonnull Object2IntMap<String> tagIndexMap, @Nonnull IntArrayList path, @Nonnull Consumer<IntSet> predicate)`: Add description.
  - Executes `consumeSet` behavior.
- `consumeTag(@Nonnull String tag, @Nonnull T tagSet, @Nonnull Object2IntMap<String> tagIndexMap, @Nonnull IntConsumer predicate)`: Add description.
  - Executes `consumeTag` behavior.
- `getOrCreateTagSet(String identifier, @Nonnull Map<String, T> tagSetMap, @Nonnull Object2IntMap<String> tagSetIndexMap, @Nonnull Object2IntMap<String> tagIndexMap, @Nonnull IntArrayList path)`: Add description.
  - Executes `getOrCreateTagSet` behavior.
- `getFlattenedSet()`: Add description.
  - Executes `getFlattenedSet` behavior.

## Notes
- No additional notes.
