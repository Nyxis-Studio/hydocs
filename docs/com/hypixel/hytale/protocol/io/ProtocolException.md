# ProtocolException

## Overview
- Documentation for `ProtocolException`.
- Declared as a class in `com.hypixel.hytale.protocol.io`.

## Constructors
- `ProtocolException(@Nonnull String message)`
  - Creates a `ProtocolException` instance.
- `ProtocolException(@Nonnull String message, @Nonnull Throwable cause)`
  - Creates a `ProtocolException` instance.
- `ProtocolException(fieldName + ": array length " + actual + " exceeds maximum " + max)`
  - Creates a `ProtocolException` instance.
- `ProtocolException(fieldName + ": string length " + actual + " exceeds maximum " + max)`
  - Creates a `ProtocolException` instance.
- `ProtocolException(fieldName + ": dictionary count " + actual + " exceeds maximum " + max)`
  - Creates a `ProtocolException` instance.
- `ProtocolException(fieldName + ": buffer too small, need " + required + " bytes but only " + available + " available")`
  - Creates a `ProtocolException` instance.
- `ProtocolException(fieldName + ": invalid or incomplete VarInt")`
  - Creates a `ProtocolException` instance.
- `ProtocolException(fieldName + ": negative length " + value)`
  - Creates a `ProtocolException` instance.
- `ProtocolException(fieldName + ": offset " + offset + " is out of bounds (buffer length: " + bufferLength + ")`
  - Creates a `ProtocolException` instance.
- `ProtocolException(typeName + ": unknown polymorphic type ID " + typeId)`
  - Creates a `ProtocolException` instance.
- `ProtocolException(fieldName + ": duplicate key '" + String.valueOf(key)`
  - Creates a `ProtocolException` instance.
- `ProtocolException(enumName + ": invalid enum value " + value)`
  - Creates a `ProtocolException` instance.
- `ProtocolException(fieldName + ": array length " + actual + " is below minimum " + min)`
  - Creates a `ProtocolException` instance.
- `ProtocolException(fieldName + ": string length " + actual + " is below minimum " + min)`
  - Creates a `ProtocolException` instance.
- `ProtocolException(fieldName + ": dictionary count " + actual + " is below minimum " + min)`
  - Creates a `ProtocolException` instance.
- `ProtocolException(fieldName + ": value " + String.valueOf(value)`
  - Creates a `ProtocolException` instance.

## Methods
- `arrayTooLong(@Nonnull String fieldName, int actual, int max)`
  - Executes `arrayTooLong` behavior.
- `stringTooLong(@Nonnull String fieldName, int actual, int max)`
  - Executes `stringTooLong` behavior.
- `dictionaryTooLarge(@Nonnull String fieldName, int actual, int max)`
  - Executes `dictionaryTooLarge` behavior.
- `bufferTooSmall(@Nonnull String fieldName, int required, int available)`
  - Executes `bufferTooSmall` behavior.
- `invalidVarInt(@Nonnull String fieldName)`
  - Executes `invalidVarInt` behavior.
- `negativeLength(@Nonnull String fieldName, int value)`
  - Executes `negativeLength` behavior.
- `invalidOffset(@Nonnull String fieldName, int offset, int bufferLength)`
  - Executes `invalidOffset` behavior.
- `unknownPolymorphicType(@Nonnull String typeName, int typeId)`
  - Executes `unknownPolymorphicType` behavior.
- `duplicateKey(@Nonnull String fieldName, @Nonnull Object key)`
  - Executes `duplicateKey` behavior.
- `invalidEnumValue(@Nonnull String enumName, int value)`
  - Executes `invalidEnumValue` behavior.
- `arrayTooShort(@Nonnull String fieldName, int actual, int min)`
  - Executes `arrayTooShort` behavior.
- `stringTooShort(@Nonnull String fieldName, int actual, int min)`
  - Executes `stringTooShort` behavior.
- `dictionaryTooSmall(@Nonnull String fieldName, int actual, int min)`
  - Executes `dictionaryTooSmall` behavior.
- `valueOutOfRange(@Nonnull String fieldName, @Nonnull Object value, double min, double max)`
  - Executes `valueOutOfRange` behavior.
- `valueBelowMinimum(@Nonnull String fieldName, @Nonnull Object value, double min)`
  - Executes `valueBelowMinimum` behavior.
- `valueAboveMaximum(@Nonnull String fieldName, @Nonnull Object value, double max)`
  - Executes `valueAboveMaximum` behavior.

## Notes
- No additional notes.
