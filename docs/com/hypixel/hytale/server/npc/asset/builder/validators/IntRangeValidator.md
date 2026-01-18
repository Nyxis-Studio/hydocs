# IntRangeValidator

## Overview
- Documentation for `IntRangeValidator`.
- Declared as a class in `com.hypixel.hytale.server.npc.asset.builder.validators`.

## Constructors
- `IntRangeValidator(RelationalOperator relationLower, int lower, RelationalOperator relationUpper, int upper)`
  - Creates a `IntRangeValidator` instance.
- `IntRangeValidator(RelationalOperator.GreaterEqual, lower, RelationalOperator.Less, upper)`
  - Creates a `IntRangeValidator` instance.
- `IntRangeValidator(RelationalOperator.Greater, lower, RelationalOperator.LessEqual, upper)`
  - Creates a `IntRangeValidator` instance.
- `IntRangeValidator(RelationalOperator.GreaterEqual, lower, RelationalOperator.LessEqual, upper)`
  - Creates a `IntRangeValidator` instance.

## Methods
- `test(int value)`
  - Executes `test` behavior.
- `errorMessage(int value)`
  - Executes `errorMessage` behavior.
- `errorMessage(int value, String name)`
  - Executes `errorMessage` behavior.
- `errorMessage0(int value, String name)`
  - Executes `errorMessage0` behavior.
- `fromInclToExcl(int lower, int upper)`
  - Executes `fromInclToExcl` behavior.
- `fromExclToIncl(int lower, int upper)`
  - Executes `fromExclToIncl` behavior.
- `between(int lower, int upper)`
  - Executes `between` behavior.

## Notes
- No additional notes.
