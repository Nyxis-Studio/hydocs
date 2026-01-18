# SleepClock

## Overview
- Documentation for `SleepClock`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.world`.

## Constructors
- `SleepClock()`
  - Creates a `SleepClock` instance.
- `SleepClock(@Nullable InstantData startGametime, @Nullable InstantData targetGametime, float progress, float durationSeconds)`
  - Creates a `SleepClock` instance.
- `SleepClock(@Nonnull SleepClock other)`
  - Creates a `SleepClock` instance.

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
