# TimestampedAssetReference

## Overview
- Documentation for `TimestampedAssetReference`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.asseteditor`.

## Constructors
- `TimestampedAssetReference()`
  - Creates a `TimestampedAssetReference` instance.
- `TimestampedAssetReference(@Nullable AssetPath path, @Nullable String timestamp)`
  - Creates a `TimestampedAssetReference` instance.
- `TimestampedAssetReference(@Nonnull TimestampedAssetReference other)`
  - Creates a `TimestampedAssetReference` instance.

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
