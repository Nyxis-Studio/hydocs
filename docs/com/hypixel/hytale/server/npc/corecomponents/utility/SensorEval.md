# SensorEval

## Overview
- Documentation for `SensorEval`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents.utility`.

## Constructors
- `SensorEval(@Nonnull BuilderSensorEval builderSensorEval, @Nonnull BuilderSupport support)`
  - Creates a `SensorEval` instance.

## Methods
- `matches(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, double dt, @Nonnull Store<EntityStore> store)`
  - Executes `matches` behavior.
- `getSensorInfo()`
  - Executes `getSensorInfo` behavior.
- `compile(@Nonnull String expression, StdScope sensorScope, List<ExecutionContext.Instruction> instructions)`
  - Executes `compile` behavior.
- `evalBoolean(StdScope sensorScope, @Nonnull ExecutionContext.Instruction[] instructions)`
  - Executes `evalBoolean` behavior.

## Notes
- No additional notes.
