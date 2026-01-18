# TemporalSequenceValidator

## Overview
- Documentation for `TemporalSequenceValidator`.
- Declared as a class in `com.hypixel.hytale.server.npc.asset.builder.validators`.

## Constructors
- `TemporalSequenceValidator(RelationalOperator relationLower, TemporalAmount lower, RelationalOperator relationUpper, TemporalAmount upper, RelationalOperator relationSequence)`
  - Creates a `TemporalSequenceValidator` instance.
- `TemporalSequenceValidator(RelationalOperator.GreaterEqual, lower, RelationalOperator.LessEqual, upper, RelationalOperator.Less)`
  - Creates a `TemporalSequenceValidator` instance.
- `TemporalSequenceValidator(RelationalOperator.GreaterEqual, lower, RelationalOperator.LessEqual, upper, RelationalOperator.LessEqual)`
  - Creates a `TemporalSequenceValidator` instance.

## Methods
- `betweenMonotonic(TemporalAmount lower, TemporalAmount upper)`
  - Executes `betweenMonotonic` behavior.
- `betweenWeaklyMonotonic(TemporalAmount lower, TemporalAmount upper)`
  - Executes `betweenWeaklyMonotonic` behavior.
- `compare(@Nonnull LocalDateTime value, @Nonnull RelationalOperator op, LocalDateTime c)`
  - Executes `compare` behavior.
- `test(@Nonnull TemporalAmount[] values)`
  - Executes `test` behavior.
- `errorMessage(String name, TemporalAmount[] value)`
  - Executes `errorMessage` behavior.

## Notes
- No additional notes.
