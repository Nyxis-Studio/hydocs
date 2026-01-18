# RequiredBlockFaceSupport

## Overview
- Documentation for `RequiredBlockFaceSupport`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `RequiredBlockFaceSupport()`
  - Creates a `RequiredBlockFaceSupport` instance.
- `RequiredBlockFaceSupport(@Nullable String faceType, @Nullable String selfFaceType, @Nullable String blockSetId, int blockTypeId, int tagIndex, int fluidId, @Nonnull SupportMatch support, @Nonnull SupportMatch matchSelf, boolean allowSupportPropagation, boolean rotate, @Nullable Vector3i[] filler)`
  - Creates a `RequiredBlockFaceSupport` instance.
- `RequiredBlockFaceSupport(@Nonnull RequiredBlockFaceSupport other)`
  - Creates a `RequiredBlockFaceSupport` instance.

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
