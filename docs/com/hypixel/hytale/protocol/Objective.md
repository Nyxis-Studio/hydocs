# Objective

## Overview
- Documentation for `Objective`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `Objective()`
  - Creates a `Objective` instance.
- `Objective(@Nonnull UUID objectiveUuid, @Nullable String objectiveTitleKey, @Nullable String objectiveDescriptionKey, @Nullable String objectiveLineId, @Nullable ObjectiveTask[] tasks)`
  - Creates a `Objective` instance.
- `Objective(@Nonnull Objective other)`
  - Creates a `Objective` instance.

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
