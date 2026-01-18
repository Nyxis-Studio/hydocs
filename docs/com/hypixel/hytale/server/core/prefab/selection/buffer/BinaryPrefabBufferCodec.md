# BinaryPrefabBufferCodec

## Overview
- Documentation for `BinaryPrefabBufferCodec`.
- Declared as a class in `com.hypixel.hytale.server.core.prefab.selection.buffer`.

## Constructors
- `BinaryPrefabBufferCodec()`
  - Creates a `BinaryPrefabBufferCodec` instance.

## Methods
- `deserialize(Path path, @Nonnull ByteBuf buffer)`
  - Executes `deserialize` behavior.
- `deserializeBlock(@Nonnull ByteBuf buffer, @Nonnull BlockTypeAssetMap<String, BlockType> assetMap, @Nullable Function<String, String> blockMigration)`
  - Executes `deserializeBlock` behavior.
- `deserializeFluid(@Nonnull ByteBuf buffer, @Nonnull IndexedLookupTableAssetMap<String, Fluid> assetMap)`
  - Executes `deserializeFluid` behavior.
- `serialize(@Nonnull PrefabBuffer prefabBuffer)`
  - Executes `serialize` behavior.

## Notes
- No additional notes.
