# ASTOperand

## Overview
- Documentation for `ASTOperand`.
- Declared as a class in `com.hypixel.hytale.server.npc.util.expression.compile.ast`.

## Constructors
- `ASTOperand(@Nonnull ValueType valueType, @Nonnull Token token, int tokenPosition)`
  - Creates a `ASTOperand` instance.

## Methods
- `createFromParsedToken(@Nonnull Parser.ParsedToken operand, @Nonnull CompileContext compileContext)`
  - Executes `createFromParsedToken` behavior.
- `createFromScopeConstant(@Nonnull Token token, int tokenPosition, @Nonnull Scope scope, String identifier)`
  - Executes `createFromScopeConstant` behavior.
- `createFromOperand(@Nonnull Token token, int tokenPosition, @Nonnull ExecutionContext.Operand operand)`
  - Executes `createFromOperand` behavior.

## Notes
- No additional notes.
