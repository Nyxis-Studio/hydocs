**Source Hash:** `9ee6ad983c104b680a33fafe2a2e1cf31b1869845035534b8c298946661798bd`

# TemporalSequenceValidator

## Overview

## Constructor Descriptions
- `TemporalSequenceValidator(RelationalOperator relationLower, TemporalAmount lower, RelationalOperator relationUpper, TemporalAmount upper, RelationalOperator relationSequence)`
  - Creates a `TemporalSequenceValidator` instance.
- `TemporalSequenceValidator(RelationalOperator.GreaterEqual, lower, RelationalOperator.LessEqual, upper, RelationalOperator.Less)`
  - Creates a `TemporalSequenceValidator` instance.
- `TemporalSequenceValidator(RelationalOperator.GreaterEqual, lower, RelationalOperator.LessEqual, upper, RelationalOperator.LessEqual)`
  - Creates a `TemporalSequenceValidator` instance.

## Method Descriptions
- `betweenMonotonic(TemporalAmount lower, TemporalAmount upper)`: Add description.
  - Executes `betweenMonotonic` behavior.
- `betweenWeaklyMonotonic(TemporalAmount lower, TemporalAmount upper)`: Add description.
  - Executes `betweenWeaklyMonotonic` behavior.
- `compare(@Nonnull LocalDateTime value, @Nonnull RelationalOperator op, LocalDateTime c)`: Add description.
  - Executes `compare` behavior.
- `test(@Nonnull TemporalAmount[] values)`: Add description.
  - Executes `test` behavior.
- `errorMessage(String name, TemporalAmount[] value)`: Add description.
  - Executes `errorMessage` behavior.

## Notes
- No additional notes.
