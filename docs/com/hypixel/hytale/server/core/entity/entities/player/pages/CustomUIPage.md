# CustomUIPage

## Overview
- Documentation for `CustomUIPage`.
- Declared as a class in `com.hypixel.hytale.server.core.entity.entities.player.pages`.

## Constructors
- `CustomUIPage(@Nonnull PlayerRef playerRef, @Nonnull CustomPageLifetime lifetime)`
  - Creates a `CustomUIPage` instance.

## Methods
- `setLifetime(@Nonnull CustomPageLifetime lifetime)`
  - Executes `setLifetime` behavior.
- `getLifetime()`
  - Executes `getLifetime` behavior.
- `handleDataEvent(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, String rawData)`
  - Executes `handleDataEvent` behavior.
- `build(@Nonnull Ref<EntityStore> var1, @Nonnull UICommandBuilder var2, @Nonnull UIEventBuilder var3, @Nonnull Store<EntityStore> var4)`
  - Executes `build` behavior.
- `rebuild()`
  - Executes `rebuild` behavior.
- `sendUpdate()`
  - Executes `sendUpdate` behavior.
- `sendUpdate(@Nullable UICommandBuilder commandBuilder)`
  - Executes `sendUpdate` behavior.
- `sendUpdate(@Nullable UICommandBuilder commandBuilder, boolean clear)`
  - Executes `sendUpdate` behavior.
- `close()`
  - Executes `close` behavior.
- `onDismiss(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store)`
  - Executes `onDismiss` behavior.

## Notes
- No additional notes.
