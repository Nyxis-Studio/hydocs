# NPCDumpCommand

## Overview
- Documentation for `NPCDumpCommand`.
- Declared as a class in `com.hypixel.hytale.server.npc.commands`.

## Constructors
- `NPCDumpCommand()`
  - Creates a `NPCDumpCommand` instance.

## Methods
- `execute(@Nonnull CommandContext context, @Nonnull NPCEntity npc, @Nonnull World world, @Nonnull Store<EntityStore> store, @Nonnull Ref<EntityStore> ref)`
  - Executes `execute` behavior.
- `dumpComponent(@Nonnull Role role, @Nonnull IAnnotatedComponent component, int index, int nestingDepth, @Nonnull List<ComponentInfo> infoList)`
  - Executes `dumpComponent` behavior.
- `dumpComponentsAsJson(@Nonnull Role role, @Nonnull IAnnotatedComponent component, int index, int nestingDepth, @Nonnull JsonElement parent)`
  - Executes `dumpComponentsAsJson` behavior.

## Notes
- No additional notes.
