# SyncInteractionChain

## Overview
- Documentation for `SyncInteractionChain`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.interaction`.

## Constructors
- `SyncInteractionChain()`
  - Creates a `SyncInteractionChain` instance.
- `SyncInteractionChain(int activeHotbarSlot, int activeUtilitySlot, int activeToolsSlot, @Nullable String itemInHandId, @Nullable String utilityItemId, @Nullable String toolsItemId, boolean initial, boolean desync, int overrideRootInteraction, @Nonnull InteractionType interactionType, int equipSlot, int chainId, @Nullable ForkedChainId forkedId, @Nullable InteractionChainData data, @Nonnull InteractionState state, @Nullable SyncInteractionChain[] newForks, int operationBaseIndex, @Nullable InteractionSyncData[] interactionData)`
  - Creates a `SyncInteractionChain` instance.
- `SyncInteractionChain(@Nonnull SyncInteractionChain other)`
  - Creates a `SyncInteractionChain` instance.

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
