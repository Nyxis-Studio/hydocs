# HostAddress

## Overview
- Documentation for `HostAddress`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `HostAddress()`
  - Creates a `HostAddress` instance.
- `HostAddress(@Nonnull String host, short port)`
  - Creates a `HostAddress` instance.
- `HostAddress(@Nonnull HostAddress other)`
  - Creates a `HostAddress` instance.

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
