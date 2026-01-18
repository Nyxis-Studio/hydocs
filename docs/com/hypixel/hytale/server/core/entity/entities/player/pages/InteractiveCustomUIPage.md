# InteractiveCustomUIPage

## Overview
- Documentation for `InteractiveCustomUIPage`.
- Declared as a class in `com.hypixel.hytale.server.core.entity.entities.player.pages`.

## Constructors
- `InteractiveCustomUIPage(@Nonnull PlayerRef playerRef, @Nonnull CustomPageLifetime lifetime, @Nonnull BuilderCodec<T> eventDataCodec)`
  - Creates a `InteractiveCustomUIPage` instance.

## Methods
- `handleDataEvent(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull T data)`
  - Executes `handleDataEvent` behavior.
- `sendUpdate(@Nullable UICommandBuilder commandBuilder, @Nullable UIEventBuilder eventBuilder, boolean clear)`
  - Executes `sendUpdate` behavior.
- `handleDataEvent(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, String rawData)`
  - Executes `handleDataEvent` behavior.
- `sendUpdate(@Nullable UICommandBuilder commandBuilder, boolean clear)`
  - Executes `sendUpdate` behavior.

## Notes
- No additional notes.
