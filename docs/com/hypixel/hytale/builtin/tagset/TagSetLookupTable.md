# TagSetLookupTable

## Overview
- Documentation for `TagSetLookupTable`.
- Declared as a class in `com.hypixel.hytale.builtin.tagset`.

## Constructors
- `TagSetLookupTable(@Nonnull Map<String, T> tagSetMap, @Nonnull Object2IntMap<String> tagSetIndexMap, @Nonnull Object2IntMap<String> tagIndexMap)`
  - Creates a `TagSetLookupTable` instance.

## Methods
- `createTagMap(@Nonnull Map<String, T> tagSetMap, @Nonnull Object2IntMap<String> tagSetIndexMap, @Nonnull Object2IntMap<String> tagIndexMap)`
  - Executes `createTagMap` behavior.
- `createTagSet(@Nonnull T tagSet, @Nonnull Map<String, T> tagSetMap, @Nonnull Object2IntMap<String> tagSetIndexMap, @Nonnull Object2IntMap<String> tagIndexMap, @Nonnull IntArrayList path)`
  - Executes `createTagSet` behavior.
- `consumeSet(String tag, @Nonnull Map<String, T> tagSetMap, @Nonnull Object2IntMap<String> tagSetIndexMap, @Nonnull Object2IntMap<String> tagIndexMap, @Nonnull IntArrayList path, @Nonnull Consumer<IntSet> predicate)`
  - Executes `consumeSet` behavior.
- `consumeTag(@Nonnull String tag, @Nonnull T tagSet, @Nonnull Object2IntMap<String> tagIndexMap, @Nonnull IntConsumer predicate)`
  - Executes `consumeTag` behavior.
- `getOrCreateTagSet(String identifier, @Nonnull Map<String, T> tagSetMap, @Nonnull Object2IntMap<String> tagSetIndexMap, @Nonnull Object2IntMap<String> tagIndexMap, @Nonnull IntArrayList path)`
  - Executes `getOrCreateTagSet` behavior.
- `getFlattenedSet()`
  - Executes `getFlattenedSet` behavior.

## Notes
- No additional notes.
