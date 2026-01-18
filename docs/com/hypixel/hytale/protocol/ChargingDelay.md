# ChargingDelay

## Overview
- Documentation for `ChargingDelay`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ChargingDelay()`
  - Creates a `ChargingDelay` instance.
- `ChargingDelay(float minDelay, float maxDelay, float maxTotalDelay, float minHealth, float maxHealth)`
  - Creates a `ChargingDelay` instance.
- `ChargingDelay(@Nonnull ChargingDelay other)`
  - Creates a `ChargingDelay` instance.

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
