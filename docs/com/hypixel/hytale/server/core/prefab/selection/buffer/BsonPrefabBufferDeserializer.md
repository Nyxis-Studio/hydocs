# BsonPrefabBufferDeserializer

## Overview
- Documentation for `BsonPrefabBufferDeserializer`.
- Declared as a class in `com.hypixel.hytale.server.core.prefab.selection.buffer`.

## Constructors
- `BsonPrefabBufferDeserializer()`
  - Creates a `BsonPrefabBufferDeserializer` instance.

## Methods
- `deserialize(Path path, @Nonnull BsonDocument document)`
  - Executes `deserialize` behavior.
- `deserializeBlockType(@Nonnull PrefabBufferBlockEntry blockEntry, @Nonnull BsonDocument blockDocument, @Nonnull BlockTypeAssetMap<String, BlockType> assetMap, @Nullable Function<String, String> blockMigration)`
  - Executes `deserializeBlockType` behavior.
- `deserializeState(@Nonnull PrefabBufferBlockEntry blockEntry, @Nonnull BsonDocument blockDocument, int version, int worldVersion)`
  - Executes `deserializeState` behavior.
- `deserializeEntityHolders(@Nonnull BsonDocument document, @Nonnull Vector3i anchor, int version, int entityVersion)`
  - Executes `deserializeEntityHolders` behavior.

## Notes
- No additional notes.
