# WorldSettingsCommand

## Overview
- Documentation for `WorldSettingsCommand`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.commands`.

## Constructors
- `WorldSettingsCommand()`
  - Creates a `WorldSettingsCommand` instance.

## Methods
- `generateSubCommand(@Nonnull String command, @Nonnull String description, @Nonnull String arg, @Nonnull ArgumentType<T> argumentType, @Nonnull String display, @Nonnull Function<WorldConfig, T> getter, @Nonnull BiConsumer<WorldConfig, T> setter)`
  - Executes `generateSubCommand` behavior.
- `generateSubCommand(@Nonnull String command, @Nonnull String description, @Nonnull String arg, ArgumentType<T> argumentType, @Nonnull String display, @Nonnull Function<World, T> getter, Function<WorldConfig, T> defaultGetter, @Nonnull BiConsumer<World, T> setter)`
  - Executes `generateSubCommand` behavior.
- `execute(@Nonnull CommandContext context, @Nonnull World world, @Nonnull Store<EntityStore> store)`
  - Executes `execute` behavior.

## Notes
- No additional notes.
