# Modifier

## Overview
- Documentation for `Modifier`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `Modifier()`
  - Creates a `Modifier` instance.
- `Modifier(@Nonnull ModifierTarget target, @Nonnull CalculationType calculationType, float amount)`
  - Creates a `Modifier` instance.
- `Modifier(@Nonnull Modifier other)`
  - Creates a `Modifier` instance.

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
