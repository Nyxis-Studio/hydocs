# ModelTrail

## Overview
- Documentation for `ModelTrail`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ModelTrail()`
  - Creates a `ModelTrail` instance.
- `ModelTrail(@Nullable String trailId, @Nonnull EntityPart targetEntityPart, @Nullable String targetNodeName, @Nullable Vector3f positionOffset, @Nullable Direction rotationOffset, boolean fixedRotation)`
  - Creates a `ModelTrail` instance.
- `ModelTrail(@Nonnull ModelTrail other)`
  - Creates a `ModelTrail` instance.

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
