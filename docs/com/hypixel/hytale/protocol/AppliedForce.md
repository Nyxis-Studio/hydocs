# AppliedForce

## Overview
- Documentation for `AppliedForce`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `AppliedForce()`
  - Creates a `AppliedForce` instance.
- `AppliedForce(@Nullable Vector3f direction, boolean adjustVertical, float force)`
  - Creates a `AppliedForce` instance.
- `AppliedForce(@Nonnull AppliedForce other)`
  - Creates a `AppliedForce` instance.

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
