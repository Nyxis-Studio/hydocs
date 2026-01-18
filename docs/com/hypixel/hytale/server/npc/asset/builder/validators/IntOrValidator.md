# IntOrValidator

## Overview
- Documentation for `IntOrValidator`.
- Declared as a class in `com.hypixel.hytale.server.npc.asset.builder.validators`.

## Constructors
- `IntOrValidator(RelationalOperator relationOne, int valueOne, RelationalOperator relationTwo, int valueTwo)`
  - Creates a `IntOrValidator` instance.
- `IntOrValidator(RelationalOperator.Greater, 0, RelationalOperator.Equal, -1)`
  - Creates a `IntOrValidator` instance.

## Methods
- `test(int value)`
  - Executes `test` behavior.
- `errorMessage(int value)`
  - Executes `errorMessage` behavior.
- `errorMessage(int value, String name)`
  - Executes `errorMessage` behavior.
- `errorMessage0(int value, String name)`
  - Executes `errorMessage0` behavior.
- `greater0OrMinus1()`
  - Executes `greater0OrMinus1` behavior.

## Notes
- No additional notes.
