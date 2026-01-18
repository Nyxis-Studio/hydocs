# CustomUICommand

## Overview
- Documentation for `CustomUICommand`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.interface_`.

## Constructors
- `CustomUICommand()`
  - Creates a `CustomUICommand` instance.
- `CustomUICommand(@Nonnull CustomUICommandType type, @Nullable String selector, @Nullable String data, @Nullable String text)`
  - Creates a `CustomUICommand` instance.
- `CustomUICommand(@Nonnull CustomUICommand other)`
  - Creates a `CustomUICommand` instance.

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
