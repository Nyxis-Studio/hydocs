# AST

## Overview
- Documentation for `AST`.
- Declared as a class in `com.hypixel.hytale.server.npc.util.expression.compile.ast`.

## Constructors
- `AST(@Nonnull ValueType valueType, @Nonnull Token token, int tokenPosition)`
  - Creates a `AST` instance.

## Methods
- `getParent()`
  - Executes `getParent` behavior.
- `setParent(AST parent)`
  - Executes `setParent` behavior.
- `getValueType()`
  - Executes `getValueType` behavior.
- `getToken()`
  - Executes `getToken` behavior.
- `getTokenPosition()`
  - Executes `getTokenPosition` behavior.
- `isConstant()`
  - Executes `isConstant` behavior.
- `getString()`
  - Executes `getString` behavior.
- `getBoolean()`
  - Executes `getBoolean` behavior.
- `getNumber()`
  - Executes `getNumber` behavior.
- `returnType()`
  - Executes `returnType` behavior.
- `genCode(@Nonnull List<ExecutionContext.Instruction> list, Scope scope)`
  - Executes `genCode` behavior.

## Notes
- No additional notes.
