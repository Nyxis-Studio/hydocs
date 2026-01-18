# CompileContext

## Overview
- Documentation for `CompileContext`.
- Declared as a class in `com.hypixel.hytale.server.npc.util.expression.compile`.

## Constructors
- `CompileContext()`
  - Creates a `CompileContext` instance.
- `CompileContext(Scope scope)`
  - Creates a `CompileContext` instance.

## Methods
- `getScope()`
  - Executes `getScope` behavior.
- `getOperandStack()`
  - Executes `getOperandStack` behavior.
- `getExecutionContext()`
  - Executes `getExecutionContext` behavior.
- `compile(@Nonnull String expression, Scope compileScope, boolean fullResolve)`
  - Executes `compile` behavior.
- `compile(@Nonnull String expression, Scope compileScope, boolean fullResolve, List<ExecutionContext.Instruction> instructions)`
  - Executes `compile` behavior.
- `compile0(@Nonnull String expression, Scope compileScope, boolean fullResolve, List<ExecutionContext.Instruction> instructions)`
  - Executes `compile0` behavior.
- `compile(@Nonnull String expression, boolean fullResolve)`
  - Executes `compile` behavior.
- `setInstructions(List<ExecutionContext.Instruction> instructionList)`
  - Executes `setInstructions` behavior.
- `getResultType()`
  - Executes `getResultType` behavior.
- `checkResultType(ValueType type)`
  - Executes `checkResultType` behavior.
- `pushOperand(@Nonnull Parser.ParsedToken parsedToken)`
  - Executes `pushOperand` behavior.
- `processOperator(@Nonnull Parser.ParsedToken operator)`
  - Executes `processOperator` behavior.
- `processFunction(int argumentCount)`
  - Executes `processFunction` behavior.
- `processTuple(@Nonnull Parser.ParsedToken openingToken, int argumentCount)`
  - Executes `processTuple` behavior.
- `done()`
  - Executes `done` behavior.

## Notes
- No additional notes.
