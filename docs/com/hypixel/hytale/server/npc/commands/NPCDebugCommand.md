# NPCDebugCommand

## Overview
- Documentation for `NPCDebugCommand`.
- Declared as a class in `com.hypixel.hytale.server.npc.commands`.

## Constructors
- `NPCDebugCommand()`
  - Creates a `NPCDebugCommand` instance.

## Methods
- `modifyFlags(@Nonnull CommandContext context, @Nonnull NPCEntity npc, @Nonnull Ref<EntityStore> ref, @Nonnull EnumSet<RoleDebugFlags> flags, @Nonnull BiFunction<EnumSet<RoleDebugFlags>, EnumSet<RoleDebugFlags>, EnumSet<RoleDebugFlags>> flagsModifier, @Nonnull Store<EntityStore> store)`
  - Executes `modifyFlags` behavior.
- `safeSetRoleDebugFlags(@Nonnull NPCEntity npc, @Nonnull Ref<EntityStore> ref, @Nonnull EnumSet<RoleDebugFlags> flags, @Nonnull Store<EntityStore> store)`
  - Executes `safeSetRoleDebugFlags` behavior.
- `printNewFlags(@Nonnull NPCEntity npc, @Nonnull CommandContext context, @Nonnull EnumSet<RoleDebugFlags> newFlags)`
  - Executes `printNewFlags` behavior.
- `getListOfFlags(@Nonnull EnumSet<RoleDebugFlags> flags)`
  - Executes `getListOfFlags` behavior.
- `execute(@Nonnull CommandContext context, @Nonnull NPCEntity npc, @Nonnull World world, @Nonnull Store<EntityStore> store, @Nonnull Ref<EntityStore> ref)`
  - Executes `execute` behavior.
- `execute(@Nonnull CommandContext context)`
  - Executes `execute` behavior.

## Notes
- No additional notes.
