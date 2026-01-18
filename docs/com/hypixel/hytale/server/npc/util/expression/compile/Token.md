# Token

## Overview
- Documentation for `Token`.
- Declared as a enum in `com.hypixel.hytale.server.npc.util.expression.compile`.

## Constructors
- `Token(String text, int precedence)`
  - Creates a `Token` instance.
- `Token(String text, int precedence, EnumSet<TokenFlags> flags)`
  - Creates a `Token` instance.
- `Token(String text, int precedence, EnumSet<TokenFlags> flags, Token matchingBracket, Token unaryVariant)`
  - Creates a `Token` instance.

## Methods
- `get()`
  - Executes `get` behavior.
- `getPrecedence()`
  - Executes `getPrecedence` behavior.
- `getFlags()`
  - Executes `getFlags` behavior.
- `containsAnyFlag(@Nonnull EnumSet<TokenFlags> testFlags)`
  - Executes `containsAnyFlag` behavior.
- `isEndToken()`
  - Executes `isEndToken` behavior.
- `isOperand()`
  - Executes `isOperand` behavior.
- `isLiteral()`
  - Executes `isLiteral` behavior.
- `isOperator()`
  - Executes `isOperator` behavior.
- `isRightToLeft()`
  - Executes `isRightToLeft` behavior.
- `canBeUnary()`
  - Executes `canBeUnary` behavior.
- `getUnaryVariant()`
  - Executes `getUnaryVariant` behavior.
- `isUnary()`
  - Executes `isUnary` behavior.
- `isOpenBracket()`
  - Executes `isOpenBracket` behavior.
- `isOpenTuple()`
  - Executes `isOpenTuple` behavior.
- `isCloseBracket()`
  - Executes `isCloseBracket` behavior.
- `getMatchingBracket()`
  - Executes `getMatchingBracket` behavior.
- `isList()`
  - Executes `isList` behavior.

## Notes
- No additional notes.
