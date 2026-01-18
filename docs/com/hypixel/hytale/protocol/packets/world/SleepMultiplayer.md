# SleepMultiplayer

## Overview
- Documentation for `SleepMultiplayer`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.world`.

## Constructors
- `SleepMultiplayer()`
  - Creates a `SleepMultiplayer` instance.
- `SleepMultiplayer(int sleepersCount, int awakeCount, @Nullable UUID[] awakeSample)`
  - Creates a `SleepMultiplayer` instance.
- `SleepMultiplayer(@Nonnull SleepMultiplayer other)`
  - Creates a `SleepMultiplayer` instance.

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
