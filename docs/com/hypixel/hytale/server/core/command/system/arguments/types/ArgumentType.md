# ArgumentType

## Overview
- Documentation for `ArgumentType`.
- Declared as a class in `com.hypixel.hytale.server.core.command.system.arguments.types`.

## Constructors
- `ArgumentType(@Nonnull Message name, @Nonnull Message argumentUsage, int numberOfParameters, String ... examples)`
  - Creates a `ArgumentType` instance.
- `ArgumentType(@Nonnull String name, @Nonnull Message argumentUsage, int numberOfParameters, String ... examples)`
  - Creates a `ArgumentType` instance.
- `ArgumentType(String name, @Nonnull String argumentUsage, int numberOfParameters, String ... examples)`
  - Creates a `ArgumentType` instance.

## Methods
- `processedGet(CommandSender sender, CommandContext context, Argument<?, DataType> argument)`
  - Executes `processedGet` behavior.
- `suggest(@Nonnull CommandSender sender, @Nonnull String textAlreadyEntered, int numParametersTyped, @Nonnull SuggestionResult result)`
  - Executes `suggest` behavior.
- `parse(@Nonnull String[] var1, @Nonnull ParseResult var2)`
  - Executes `parse` behavior.
- `getArgumentUsage()`
  - Executes `getArgumentUsage` behavior.
- `getNumberOfParameters()`
  - Executes `getNumberOfParameters` behavior.
- `getName()`
  - Executes `getName` behavior.
- `getExamples()`
  - Executes `getExamples` behavior.
- `isListArgument()`
  - Executes `isListArgument` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
