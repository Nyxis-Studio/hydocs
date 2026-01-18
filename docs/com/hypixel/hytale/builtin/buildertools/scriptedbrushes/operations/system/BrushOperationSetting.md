# BrushOperationSetting

## Overview
- Documentation for `BrushOperationSetting`.
- Declared as a class in `com.hypixel.hytale.builtin.buildertools.scriptedbrushes.operations.system`.

## Constructors
- `BrushOperationSetting(String name, String description, T defaultValue, ArgumentType<T> argumentType)`
  - Creates a `BrushOperationSetting` instance.
- `BrushOperationSetting(String name, String description, T defaultValue, ArgumentType<T> argumentType, Function<BrushOperationSetting<T>, String> toStringFunction)`
  - Creates a `BrushOperationSetting` instance.
- `BrushOperationSetting(String name, String description, T defaultValue, ArgumentType<T> argumentType, @Nullable Validator<T> valueValidator, @Nullable Function<BrushOperationSetting<T>, String> toStringFunction)`
  - Creates a `BrushOperationSetting` instance.

## Methods
- `setValue(T value)`
  - Executes `setValue` behavior.
- `setValueUnsafe(String input, Object value)`
  - Executes `setValueUnsafe` behavior.
- `parseAndSetValue(String[] input)`
  - Executes `parseAndSetValue` behavior.
- `getInput()`
  - Executes `getInput` behavior.
- `getName()`
  - Executes `getName` behavior.
- `getDescription()`
  - Executes `getDescription` behavior.
- `getDefaultValue()`
  - Executes `getDefaultValue` behavior.
- `getArgumentType()`
  - Executes `getArgumentType` behavior.
- `getValueValidator()`
  - Executes `getValueValidator` behavior.
- `getValue()`
  - Executes `getValue` behavior.
- `getValueString()`
  - Executes `getValueString` behavior.

## Notes
- No additional notes.
