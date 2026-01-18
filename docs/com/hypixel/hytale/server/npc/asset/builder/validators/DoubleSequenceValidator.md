# DoubleSequenceValidator

## Overview
- Documentation for `DoubleSequenceValidator`.
- Declared as a class in `com.hypixel.hytale.server.npc.asset.builder.validators`.

## Constructors
- `DoubleSequenceValidator(RelationalOperator.GreaterEqual, 0.0, RelationalOperator.LessEqual, 1.0, null)`
  - Creates a `DoubleSequenceValidator` instance.
- `DoubleSequenceValidator(RelationalOperator.GreaterEqual, 0.0, RelationalOperator.LessEqual, 1.0, RelationalOperator.LessEqual)`
  - Creates a `DoubleSequenceValidator` instance.
- `DoubleSequenceValidator(RelationalOperator.GreaterEqual, 0.0, RelationalOperator.LessEqual, 1.0, RelationalOperator.Less)`
  - Creates a `DoubleSequenceValidator` instance.
- `DoubleSequenceValidator(RelationalOperator.GreaterEqual, -1.7976931348623157E308, RelationalOperator.LessEqual, Double.MAX_VALUE, RelationalOperator.LessEqual)`
  - Creates a `DoubleSequenceValidator` instance.
- `DoubleSequenceValidator(RelationalOperator.GreaterEqual, -1.7976931348623157E308, RelationalOperator.LessEqual, Double.MAX_VALUE, RelationalOperator.Less)`
  - Creates a `DoubleSequenceValidator` instance.
- `DoubleSequenceValidator(RelationalOperator relationLower, double lower, RelationalOperator relationUpper, double upper, RelationalOperator relationSequence)`
  - Creates a `DoubleSequenceValidator` instance.
- `DoubleSequenceValidator(RelationalOperator.GreaterEqual, lower, RelationalOperator.LessEqual, upper, null)`
  - Creates a `DoubleSequenceValidator` instance.
- `DoubleSequenceValidator(RelationalOperator.GreaterEqual, lower, RelationalOperator.LessEqual, upper, RelationalOperator.LessEqual)`
  - Creates a `DoubleSequenceValidator` instance.
- `DoubleSequenceValidator(RelationalOperator.GreaterEqual, lower, RelationalOperator.LessEqual, upper, RelationalOperator.Less)`
  - Creates a `DoubleSequenceValidator` instance.
- `DoubleSequenceValidator(RelationalOperator.Greater, lower, RelationalOperator.LessEqual, upper, null)`
  - Creates a `DoubleSequenceValidator` instance.
- `DoubleSequenceValidator(RelationalOperator.Greater, lower, RelationalOperator.LessEqual, upper, RelationalOperator.LessEqual)`
  - Creates a `DoubleSequenceValidator` instance.
- `DoubleSequenceValidator(RelationalOperator.Greater, lower, RelationalOperator.LessEqual, upper, RelationalOperator.Less)`
  - Creates a `DoubleSequenceValidator` instance.

## Methods
- `between01()`
  - Executes `between01` behavior.
- `between01WeaklyMonotonic()`
  - Executes `between01WeaklyMonotonic` behavior.
- `between01Monotonic()`
  - Executes `between01Monotonic` behavior.
- `between(double lower, double upper)`
  - Executes `between` behavior.
- `betweenWeaklyMonotonic(double lower, double upper)`
  - Executes `betweenWeaklyMonotonic` behavior.
- `betweenMonotonic(double lower, double upper)`
  - Executes `betweenMonotonic` behavior.
- `fromExclToIncl(double lower, double upper)`
  - Executes `fromExclToIncl` behavior.
- `fromExclToInclWeaklyMonotonic(double lower, double upper)`
  - Executes `fromExclToInclWeaklyMonotonic` behavior.
- `fromExclToInclMonotonic(double lower, double upper)`
  - Executes `fromExclToInclMonotonic` behavior.
- `monotonic()`
  - Executes `monotonic` behavior.
- `weaklyMonotonic()`
  - Executes `weaklyMonotonic` behavior.
- `test(@Nonnull double[] values)`
  - Executes `test` behavior.
- `errorMessage(double[] value)`
  - Executes `errorMessage` behavior.
- `errorMessage(double[] value, String name)`
  - Executes `errorMessage` behavior.
- `errorMessage0(double[] value, String name)`
  - Executes `errorMessage0` behavior.

## Notes
- No additional notes.
