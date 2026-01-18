# StringUtil

## Overview
- Documentation for `StringUtil`.
- Declared as a class in `com.hypixel.hytale.common.util`.

## Constructors
- None.

## Methods
- `isNumericString(@Nonnull String str)`
  - Executes `isNumericString` behavior.
- `isAlphaNumericHyphenString(@Nonnull String str)`
  - Executes `isAlphaNumericHyphenString` behavior.
- `isAlphaNumericHyphenUnderscoreString(@Nonnull String str)`
  - Executes `isAlphaNumericHyphenUnderscoreString` behavior.
- `isCapitalized(@Nonnull String keyStr, char delim)`
  - Executes `isCapitalized` behavior.
- `capitalize(@Nonnull String keyStr, char delim)`
  - Executes `capitalize` behavior.
- `parseEnum(@Nonnull V[] enumConstants, String str)`
  - Executes `parseEnum` behavior.
- `parseEnum(@Nonnull V[] enumConstants, String str, MatchType matchType)`
  - Executes `parseEnum` behavior.
- `parseArgs(String rawString, @Nonnull Map<String, String> argOptions)`
  - Executes `parseArgs` behavior.
- `parseArgs(String rawString)`
  - Executes `parseArgs` behavior.
- `removeQuotes(@Nonnull String value)`
  - Executes `removeQuotes` behavior.
- `stripQuotes(@Nonnull String s)`
  - Executes `stripQuotes` behavior.
- `isGlobMatching(@Nonnull String pattern, @Nonnull String text)`
  - Executes `isGlobMatching` behavior.
- `isGlobMatching(@Nonnull String pattern, int patternPos, @Nonnull String text, int textPos)`
  - Executes `isGlobMatching` behavior.
- `isGlobPattern(@Nonnull String text)`
  - Executes `isGlobPattern` behavior.
- `humanizeTime(@Nonnull Duration duration, boolean useSeconds)`
  - Executes `humanizeTime` behavior.
- `humanizeTime(@Nonnull Duration length)`
  - Executes `humanizeTime` behavior.
- `sortByFuzzyDistance(@Nonnull String str, @Nonnull Collection<T> collection, int length)`
  - Executes `sortByFuzzyDistance` behavior.
- `sortByFuzzyDistance(@Nonnull String str, @Nonnull Collection<T> collection)`
  - Executes `sortByFuzzyDistance` behavior.
- `toPaddedBinaryString(int val)`
  - Executes `toPaddedBinaryString` behavior.
- `trimEnd(@Nonnull String str, @Nonnull String end)`
  - Executes `trimEnd` behavior.
- `generateGraph(@Nonnull StringBuilder sb, int width, int height, long minX, long maxX, double minY, double maxY, @Nonnull DoubleFunction<String> labelFormatFunc, int historyLength, @Nonnull IntToLongFunction timestampFunc, @Nonnull IntToDoubleFunction valueFunc)`
  - Executes `generateGraph` behavior.

## Notes
- No additional notes.
