# DoubleRangeValidator

## Overview
- Documentation for `DoubleRangeValidator`.
- Declared as a class in `com.hypixel.hytale.server.npc.asset.builder.validators`.

## Constructors
- `DoubleRangeValidator(RelationalOperator.GreaterEqual, 0.0, RelationalOperator.LessEqual, 1.0)`
  - Creates a `DoubleRangeValidator` instance.
- `DoubleRangeValidator(RelationalOperator relationLower, double lower, RelationalOperator relationUpper, double upper)`
  - Creates a `DoubleRangeValidator` instance.
- `DoubleRangeValidator(RelationalOperator.GreaterEqual, lower, RelationalOperator.LessEqual, upper)`
  - Creates a `DoubleRangeValidator` instance.
- `DoubleRangeValidator(RelationalOperator.Greater, lower, RelationalOperator.LessEqual, upper)`
  - Creates a `DoubleRangeValidator` instance.
- `DoubleRangeValidator(RelationalOperator.Greater, lower, RelationalOperator.Less, upper)`
  - Creates a `DoubleRangeValidator` instance.

## Methods
- `between01()`
  - Executes `between01` behavior.
- `between(double lower, double upper)`
  - Executes `between` behavior.
- `fromExclToIncl(double lower, double upper)`
  - Executes `fromExclToIncl` behavior.
- `fromExclToExcl(double lower, double upper)`
  - Executes `fromExclToExcl` behavior.
- `test(double value)`
  - Executes `test` behavior.
- `errorMessage(double value)`
  - Executes `errorMessage` behavior.
- `errorMessage(double value, String name)`
  - Executes `errorMessage` behavior.
- `errorMessage0(double value, String name)`
  - Executes `errorMessage0` behavior.

## Notes
- No additional notes.
