# BrushConfigCommandExecutor

## Overview
- Documentation for `BrushConfigCommandExecutor`.
- Declared as a class in `com.hypixel.hytale.builtin.buildertools.scriptedbrushes`.

## Constructors
- `BrushConfigCommandExecutor(BrushConfig brushConfig)`
  - Creates a `BrushConfigCommandExecutor` instance.

## Methods
- `resetInternalState()`
  - Executes `resetInternalState` behavior.
- `execute(@Nonnull Ref<EntityStore> ref, @Nonnull World world, @Nonnull Vector3i origin, boolean isHoldDownInteraction, @Nonnull InteractionType interactionType, @Nullable Consumer<BrushConfig> existingBrushDataLoadingConsumer, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `execute` behavior.
- `execute(@Nonnull Ref<EntityStore> ref, World world, Vector3i origin, boolean isHoldDownInteraction, InteractionType interactionType, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `execute` behavior.
- `exitExecution(Ref<EntityStore> ref, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `exitExecution` behavior.
- `sendExecutionErrorMessage(PlayerRef playerRef, @Nonnull SequenceBrushOperation brushOperation)`
  - Executes `sendExecutionErrorMessage` behavior.
- `storeOperatingIndex(String name, int index)`
  - Executes `storeOperatingIndex` behavior.
- `loadOperatingIndex(String name)`
  - Executes `loadOperatingIndex` behavior.
- `loadOperatingIndex(String name, boolean allowFutureJump)`
  - Executes `loadOperatingIndex` behavior.
- `clearAllPersistentVariables()`
  - Executes `clearAllPersistentVariables` behavior.
- `clearPersistentVariable(String variableName)`
  - Executes `clearPersistentVariable` behavior.
- `setPersistentVariable(String variableName, int value)`
  - Executes `setPersistentVariable` behavior.
- `getPersistentVariableOrDefault(String variableName, int defaultValue)`
  - Executes `getPersistentVariableOrDefault` behavior.
- `storeBrushConfigSnapshot(@Nonnull String name)`
  - Executes `storeBrushConfigSnapshot` behavior.
- `loadBrushConfigSnapshot(String name, BrushConfig.DataSettingFlags ... dataToLoad)`
  - Executes `loadBrushConfigSnapshot` behavior.
- `setAllowOverwritingSavedSnapshots(boolean allowOverwritingSavedSnapshots)`
  - Executes `setAllowOverwritingSavedSnapshots` behavior.
- `getSequentialOperations()`
  - Executes `getSequentialOperations` behavior.
- `getGlobalOperations()`
  - Executes `getGlobalOperations` behavior.
- `isIgnoreExistingBrushData()`
  - Executes `isIgnoreExistingBrushData` behavior.
- `isInDebugSteppingMode()`
  - Executes `isInDebugSteppingMode` behavior.
- `getEdit()`
  - Executes `getEdit` behavior.
- `setInDebugSteppingMode(boolean inDebugSteppingMode)`
  - Executes `setInDebugSteppingMode` behavior.
- `setPrintOperations(boolean printOperations)`
  - Executes `setPrintOperations` behavior.
- `setIgnoreExistingBrushData(boolean ignoreExistingBrushData)`
  - Executes `setIgnoreExistingBrushData` behavior.
- `setCurrentlyExecutingActionIndex(int newCurrentOperationIndex)`
  - Executes `setCurrentlyExecutingActionIndex` behavior.
- `getCurrentOperationIndex()`
  - Executes `getCurrentOperationIndex` behavior.
- `isEnableBreakpoints()`
  - Executes `isEnableBreakpoints` behavior.
- `setEnableBreakpoints(boolean enableBreakpoints)`
  - Executes `setEnableBreakpoints` behavior.
- `getDebugOutputTarget()`
  - Executes `getDebugOutputTarget` behavior.
- `setDebugOutputTarget(DebugOutputTarget debugOutputTarget)`
  - Executes `setDebugOutputTarget` behavior.
- `isBreakOnError()`
  - Executes `isBreakOnError` behavior.
- `setBreakOnError(boolean breakOnError)`
  - Executes `setBreakOnError` behavior.

## Notes
- No additional notes.
