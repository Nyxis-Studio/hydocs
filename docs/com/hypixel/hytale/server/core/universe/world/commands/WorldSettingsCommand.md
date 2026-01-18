**Source Hash:** `adc7845bc779264bd1f0238e51932279764aede4c425da55b9a79fc4e40f61e0`

# WorldSettingsCommand

## Overview

## Constructor Descriptions
- `WorldSettingsCommand()`
  - Creates a `WorldSettingsCommand` instance.

## Method Descriptions
- `generateSubCommand(@Nonnull String command, @Nonnull String description, @Nonnull String arg, @Nonnull ArgumentType<T> argumentType, @Nonnull String display, @Nonnull Function<WorldConfig, T> getter, @Nonnull BiConsumer<WorldConfig, T> setter)`: Add description.
  - Executes `generateSubCommand` behavior.
- `generateSubCommand(@Nonnull String command, @Nonnull String description, @Nonnull String arg, ArgumentType<T> argumentType, @Nonnull String display, @Nonnull Function<World, T> getter, Function<WorldConfig, T> defaultGetter, @Nonnull BiConsumer<World, T> setter)`: Add description.
  - Executes `generateSubCommand` behavior.
- `execute(@Nonnull CommandContext context, @Nonnull World world, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `execute` behavior.

## Notes
- No additional notes.
