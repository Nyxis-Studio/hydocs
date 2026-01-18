# BenchRequirement

## Overview
- Documentation for `BenchRequirement`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `BenchRequirement()`
  - Creates a `BenchRequirement` instance.
- `BenchRequirement(@Nonnull BenchType type, @Nullable String id, @Nullable String[] categories, int requiredTierLevel)`
  - Creates a `BenchRequirement` instance.
- `BenchRequirement(@Nonnull BenchRequirement other)`
  - Creates a `BenchRequirement` instance.

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
