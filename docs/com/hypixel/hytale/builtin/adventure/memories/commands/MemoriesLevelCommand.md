**Source Hash:** `a2330947c081252fd0b683a3b713f714755084a60bf26a6eaaa9ced5f6c73dce`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# MemoriesLevelCommand

## Overview
World command that reports the current memories level based on the active gameplay configuration.

## Constructor Descriptions
- `MemoriesLevelCommand()`: Registers the `level` subcommand for memories.

## Method Descriptions
- `execute(CommandContext context, World world, Store<EntityStore> store)`: Computes the current memories level and sends it to the command sender.

## Examples
```java
// /memories level
```
