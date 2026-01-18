# AssetEditorUpdateAsset

## Overview
- Documentation for `AssetEditorUpdateAsset`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.asseteditor`.

## Constructors
- `AssetEditorUpdateAsset()`
  - Creates a `AssetEditorUpdateAsset` instance.
- `AssetEditorUpdateAsset(int token, @Nullable String assetType, @Nullable AssetPath path, int assetIndex, @Nullable byte[] data)`
  - Creates a `AssetEditorUpdateAsset` instance.
- `AssetEditorUpdateAsset(@Nonnull AssetEditorUpdateAsset other)`
  - Creates a `AssetEditorUpdateAsset` instance.

## Methods
- `getId()`
  - Executes `getId` behavior.
- `deserialize(@Nonnull ByteBuf buf, int offset)`
  - Executes `deserialize` behavior.
- `computeBytesConsumed(@Nonnull ByteBuf buf, int offset)`
  - Executes `computeBytesConsumed` behavior.
- `serialize(@Nonnull ByteBuf buf)`
  - Executes `serialize` behavior.
- `computeSize()`
  - Executes `computeSize` behavior.
- `validateStructure(@Nonnull ByteBuf buffer, int offset)`
  - Executes `validateStructure` behavior.
- `clone()`
  - Executes `clone` behavior.
- `equals(Object obj)`
  - Executes `equals` behavior.
- `hashCode()`
  - Executes `hashCode` behavior.

## Notes
- No additional notes.
