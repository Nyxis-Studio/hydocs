**Source Hash:** `b4749adb8507ad215389588f8f53ad8847ff0800417797e81bfc920ae547ee61`

# Parser

## Overview

## Constructor Descriptions
- `Parser(Lexer<Token> lexer)`
  - Creates a `Parser` instance.

## Method Descriptions
- `nextToken()`: Add description.
  - Executes `nextToken` behavior.
- `parse(@Nonnull String expression, @Nonnull ParsedTokenConsumer tokenConsumer)`: Add description.
  - Executes `parse` behavior.
- `peekOperator()`: Add description.
  - Executes `peekOperator` behavior.
- `validateOperandCount(@Nonnull ParsedToken bracket)`: Add description.
  - Executes `validateOperandCount` behavior.
- `adjustOperandCount(@Nonnull ParsedToken parsedToken, int operandCount)`: Add description.
  - Executes `adjustOperandCount` behavior.
- `hasLowerPrecedence(@Nonnull Token token, @Nullable ParsedToken stackToken)`: Add description.
  - Executes `hasLowerPrecedence` behavior.
- `arity(@Nonnull Token operator)`: Add description.
  - Executes `arity` behavior.
- `fromLexer(@Nonnull Lexer<Token> lexer, @Nonnull LexerContext<Token> context)`: Add description.
  - Executes `fromLexer` behavior.
- `pushOperand(ParsedToken var1)`: Add description.
  - Executes `pushOperand` behavior.
- `processOperator(ParsedToken var1)`: Add description.
  - Executes `processOperator` behavior.
- `processFunction(int var1)`: Add description.
  - Executes `processFunction` behavior.
- `processTuple(ParsedToken var1, int var2)`: Add description.
  - Executes `processTuple` behavior.
- `done()`: Add description.
  - Executes `done` behavior.

## Notes
- No additional notes.
