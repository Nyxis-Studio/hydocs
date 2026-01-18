# CommandManager

## Overview
- Documentation for `CommandManager`.
- Declared as a class in `com.hypixel.hytale.server.core.command.system`.

## Constructors
- `CommandManager()`
  - Creates a `CommandManager` instance.

## Methods
- `get()`
  - Executes `get` behavior.
- `shutdown()`
  - Executes `shutdown` behavior.
- `getCommandRegistration()`
  - Executes `getCommandRegistration` behavior.
- `registerCommands()`
  - Executes `registerCommands` behavior.
- `createVirtualPermissionGroups()`
  - Executes `createVirtualPermissionGroups` behavior.
- `registerSystemCommand(@Nonnull AbstractCommand command)`
  - Executes `registerSystemCommand` behavior.
- `register(@Nonnull AbstractCommand command)`
  - Executes `register` behavior.
- `handleCommand(@Nonnull PlayerRef playerRef, @Nonnull String command)`
  - Executes `handleCommand` behavior.
- `handleCommand(@Nonnull CommandSender commandSender, @Nonnull String commandString)`
  - Executes `handleCommand` behavior.
- `runCommand(@Nonnull CommandSender commandSender, @Nonnull String commandInput, @Nonnull AbstractCommand abstractCommand, @Nonnull CompletableFuture<Void> future)`
  - Executes `runCommand` behavior.
- `isInternalException(@Nonnull Throwable throwable)`
  - Executes `isInternalException` behavior.
- `handleCommands(@Nonnull CommandSender sender, @Nonnull Deque<String> commands)`
  - Executes `handleCommands` behavior.
- `handleCommands0(@Nonnull CommandSender sender, @Nonnull Deque<String> commands)`
  - Executes `handleCommands0` behavior.
- `getName()`
  - Executes `getName` behavior.

## Notes
- No additional notes.
