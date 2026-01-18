# RespawnPage

## Overview
- Documentation for `RespawnPage`.
- Declared as a class in `com.hypixel.hytale.server.core.entity.entities.player.pages`.

## Constructors
- `RespawnPage(@Nonnull PlayerRef playerRef, @Nullable Message deathReason, boolean displayDataOnDeathScreen, DeathItemLoss deathItemLoss)`
  - Creates a `RespawnPage` instance.

## Methods
- `combineSimilarItemStacks(@Nullable ItemStack[] itemsLostOnDeath)`
  - Executes `combineSimilarItemStacks` behavior.
- `build(@Nonnull Ref<EntityStore> ref, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder, @Nonnull Store<EntityStore> store)`
  - Executes `build` behavior.
- `handleDataEvent(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull RespawnPageEventData data)`
  - Executes `handleDataEvent` behavior.
- `onDismiss(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store)`
  - Executes `onDismiss` behavior.

## Notes
- No additional notes.
