# ParserContext

## Overview
- Documentation for `ParserContext`.
- Declared as a class in `com.hypixel.hytale.server.core.command.system`.

## Constructors
- `ParserContext(@Nonnull List<String> tokens, @Nonnull ParseResult parseResult)`
  - Creates a `ParserContext` instance.
- `ParserContext(tokens, parseResult)`
  - Creates a `ParserContext` instance.

## Methods
- `of(@Nonnull List<String> tokens, @Nonnull ParseResult parseResult)`
  - Executes `of` behavior.
- `contextualizeTokens(@Nonnull List<String> tokens, @Nonnull ParseResult parseResult)`
  - Executes `contextualizeTokens` behavior.
- `addNewOptionalArg(String name)`
  - Executes `addNewOptionalArg` behavior.
- `appendOptionalParameter(@Nonnull String value, @Nonnull ParseResult parseResult)`
  - Executes `appendOptionalParameter` behavior.
- `getInputString()`
  - Executes `getInputString` behavior.
- `isListToken(int index)`
  - Executes `isListToken` behavior.
- `getNumPreOptSingleValueTokensBeforeListTokens()`
  - Executes `getNumPreOptSingleValueTokensBeforeListTokens` behavior.
- `getNumPreOptionalTokens()`
  - Executes `getNumPreOptionalTokens` behavior.
- `getPreOptionalSingleValueToken(int index)`
  - Executes `getPreOptionalSingleValueToken` behavior.
- `getPreOptionalListToken(int index)`
  - Executes `getPreOptionalListToken` behavior.
- `getFirstToken()`
  - Executes `getFirstToken` behavior.
- `isHelpSpecified()`
  - Executes `isHelpSpecified` behavior.
- `isConfirmationSpecified()`
  - Executes `isConfirmationSpecified` behavior.
- `convertToSubCommand()`
  - Executes `convertToSubCommand` behavior.
- `addToken(@Nonnull String token, @Nonnull ParseResult parseResult)`
  - Executes `addToken` behavior.
- `getStringRepresentation(boolean asTooLongFailure)`
  - Executes `getStringRepresentation` behavior.
- `verifyNumberOfListItems(@Nonnull ParseResult parseResult)`
  - Executes `verifyNumberOfListItems` behavior.
- `getTokens()`
  - Executes `getTokens` behavior.
- `getNumTokensPerArgument()`
  - Executes `getNumTokensPerArgument` behavior.
- `getNumberOfListItems()`
  - Executes `getNumberOfListItems` behavior.

## Notes
- No additional notes.
