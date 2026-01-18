**Source Hash:** `c66cfa7b95d3f2d713395dad3726a987e9ff4da672816dff57efa36375761c3d`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# MemoriesClearCommand

## Overview
Admin command that clears all globally recorded memories and confirms the action to the caller.

## Field Descriptions
- `MESSAGE_COMMANDS_MEMORIES_CLEAR_SUCCESS`: Success message sent after clearing memories.

## Constructor Descriptions
- `MemoriesClearCommand()`: Registers the `clear` subcommand for memories.

## Method Descriptions
- `executeSync(CommandContext context)`: Clears recorded memories in `MemoriesPlugin` and sends the success message.

## Examples
```java
// /memories clear
```
