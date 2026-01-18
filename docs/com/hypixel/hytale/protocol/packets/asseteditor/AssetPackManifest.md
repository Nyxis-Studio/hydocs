# AssetPackManifest

## Overview
- Documentation for `AssetPackManifest`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.asseteditor`.

## Constructors
- `AssetPackManifest()`
  - Creates a `AssetPackManifest` instance.
- `AssetPackManifest(@Nullable String name, @Nullable String group, @Nullable String website, @Nullable String description, @Nullable String version, @Nullable AuthorInfo[] authors)`
  - Creates a `AssetPackManifest` instance.
- `AssetPackManifest(@Nonnull AssetPackManifest other)`
  - Creates a `AssetPackManifest` instance.

## Methods
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
