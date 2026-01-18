# ExtraInfo

## Overview
- Documentation for `ExtraInfo`.
- Declared as a class in `com.hypixel.hytale.codec`.

## Constructors
- `ExtraInfo()`
  - Creates a `ExtraInfo` instance.
- `ExtraInfo(int version)`
  - Creates a `ExtraInfo` instance.
- `ExtraInfo(int version, @Nonnull Function<ExtraInfo, ValidationResults> validationResultsSupplier)`
  - Creates a `ExtraInfo` instance.

## Methods
- `getVersion()`
  - Executes `getVersion` behavior.
- `getLegacyVersion()`
  - Executes `getLegacyVersion` behavior.
- `getKeysSize()`
  - Executes `getKeysSize` behavior.
- `getCodecStore()`
  - Executes `getCodecStore` behavior.
- `nextKeyIndex()`
  - Executes `nextKeyIndex` behavior.
- `pushKey(String key)`
  - Executes `pushKey` behavior.
- `pushIntKey(int key)`
  - Executes `pushIntKey` behavior.
- `pushKey(String key, RawJsonReader reader)`
  - Executes `pushKey` behavior.
- `pushIntKey(int key, RawJsonReader reader)`
  - Executes `pushIntKey` behavior.
- `popKey()`
  - Executes `popKey` behavior.
- `nextIgnoredUnknownIndex()`
  - Executes `nextIgnoredUnknownIndex` behavior.
- `ignoreUnusedKey(String key)`
  - Executes `ignoreUnusedKey` behavior.
- `popIgnoredUnusedKey()`
  - Executes `popIgnoredUnusedKey` behavior.
- `consumeIgnoredUnknownKey(@Nonnull RawJsonReader reader)`
  - Executes `consumeIgnoredUnknownKey` behavior.
- `consumeIgnoredUnknownKey(@Nonnull String key)`
  - Executes `consumeIgnoredUnknownKey` behavior.
- `readUnknownKey(@Nonnull RawJsonReader reader)`
  - Executes `readUnknownKey` behavior.
- `addUnknownKey(@Nonnull String key)`
  - Executes `addUnknownKey` behavior.
- `peekKey()`
  - Executes `peekKey` behavior.
- `peekKey(char separator)`
  - Executes `peekKey` behavior.
- `peekLine()`
  - Executes `peekLine` behavior.
- `peekColumn()`
  - Executes `peekColumn` behavior.
- `getUnknownKeys()`
  - Executes `getUnknownKeys` behavior.
- `getValidationResults()`
  - Executes `getValidationResults` behavior.
- `getMetadata()`
  - Executes `getMetadata` behavior.
- `appendDetailsTo(@Nonnull StringBuilder sb)`
  - Executes `appendDetailsTo` behavior.
- `toString()`
  - Executes `toString` behavior.
- `grow(int oldSize)`
  - Executes `grow` behavior.

## Notes
- No additional notes.
