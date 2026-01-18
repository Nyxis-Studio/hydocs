**Source Hash:** `1e3d6a80619be33addb8299075e51d1551f8106a4657a9cec0d3110917981a78`

# BrushOperationSetting

## Overview

## Constructor Descriptions
- `BrushOperationSetting(String name, String description, T defaultValue, ArgumentType<T> argumentType)`
  - Creates a `BrushOperationSetting` instance.
- `BrushOperationSetting(String name, String description, T defaultValue, ArgumentType<T> argumentType, Function<BrushOperationSetting<T>, String> toStringFunction)`
  - Creates a `BrushOperationSetting` instance.
- `BrushOperationSetting(String name, String description, T defaultValue, ArgumentType<T> argumentType, @Nullable Validator<T> valueValidator, @Nullable Function<BrushOperationSetting<T>, String> toStringFunction)`
  - Creates a `BrushOperationSetting` instance.

## Method Descriptions
- `setValue(T value)`: Add description.
  - Executes `setValue` behavior.
- `setValueUnsafe(String input, Object value)`: Add description.
  - Executes `setValueUnsafe` behavior.
- `parseAndSetValue(String[] input)`: Add description.
  - Executes `parseAndSetValue` behavior.
- `getInput()`: Add description.
  - Executes `getInput` behavior.
- `getName()`: Add description.
  - Executes `getName` behavior.
- `getDescription()`: Add description.
  - Executes `getDescription` behavior.
- `getDefaultValue()`: Add description.
  - Executes `getDefaultValue` behavior.
- `getArgumentType()`: Add description.
  - Executes `getArgumentType` behavior.
- `getValueValidator()`: Add description.
  - Executes `getValueValidator` behavior.
- `getValue()`: Add description.
  - Executes `getValue` behavior.
- `getValueString()`: Add description.
  - Executes `getValueString` behavior.

## Notes
- No additional notes.
