# SetFluidCmd

## Overview
- Documentation for `SetFluidCmd`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.world`.

## Constructors
- `SetFluidCmd()`
  - Creates a `SetFluidCmd` instance.
- `SetFluidCmd(short index, int fluidId, byte fluidLevel)`
  - Creates a `SetFluidCmd` instance.
- `SetFluidCmd(@Nonnull SetFluidCmd other)`
  - Creates a `SetFluidCmd` instance.

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
