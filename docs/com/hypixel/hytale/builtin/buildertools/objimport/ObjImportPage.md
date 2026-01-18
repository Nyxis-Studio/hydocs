# ObjImportPage

## Overview
- Documentation for `ObjImportPage`.
- Declared as a class in `com.hypixel.hytale.builtin.buildertools.objimport`.

## Constructors
- `ObjImportPage(@Nonnull PlayerRef playerRef)`
  - Creates a `ObjImportPage` instance.

## Methods
- `build(@Nonnull Ref<EntityStore> ref, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder, @Nonnull Store<EntityStore> store)`
  - Executes `build` behavior.
- `buildBrowserPage(@Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder)`
  - Executes `buildBrowserPage` behavior.
- `updateStatus(@Nonnull UICommandBuilder commandBuilder)`
  - Executes `updateStatus` behavior.
- `setError(@Nonnull String message)`
  - Executes `setError` behavior.
- `setStatus(@Nonnull String message)`
  - Executes `setStatus` behavior.
- `handleDataEvent(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull PageData data)`
  - Executes `handleDataEvent` behavior.
- `parseBlockPattern(@Nonnull String pattern)`
  - Executes `parseBlockPattern` behavior.
- `selectRandomBlock(@Nonnull List<WeightedBlock> blocks, @Nonnull Random random)`
  - Executes `selectRandomBlock` behavior.
- `performImport(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store)`
  - Executes `performImport` behavior.
- `switchToPasteTool(@Nonnull Player playerComponent, @Nonnull PlayerRef playerRef)`
  - Executes `switchToPasteTool` behavior.
- `loadMaterialData(@Nonnull Path objPath, @Nonnull ObjParser.ObjMesh mesh, @Nonnull BlockColorIndex colorIndex, @Nonnull Map<String, BufferedImage> materialTextures, @Nonnull Map<String, Integer> materialToBlockId, boolean autoDetectTextures)`
  - Executes `loadMaterialData` behavior.
- `findMatchingTexture(@Nonnull Path directory, @Nonnull String materialName)`
  - Executes `findMatchingTexture` behavior.
- `WeightedBlock(int blockId, int weight)`
  - Executes `WeightedBlock` behavior.

## Notes
- No additional notes.
