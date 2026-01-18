# OperatorBinary

## Overview
- Documentation for `OperatorBinary`.
- Declared as a class in `com.hypixel.hytale.server.npc.util.expression.compile`.

## Constructors
- `OperatorBinary(Token token, ValueType lhs, ValueType rhs, ValueType result, Function<Scope, ExecutionContext.Instruction> codeGen)`
  - Creates a `OperatorBinary` instance.
- `OperatorBinary(token, lhs, rhs, result, codeGen)`
  - Creates a `OperatorBinary` instance.

## Methods
- `getResultType()`
  - Executes `getResultType` behavior.
- `of(Token token, ValueType lhs, ValueType rhs, ValueType result, Function<Scope, ExecutionContext.Instruction> codeGen)`
  - Executes `of` behavior.
- `findOperator(Token token, ValueType lhs, ValueType rhs)`
  - Executes `findOperator` behavior.

## Notes
- No additional notes.
