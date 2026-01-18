# CommandContext

## Overview
- Documentation for `CommandContext`.
- Declared as a class in `com.hypixel.hytale.server.core.command.system`.

## Constructors
- `CommandContext(@Nonnull AbstractCommand calledCommand, @Nonnull CommandSender sender, @Nonnull String inputString)`
  - Creates a `CommandContext` instance.

## Methods
- `get(@Nonnull Argument<?, DataType> argument)`
  - Executes `get` behavior.
- `getInput(@Nonnull Argument<?, ?> argument)`
  - Executes `getInput` behavior.
- `provided(@Nonnull Argument<?, ?> argument)`
  - Executes `provided` behavior.
- `getInputString()`
  - Executes `getInputString` behavior.
- `sendMessage(@Nonnull Message message)`
  - Executes `sendMessage` behavior.
- `isPlayer()`
  - Executes `isPlayer` behavior.
- `senderAs(@Nonnull Class<T> senderType)`
  - Executes `senderAs` behavior.
- `senderAsPlayerRef()`
  - Executes `senderAsPlayerRef` behavior.
- `sender()`
  - Executes `sender` behavior.
- `getCalledCommand()`
  - Executes `getCalledCommand` behavior.

## Notes
- No additional notes.
