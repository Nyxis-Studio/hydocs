# PrefabEditorSaveSettingsPage

## Overview
- Documentation for `PrefabEditorSaveSettingsPage`.
- Declared as a class in `com.hypixel.hytale.builtin.buildertools.prefabeditor.ui`.

## Constructors
- `PrefabEditorSaveSettingsPage(@Nonnull PlayerRef playerRef, @Nonnull PrefabEditSession prefabEditSession)`
  - Creates a `PrefabEditorSaveSettingsPage` instance.

## Methods
- `build(@Nonnull Ref<EntityStore> ref, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder, @Nonnull Store<EntityStore> store)`
  - Executes `build` behavior.
- `handleDataEvent(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull PageData data)`
  - Executes `handleDataEvent` behavior.
- `buildPrefabList(@Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder)`
  - Executes `buildPrefabList` behavior.
- `getWritableSavePath(@Nonnull PrefabEditingMetadata metadata)`
  - Executes `getWritableSavePath` behavior.
- `onSavingFailed(@Nonnull Message errorMessage)`
  - Executes `onSavingFailed` behavior.

## Notes
- No additional notes.
