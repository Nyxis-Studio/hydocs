# PageManager

## Overview
- Documentation for `PageManager`.
- Declared as a class in `com.hypixel.hytale.server.core.entity.entities.player.pages`.

## Constructors
- None.

## Methods
- `init(@Nonnull PlayerRef playerRef, @Nonnull WindowManager windowManager)`
  - Executes `init` behavior.
- `clearCustomPageAcknowledgements()`
  - Executes `clearCustomPageAcknowledgements` behavior.
- `getCustomPage()`
  - Executes `getCustomPage` behavior.
- `setPage(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull Page page)`
  - Executes `setPage` behavior.
- `setPage(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull Page page, boolean canCloseThroughInteraction)`
  - Executes `setPage` behavior.
- `openCustomPage(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull CustomUIPage page)`
  - Executes `openCustomPage` behavior.
- `setPageWithWindows(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull Page page, boolean canCloseThroughInteraction, Window ... windows)`
  - Executes `setPageWithWindows` behavior.
- `openCustomPageWithWindows(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull CustomUIPage page, Window ... windows)`
  - Executes `openCustomPageWithWindows` behavior.
- `updateCustomPage(@Nonnull CustomPage page)`
  - Executes `updateCustomPage` behavior.
- `handleEvent(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull CustomPageEvent event)`
  - Executes `handleEvent` behavior.

## Notes
- No additional notes.
