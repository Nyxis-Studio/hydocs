# ASTOperator

## Overview
- Documentation for `ASTOperator`.
- Declared as a class in `com.hypixel.hytale.server.npc.util.expression.compile.ast`.

## Constructors
- `ASTOperator(@Nonnull ValueType returnType, @Nonnull Token token, int tokenPosition)`
  - Creates a `ASTOperator` instance.

## Methods
- `addArgument(@Nonnull AST argument)`
  - Executes `addArgument` behavior.
- `getArguments()`
  - Executes `getArguments` behavior.
- `genCode(@Nonnull List<ExecutionContext.Instruction> list, Scope scope)`
  - Executes `genCode` behavior.
- `fromParsedOperator(@Nonnull Parser.ParsedToken operand, @Nonnull CompileContext compileContext)`
  - Executes `fromParsedOperator` behavior.

## Notes
- No additional notes.
