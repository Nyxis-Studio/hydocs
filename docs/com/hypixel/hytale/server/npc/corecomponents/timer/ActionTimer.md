# ActionTimer

## Overview
- Documentation for `ActionTimer`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents.timer`.

## Constructors
- `ActionTimer(@Nonnull BuilderActionTimer builderActionTimer, @Nonnull BuilderSupport builderSupport)`
  - Creates a `ActionTimer` instance.
- `ActionTimer(@Nonnull BuilderActionTimerStart builderActionTimerStart, @Nonnull BuilderSupport builderSupport)`
  - Creates a `ActionTimer` instance.
- `ActionTimer(@Nonnull BuilderActionTimerModify builderActionTimerModify, @Nonnull BuilderSupport builderSupport)`
  - Creates a `ActionTimer` instance.
- `ActionTimer(BuilderActionTimerPause builderActionTimerPause, @Nonnull BuilderSupport builderSupport)`
  - Creates a `ActionTimer` instance.
- `ActionTimer(BuilderActionTimerStop builderActionTimerStop, @Nonnull BuilderSupport builderSupport)`
  - Creates a `ActionTimer` instance.
- `ActionTimer(BuilderActionTimerContinue builderActionTimerContinue, @Nonnull BuilderSupport builderSupport)`
  - Creates a `ActionTimer` instance.
- `ActionTimer(BuilderActionTimerRestart builderActionTimerRestart, @Nonnull BuilderSupport builderSupport)`
  - Creates a `ActionTimer` instance.

## Methods
- `execute(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, InfoProvider sensorInfo, double dt, @Nonnull Store<EntityStore> store)`
  - Executes `execute` behavior.
- `executeRestartAction()`
  - Executes `executeRestartAction` behavior.
- `executeModifyAction()`
  - Executes `executeModifyAction` behavior.
- `executeContinueAction()`
  - Executes `executeContinueAction` behavior.
- `executePauseAction()`
  - Executes `executePauseAction` behavior.
- `executeStopAction()`
  - Executes `executeStopAction` behavior.
- `executeStartAction()`
  - Executes `executeStartAction` behavior.

## Notes
- No additional notes.
