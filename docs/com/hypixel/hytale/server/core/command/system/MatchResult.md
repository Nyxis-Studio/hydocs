# MatchResult

## Overview
- Documentation for `MatchResult`.
- Declared as a class in `com.hypixel.hytale.server.core.command.system`.

## Constructors
- `MatchResult(Integer.MIN_VALUE, Integer.MIN_VALUE, Integer.MIN_VALUE, Integer.MIN_VALUE)`
  - Creates a `MatchResult` instance.
- `MatchResult(Integer.MAX_VALUE, Integer.MAX_VALUE, Integer.MAX_VALUE, Integer.MAX_VALUE)`
  - Creates a `MatchResult` instance.
- `MatchResult(termDepth, depth, type, StringCompareUtil.getLevenshteinDistance(text, search)`
  - Creates a `MatchResult` instance.
- `MatchResult(int term, int depth, int type, int match)`
  - Creates a `MatchResult` instance.

## Methods
- `of(int termDepth, int depth, int type, @Nonnull String text, @Nonnull String search)`
  - Executes `of` behavior.
- `getDepth()`
  - Executes `getDepth` behavior.
- `getType()`
  - Executes `getType` behavior.
- `getMatch()`
  - Executes `getMatch` behavior.
- `min(@Nonnull MatchResult other)`
  - Executes `min` behavior.
- `compareTo(@Nonnull MatchResult o)`
  - Executes `compareTo` behavior.
- `equals(@Nullable Object o)`
  - Executes `equals` behavior.
- `hashCode()`
  - Executes `hashCode` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
