**Source Hash:** `2a390fe3dcd38ee159aa25bac04de47e97df1ed958221aecda1703dfd42fd65a`

# CompileContext

## Overview

## Constructor Descriptions
- `CompileContext()`
  - Creates a `CompileContext` instance.
- `CompileContext(Scope scope)`
  - Creates a `CompileContext` instance.

## Method Descriptions
- `getScope()`: Add description.
  - Executes `getScope` behavior.
- `getOperandStack()`: Add description.
  - Executes `getOperandStack` behavior.
- `getExecutionContext()`: Add description.
  - Executes `getExecutionContext` behavior.
- `compile(@Nonnull String expression, Scope compileScope, boolean fullResolve)`: Add description.
  - Executes `compile` behavior.
- `compile(@Nonnull String expression, Scope compileScope, boolean fullResolve, List<ExecutionContext.Instruction> instructions)`: Add description.
  - Executes `compile` behavior.
- `compile0(@Nonnull String expression, Scope compileScope, boolean fullResolve, List<ExecutionContext.Instruction> instructions)`: Add description.
  - Executes `compile0` behavior.
- `compile(@Nonnull String expression, boolean fullResolve)`: Add description.
  - Executes `compile` behavior.
- `setInstructions(List<ExecutionContext.Instruction> instructionList)`: Add description.
  - Executes `setInstructions` behavior.
- `getResultType()`: Add description.
  - Executes `getResultType` behavior.
- `checkResultType(ValueType type)`: Add description.
  - Executes `checkResultType` behavior.
- `pushOperand(@Nonnull Parser.ParsedToken parsedToken)`: Add description.
  - Executes `pushOperand` behavior.
- `processOperator(@Nonnull Parser.ParsedToken operator)`: Add description.
  - Executes `processOperator` behavior.
- `processFunction(int argumentCount)`: Add description.
  - Executes `processFunction` behavior.
- `processTuple(@Nonnull Parser.ParsedToken openingToken, int argumentCount)`: Add description.
  - Executes `processTuple` behavior.
- `done()`: Add description.
  - Executes `done` behavior.

## Notes
- No additional notes.
