**Source Hash:** `07d6bb0b533ad0d7521e22895ba5dd6d837383bd1e3a416b27ab91681030442f`

# DoubleRangeValidator

## Overview

## Constructor Descriptions
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

## Method Descriptions
- `between01()`: Add description.
  - Executes `between01` behavior.
- `between(double lower, double upper)`: Add description.
  - Executes `between` behavior.
- `fromExclToIncl(double lower, double upper)`: Add description.
  - Executes `fromExclToIncl` behavior.
- `fromExclToExcl(double lower, double upper)`: Add description.
  - Executes `fromExclToExcl` behavior.
- `test(double value)`: Add description.
  - Executes `test` behavior.
- `errorMessage(double value)`: Add description.
  - Executes `errorMessage` behavior.
- `errorMessage(double value, String name)`: Add description.
  - Executes `errorMessage` behavior.
- `errorMessage0(double value, String name)`: Add description.
  - Executes `errorMessage0` behavior.

## Notes
- No additional notes.
