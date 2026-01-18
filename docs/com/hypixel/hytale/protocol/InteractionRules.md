# InteractionRules

## Overview
- Documentation for `InteractionRules`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `InteractionRules()`
  - Creates a `InteractionRules` instance.
- `InteractionRules(@Nullable InteractionType[] blockedBy, @Nullable InteractionType[] blocking, @Nullable InteractionType[] interruptedBy, @Nullable InteractionType[] interrupting, int blockedByBypassIndex, int blockingBypassIndex, int interruptedByBypassIndex, int interruptingBypassIndex)`
  - Creates a `InteractionRules` instance.
- `InteractionRules(@Nonnull InteractionRules other)`
  - Creates a `InteractionRules` instance.

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
