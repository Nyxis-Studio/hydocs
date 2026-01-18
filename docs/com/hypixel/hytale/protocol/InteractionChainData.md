# InteractionChainData

## Overview
- Documentation for `InteractionChainData`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `InteractionChainData()`
  - Creates a `InteractionChainData` instance.
- `InteractionChainData(int entityId, @Nonnull UUID proxyId, @Nullable Vector3f hitLocation, @Nullable String hitDetail, @Nullable BlockPosition blockPosition, int targetSlot, @Nullable Vector3f hitNormal)`
  - Creates a `InteractionChainData` instance.
- `InteractionChainData(@Nonnull InteractionChainData other)`
  - Creates a `InteractionChainData` instance.

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
