# EntitySpawnPage

## Overview
- Documentation for `EntitySpawnPage`.
- Declared as a class in `com.hypixel.hytale.server.npc.pages`.

## Constructors
- `EntitySpawnPage(@Nonnull PlayerRef playerRef)`
  - Creates a `EntitySpawnPage` instance.

## Methods
- `build(@Nonnull Ref<EntityStore> ref, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder, @Nonnull Store<EntityStore> store)`
  - Executes `build` behavior.
- `handleDataEvent(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull EntitySpawnPageEventData data)`
  - Executes `handleDataEvent` behavior.
- `handleSelect(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull EntitySpawnPageEventData data)`
  - Executes `handleSelect` behavior.
- `handleSetItemMaterial(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull EntitySpawnPageEventData data)`
  - Executes `handleSetItemMaterial` behavior.
- `clearSelectedItem(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store)`
  - Executes `clearSelectedItem` behavior.
- `handleSpawn(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull EntitySpawnPageEventData data)`
  - Executes `handleSpawn` behavior.
- `spawnNPC(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, int count)`
  - Executes `spawnNPC` behavior.
- `spawnModel(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, int count)`
  - Executes `spawnModel` behavior.
- `onDismiss(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store)`
  - Executes `onDismiss` behavior.
- `clearPreview(@Nonnull Store<EntityStore> store)`
  - Executes `clearPreview` behavior.
- `updateTabVisibility(@Nonnull UICommandBuilder commandBuilder)`
  - Executes `updateTabVisibility` behavior.
- `buildList(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder)`
  - Executes `buildList` behavior.
- `buildNPCList(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder)`
  - Executes `buildNPCList` behavior.
- `buildModelList(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder)`
  - Executes `buildModelList` behavior.
- `buildItemsContent(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull UICommandBuilder commandBuilder)`
  - Executes `buildItemsContent` behavior.
- `selectItem(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull String itemId, @Nonnull UICommandBuilder commandBuilder)`
  - Executes `selectItem` behavior.
- `spawnItem(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, int count)`
  - Executes `spawnItem` behavior.
- `getItemModelId(@Nonnull Item item)`
  - Executes `getItemModelId` behavior.
- `getItemModel(@Nonnull Item item)`
  - Executes `getItemModel` behavior.
- `selectNPCRole(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull String npcRole, @Nonnull UICommandBuilder commandBuilder)`
  - Executes `selectNPCRole` behavior.
- `selectModel(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull String modelId, @Nonnull UICommandBuilder commandBuilder)`
  - Executes `selectModel` behavior.
- `initPosition(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store)`
  - Executes `initPosition` behavior.
- `createOrUpdatePreview(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull UICommandBuilder commandBuilder, @Nullable Model model)`
  - Executes `createOrUpdatePreview` behavior.
- `updatePreviewScale(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store)`
  - Executes `updatePreviewScale` behavior.
- `createOrUpdateBlockPreview(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull String blockTypeKey)`
  - Executes `createOrUpdateBlockPreview` behavior.
- `createOrUpdateItemPreview(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull String itemId)`
  - Executes `createOrUpdateItemPreview` behavior.
- `getNPCModel()`
  - Executes `getNPCModel` behavior.

## Notes
- No additional notes.
