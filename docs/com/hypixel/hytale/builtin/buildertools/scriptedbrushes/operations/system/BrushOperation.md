# BrushOperation

## Overview
- Documentation for `BrushOperation`.
- Declared as a class in `com.hypixel.hytale.builtin.buildertools.scriptedbrushes.operations.system`.

## Constructors
- `BrushOperation(String name, String description)`
  - Creates a `BrushOperation` instance.

## Methods
- `modifyBrushConfig(@Nonnull Ref<EntityStore> var1, @Nonnull BrushConfig var2, @Nonnull BrushConfigCommandExecutor var3, @Nonnull ComponentAccessor<EntityStore> var4)`
  - Executes `modifyBrushConfig` behavior.
- `resetInternalState()`
  - Executes `resetInternalState` behavior.
- `preExecutionModifyBrushConfig(BrushConfigCommandExecutor brushConfigCommandExecutor, int operationIndex)`
  - Executes `preExecutionModifyBrushConfig` behavior.
- `createBrushSetting(@Nonnull String name, String description, T defaultValue, ArgumentType<T> argumentType)`
  - Executes `createBrushSetting` behavior.
- `createBrushSetting(@Nonnull String name, String description, T defaultValue, ArgumentType<T> argumentType, Function<BrushOperationSetting<T>, String> toStringFunction)`
  - Executes `createBrushSetting` behavior.
- `getName()`
  - Executes `getName` behavior.
- `getDescription()`
  - Executes `getDescription` behavior.

## Notes
- No additional notes.
