# PluginListPage

## Overview
- Documentation for `PluginListPage`.
- Declared as a class in `com.hypixel.hytale.server.core.plugin.pages`.

## Constructors
- `PluginListPage(@Nonnull PlayerRef playerRef)`
  - Creates a `PluginListPage` instance.

## Methods
- `build(@Nonnull Ref<EntityStore> ref, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder, @Nonnull Store<EntityStore> store)`
  - Executes `build` behavior.
- `handleDataEvent(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull PluginListPageEventData data)`
  - Executes `handleDataEvent` behavior.
- `onDismiss(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store)`
  - Executes `onDismiss` behavior.
- `buildPluginList(@Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder)`
  - Executes `buildPluginList` behavior.
- `selectPlugin(@Nonnull String playerSelectedPlugin, @Nonnull UICommandBuilder commandBuilder)`
  - Executes `selectPlugin` behavior.
- `checkBoxChanged(@Nonnull String pluginName, @Nonnull UICommandBuilder commandBuilder)`
  - Executes `checkBoxChanged` behavior.
- `handlePluginChangeEvent(@Nonnull PluginIdentifier plugin, boolean activeState)`
  - Executes `handlePluginChangeEvent` behavior.

## Notes
- No additional notes.
