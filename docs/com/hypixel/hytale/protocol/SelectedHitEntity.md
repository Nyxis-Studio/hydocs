# SelectedHitEntity

## Overview
- Documentation for `SelectedHitEntity`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `SelectedHitEntity()`
  - Creates a `SelectedHitEntity` instance.
- `SelectedHitEntity(int networkId, @Nullable Vector3f hitLocation, @Nullable Position position, @Nullable Direction bodyRotation)`
  - Creates a `SelectedHitEntity` instance.
- `SelectedHitEntity(@Nonnull SelectedHitEntity other)`
  - Creates a `SelectedHitEntity` instance.

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
