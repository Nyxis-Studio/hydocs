# UpdateFluids

## Overview
- Documentation for `UpdateFluids`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.assets`.

## Constructors
- `UpdateFluids()`
  - Creates a `UpdateFluids` instance.
- `UpdateFluids(@Nonnull UpdateType type, int maxId, @Nullable Map<Integer, Fluid> fluids)`
  - Creates a `UpdateFluids` instance.
- `UpdateFluids(@Nonnull UpdateFluids other)`
  - Creates a `UpdateFluids` instance.

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
