**Source Hash:** `339fe660e5b0918f7b9c7350718dcb75e1c10d37909045d920d42a1fedbe5b1f`

# ProtocolException

## Overview

## Constructor Descriptions
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

## Method Descriptions
- `arrayTooLong(@Nonnull String fieldName, int actual, int max)`: Add description.
  - Executes `arrayTooLong` behavior.
- `stringTooLong(@Nonnull String fieldName, int actual, int max)`: Add description.
  - Executes `stringTooLong` behavior.
- `dictionaryTooLarge(@Nonnull String fieldName, int actual, int max)`: Add description.
  - Executes `dictionaryTooLarge` behavior.
- `bufferTooSmall(@Nonnull String fieldName, int required, int available)`: Add description.
  - Executes `bufferTooSmall` behavior.
- `invalidVarInt(@Nonnull String fieldName)`: Add description.
  - Executes `invalidVarInt` behavior.
- `negativeLength(@Nonnull String fieldName, int value)`: Add description.
  - Executes `negativeLength` behavior.
- `invalidOffset(@Nonnull String fieldName, int offset, int bufferLength)`: Add description.
  - Executes `invalidOffset` behavior.
- `unknownPolymorphicType(@Nonnull String typeName, int typeId)`: Add description.
  - Executes `unknownPolymorphicType` behavior.
- `duplicateKey(@Nonnull String fieldName, @Nonnull Object key)`: Add description.
  - Executes `duplicateKey` behavior.
- `invalidEnumValue(@Nonnull String enumName, int value)`: Add description.
  - Executes `invalidEnumValue` behavior.
- `arrayTooShort(@Nonnull String fieldName, int actual, int min)`: Add description.
  - Executes `arrayTooShort` behavior.
- `stringTooShort(@Nonnull String fieldName, int actual, int min)`: Add description.
  - Executes `stringTooShort` behavior.
- `dictionaryTooSmall(@Nonnull String fieldName, int actual, int min)`: Add description.
  - Executes `dictionaryTooSmall` behavior.
- `valueOutOfRange(@Nonnull String fieldName, @Nonnull Object value, double min, double max)`: Add description.
  - Executes `valueOutOfRange` behavior.
- `valueBelowMinimum(@Nonnull String fieldName, @Nonnull Object value, double min)`: Add description.
  - Executes `valueBelowMinimum` behavior.
- `valueAboveMaximum(@Nonnull String fieldName, @Nonnull Object value, double max)`: Add description.
  - Executes `valueAboveMaximum` behavior.

## Notes
- No additional notes.
