# SingleCollector

## Overview
- Documentation for `SingleCollector`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.interaction.interaction.config.data`.

## Constructors
- `SingleCollector(TriFunction<CollectorTag, InteractionContext, Interaction, T> function)`
  - Creates a `SingleCollector` instance.

## Methods
- `getResult()`
  - Executes `getResult` behavior.
- `start()`
  - Executes `start` behavior.
- `into(@Nonnull InteractionContext context, Interaction interaction)`
  - Executes `into` behavior.
- `collect(@Nonnull CollectorTag tag, @Nonnull InteractionContext context, @Nonnull Interaction interaction)`
  - Executes `collect` behavior.
- `outof()`
  - Executes `outof` behavior.
- `finished()`
  - Executes `finished` behavior.

## Notes
- No additional notes.
