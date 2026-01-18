**Source Hash:** `f172c3b3638333f96dc5da6632eb96ec086f1327a70d96b254419959648a335d`

# BrushConfigCommandExecutor

## Overview

## Constructor Descriptions
- `BrushConfigCommandExecutor(BrushConfig brushConfig)`
  - Creates a `BrushConfigCommandExecutor` instance.

## Method Descriptions
- `resetInternalState()`: Add description.
  - Executes `resetInternalState` behavior.
- `execute(@Nonnull Ref<EntityStore> ref, @Nonnull World world, @Nonnull Vector3i origin, boolean isHoldDownInteraction, @Nonnull InteractionType interactionType, @Nullable Consumer<BrushConfig> existingBrushDataLoadingConsumer, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `execute` behavior.
- `execute(@Nonnull Ref<EntityStore> ref, World world, Vector3i origin, boolean isHoldDownInteraction, InteractionType interactionType, ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `execute` behavior.
- `exitExecution(Ref<EntityStore> ref, ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `exitExecution` behavior.
- `sendExecutionErrorMessage(PlayerRef playerRef, @Nonnull SequenceBrushOperation brushOperation)`: Add description.
  - Executes `sendExecutionErrorMessage` behavior.
- `storeOperatingIndex(String name, int index)`: Add description.
  - Executes `storeOperatingIndex` behavior.
- `loadOperatingIndex(String name)`: Add description.
  - Executes `loadOperatingIndex` behavior.
- `loadOperatingIndex(String name, boolean allowFutureJump)`: Add description.
  - Executes `loadOperatingIndex` behavior.
- `clearAllPersistentVariables()`: Add description.
  - Executes `clearAllPersistentVariables` behavior.
- `clearPersistentVariable(String variableName)`: Add description.
  - Executes `clearPersistentVariable` behavior.
- `setPersistentVariable(String variableName, int value)`: Add description.
  - Executes `setPersistentVariable` behavior.
- `getPersistentVariableOrDefault(String variableName, int defaultValue)`: Add description.
  - Executes `getPersistentVariableOrDefault` behavior.
- `storeBrushConfigSnapshot(@Nonnull String name)`: Add description.
  - Executes `storeBrushConfigSnapshot` behavior.
- `loadBrushConfigSnapshot(String name, BrushConfig.DataSettingFlags ... dataToLoad)`: Add description.
  - Executes `loadBrushConfigSnapshot` behavior.
- `setAllowOverwritingSavedSnapshots(boolean allowOverwritingSavedSnapshots)`: Add description.
  - Executes `setAllowOverwritingSavedSnapshots` behavior.
- `getSequentialOperations()`: Add description.
  - Executes `getSequentialOperations` behavior.
- `getGlobalOperations()`: Add description.
  - Executes `getGlobalOperations` behavior.
- `isIgnoreExistingBrushData()`: Add description.
  - Executes `isIgnoreExistingBrushData` behavior.
- `isInDebugSteppingMode()`: Add description.
  - Executes `isInDebugSteppingMode` behavior.
- `getEdit()`: Add description.
  - Executes `getEdit` behavior.
- `setInDebugSteppingMode(boolean inDebugSteppingMode)`: Add description.
  - Executes `setInDebugSteppingMode` behavior.
- `setPrintOperations(boolean printOperations)`: Add description.
  - Executes `setPrintOperations` behavior.
- `setIgnoreExistingBrushData(boolean ignoreExistingBrushData)`: Add description.
  - Executes `setIgnoreExistingBrushData` behavior.
- `setCurrentlyExecutingActionIndex(int newCurrentOperationIndex)`: Add description.
  - Executes `setCurrentlyExecutingActionIndex` behavior.
- `getCurrentOperationIndex()`: Add description.
  - Executes `getCurrentOperationIndex` behavior.
- `isEnableBreakpoints()`: Add description.
  - Executes `isEnableBreakpoints` behavior.
- `setEnableBreakpoints(boolean enableBreakpoints)`: Add description.
  - Executes `setEnableBreakpoints` behavior.
- `getDebugOutputTarget()`: Add description.
  - Executes `getDebugOutputTarget` behavior.
- `setDebugOutputTarget(DebugOutputTarget debugOutputTarget)`: Add description.
  - Executes `setDebugOutputTarget` behavior.
- `isBreakOnError()`: Add description.
  - Executes `isBreakOnError` behavior.
- `setBreakOnError(boolean breakOnError)`: Add description.
  - Executes `setBreakOnError` behavior.

## Notes
- No additional notes.
