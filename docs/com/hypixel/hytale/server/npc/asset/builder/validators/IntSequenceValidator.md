# IntSequenceValidator

## Overview
- Documentation for `IntSequenceValidator`.
- Declared as a class in `com.hypixel.hytale.server.npc.asset.builder.validators`.

## Constructors
- `IntSequenceValidator(RelationalOperator.GreaterEqual, 0, RelationalOperator.LessEqual, 1, null)`
  - Creates a `IntSequenceValidator` instance.
- `IntSequenceValidator(RelationalOperator.GreaterEqual, 0, RelationalOperator.LessEqual, 1, RelationalOperator.LessEqual)`
  - Creates a `IntSequenceValidator` instance.
- `IntSequenceValidator(RelationalOperator.GreaterEqual, 0, RelationalOperator.LessEqual, 1, RelationalOperator.Less)`
  - Creates a `IntSequenceValidator` instance.
- `IntSequenceValidator(RelationalOperator relationLower, int lower, RelationalOperator relationUpper, int upper, RelationalOperator relationSequence)`
  - Creates a `IntSequenceValidator` instance.
- `IntSequenceValidator(RelationalOperator.GreaterEqual, lower, RelationalOperator.LessEqual, upper, null)`
  - Creates a `IntSequenceValidator` instance.
- `IntSequenceValidator(RelationalOperator.GreaterEqual, lower, RelationalOperator.LessEqual, upper, RelationalOperator.LessEqual)`
  - Creates a `IntSequenceValidator` instance.
- `IntSequenceValidator(RelationalOperator.GreaterEqual, lower, RelationalOperator.LessEqual, upper, RelationalOperator.Less)`
  - Creates a `IntSequenceValidator` instance.
- `IntSequenceValidator(RelationalOperator.Greater, lower, RelationalOperator.LessEqual, upper, null)`
  - Creates a `IntSequenceValidator` instance.
- `IntSequenceValidator(RelationalOperator.Greater, lower, RelationalOperator.LessEqual, upper, RelationalOperator.LessEqual)`
  - Creates a `IntSequenceValidator` instance.
- `IntSequenceValidator(RelationalOperator.Greater, lower, RelationalOperator.LessEqual, upper, RelationalOperator.Less)`
  - Creates a `IntSequenceValidator` instance.

## Methods
- `between01()`
  - Executes `between01` behavior.
- `between01WeaklyMonotonic()`
  - Executes `between01WeaklyMonotonic` behavior.
- `between01Monotonic()`
  - Executes `between01Monotonic` behavior.
- `between(int lower, int upper)`
  - Executes `between` behavior.
- `betweenWeaklyMonotonic(int lower, int upper)`
  - Executes `betweenWeaklyMonotonic` behavior.
- `betweenMonotonic(int lower, int upper)`
  - Executes `betweenMonotonic` behavior.
- `fromExclToIncl(int lower, int upper)`
  - Executes `fromExclToIncl` behavior.
- `fromExclToInclWeaklyMonotonic(int lower, int upper)`
  - Executes `fromExclToInclWeaklyMonotonic` behavior.
- `fromExclToInclMonotonic(int lower, int upper)`
  - Executes `fromExclToInclMonotonic` behavior.
- `test(@Nonnull int[] values)`
  - Executes `test` behavior.
- `errorMessage(int[] value)`
  - Executes `errorMessage` behavior.
- `errorMessage(int[] value, String name)`
  - Executes `errorMessage` behavior.
- `errorMessage0(int[] value, String name)`
  - Executes `errorMessage0` behavior.

## Notes
- No additional notes.
