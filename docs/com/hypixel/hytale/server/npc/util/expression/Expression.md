# Expression

## Overview
- Documentation for `Expression`.
- Declared as a class in `com.hypixel.hytale.server.npc.util.expression`.

## Constructors
- `Expression()`
  - Creates a `Expression` instance.

## Methods
- `compile(@Nonnull String expression, Scope scope, @Nonnull List<ExecutionContext.Instruction> instructions, boolean fullResolve)`
  - Executes `compile` behavior.
- `compile(@Nonnull String expression, Scope compileScope, @Nonnull List<ExecutionContext.Instruction> instructions)`
  - Executes `compile` behavior.
- `execute(@Nonnull List<ExecutionContext.Instruction> instructions, Scope scope)`
  - Executes `execute` behavior.
- `execute(@Nonnull ExecutionContext.Instruction[] instructions, Scope scope)`
  - Executes `execute` behavior.
- `evaluate(@Nonnull String expression, Scope scope)`
  - Executes `evaluate` behavior.
- `compileStatic(@Nonnull String expression, Scope scope, @Nonnull List<ExecutionContext.Instruction> instructions)`
  - Executes `compileStatic` behavior.
- `getLexerInstance()`
  - Executes `getLexerInstance` behavior.

## Notes
- No additional notes.
