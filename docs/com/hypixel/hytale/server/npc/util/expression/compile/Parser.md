# Parser

## Overview
- Documentation for `Parser`.
- Declared as a class in `com.hypixel.hytale.server.npc.util.expression.compile`.

## Constructors
- `Parser(Lexer<Token> lexer)`
  - Creates a `Parser` instance.

## Methods
- `nextToken()`
  - Executes `nextToken` behavior.
- `parse(@Nonnull String expression, @Nonnull ParsedTokenConsumer tokenConsumer)`
  - Executes `parse` behavior.
- `peekOperator()`
  - Executes `peekOperator` behavior.
- `validateOperandCount(@Nonnull ParsedToken bracket)`
  - Executes `validateOperandCount` behavior.
- `adjustOperandCount(@Nonnull ParsedToken parsedToken, int operandCount)`
  - Executes `adjustOperandCount` behavior.
- `hasLowerPrecedence(@Nonnull Token token, @Nullable ParsedToken stackToken)`
  - Executes `hasLowerPrecedence` behavior.
- `arity(@Nonnull Token operator)`
  - Executes `arity` behavior.
- `fromLexer(@Nonnull Lexer<Token> lexer, @Nonnull LexerContext<Token> context)`
  - Executes `fromLexer` behavior.
- `pushOperand(ParsedToken var1)`
  - Executes `pushOperand` behavior.
- `processOperator(ParsedToken var1)`
  - Executes `processOperator` behavior.
- `processFunction(int var1)`
  - Executes `processFunction` behavior.
- `processTuple(ParsedToken var1, int var2)`
  - Executes `processTuple` behavior.
- `done()`
  - Executes `done` behavior.

## Notes
- No additional notes.
