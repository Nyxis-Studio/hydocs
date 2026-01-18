# MountedUpdate

## Overview
- Documentation for `MountedUpdate`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `MountedUpdate()`
  - Creates a `MountedUpdate` instance.
- `MountedUpdate(int mountedToEntity, @Nullable Vector3f attachmentOffset, @Nonnull MountController controller, @Nullable BlockMount block)`
  - Creates a `MountedUpdate` instance.
- `MountedUpdate(@Nonnull MountedUpdate other)`
  - Creates a `MountedUpdate` instance.

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
