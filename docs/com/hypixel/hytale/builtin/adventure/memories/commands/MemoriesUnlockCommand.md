**Source Hash:** `bf55724579d20ec4fbf6a1672a1cf099d7f7b41a42c3d582719862c2708a8d98`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# MemoriesUnlockCommand

## Overview
World command that marks all known memories as recorded.

## Field Descriptions
- `MESSAGE_COMMANDS_MEMORIES_UNLOCK_ALL_SUCCESS`: Success message sent after recording all memories.

## Constructor Descriptions
- `MemoriesUnlockCommand()`: Registers the `unlockAll` subcommand.

## Method Descriptions
- `execute(CommandContext context, World world, Store<EntityStore> store)`: Records all memories in `MemoriesPlugin` and sends the success message.

## Examples
```java
// /memories unlockAll
```
