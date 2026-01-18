# VersionedExtraInfo

## Overview
- Documentation for `VersionedExtraInfo`.
- Declared as a class in `com.hypixel.hytale.codec`.

## Constructors
- `VersionedExtraInfo(int version, ExtraInfo delegate)`
  - Creates a `VersionedExtraInfo` instance.

## Methods
- `getVersion()`
  - Executes `getVersion` behavior.
- `getKeysSize()`
  - Executes `getKeysSize` behavior.
- `getCodecStore()`
  - Executes `getCodecStore` behavior.
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
- `getUnknownKeys()`
  - Executes `getUnknownKeys` behavior.
- `getValidationResults()`
  - Executes `getValidationResults` behavior.
- `getMetadata()`
  - Executes `getMetadata` behavior.
- `appendDetailsTo(@Nonnull StringBuilder sb)`
  - Executes `appendDetailsTo` behavior.
- `getLegacyVersion()`
  - Executes `getLegacyVersion` behavior.

## Notes
- No additional notes.
