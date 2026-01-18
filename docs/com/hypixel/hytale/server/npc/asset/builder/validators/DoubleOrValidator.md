# DoubleOrValidator

## Overview
- Documentation for `DoubleOrValidator`.
- Declared as a class in `com.hypixel.hytale.server.npc.asset.builder.validators`.

## Constructors
- `DoubleOrValidator(RelationalOperator.GreaterEqual, 0.0, RelationalOperator.Equal, -1.0)`
  - Creates a `DoubleOrValidator` instance.
- `DoubleOrValidator(RelationalOperator relationOne, double valueOne, RelationalOperator relationTwo, double valueTwo)`
  - Creates a `DoubleOrValidator` instance.

## Methods
- `test(double value)`
  - Executes `test` behavior.
- `errorMessage(double value)`
  - Executes `errorMessage` behavior.
- `errorMessage(double value, String name)`
  - Executes `errorMessage` behavior.
- `errorMessage0(double value, String name)`
  - Executes `errorMessage0` behavior.
- `greaterEqual0OrMinus1()`
  - Executes `greaterEqual0OrMinus1` behavior.

## Notes
- No additional notes.
