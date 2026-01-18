# StringTreeMap

## Overview
- Documentation for `StringTreeMap`.
- Declared as a class in `com.hypixel.hytale.codec.builder`.

## Constructors
- `StringTreeMap()`
  - Creates a `StringTreeMap` instance.
- `StringTreeMap(@Nonnull StringTreeMap<V> parent)`
  - Creates a `StringTreeMap` instance.
- `StringTreeMap(@Nonnull Map<String, V> entries)`
  - Creates a `StringTreeMap` instance.

## Methods
- `getKey()`
  - Executes `getKey` behavior.
- `getValue()`
  - Executes `getValue` behavior.
- `putAll(@Nonnull Map<String, V> entries)`
  - Executes `putAll` behavior.
- `put(@Nonnull String key, V values)`
  - Executes `put` behavior.
- `put0(@Nonnull String key, V fields, int start, int end)`
  - Executes `put0` behavior.
- `remove(@Nonnull String key)`
  - Executes `remove` behavior.
- `remove0(@Nonnull String key, int start, int end)`
  - Executes `remove0` behavior.
- `findEntry(@Nonnull RawJsonReader reader)`
  - Executes `findEntry` behavior.
- `findEntryOrDefault(@Nonnull RawJsonReader reader, StringTreeMap<V> def)`
  - Executes `findEntryOrDefault` behavior.
- `findEntry0(@Nonnull RawJsonReader reader, StringTreeMap<V> def, int end)`
  - Executes `findEntry0` behavior.
- `consumeEntryKey(@Nonnull RawJsonReader reader, StringTreeMap<V> def, int end, @Nonnull StringTreeMap<V> entry)`
  - Executes `consumeEntryKey` behavior.
- `toString()`
  - Executes `toString` behavior.
- `readStringPartAsLong(@Nonnull String key, int start, int end)`
  - Executes `readStringPartAsLong` behavior.

## Notes
- No additional notes.
