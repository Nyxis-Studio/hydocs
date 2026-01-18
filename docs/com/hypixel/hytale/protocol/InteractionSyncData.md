# InteractionSyncData

## Overview
- Documentation for `InteractionSyncData`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `InteractionSyncData()`
  - Creates a `InteractionSyncData` instance.
- `InteractionSyncData(@Nonnull InteractionState state, float progress, int operationCounter, int rootInteraction, int totalForks, int entityId, int enteredRootInteraction, @Nullable BlockPosition blockPosition, @Nonnull BlockFace blockFace, @Nullable BlockRotation blockRotation, int placedBlockId, float chargeValue, @Nullable Map<InteractionType, Integer> forkCounts, int chainingIndex, int flagIndex, @Nullable SelectedHitEntity[] hitEntities, @Nullable Position attackerPos, @Nullable Direction attackerRot, @Nullable Position raycastHit, float raycastDistance, @Nullable Vector3f raycastNormal, @Nonnull MovementDirection movementDirection, @Nonnull ApplyForceState applyForceState, int nextLabel, @Nullable UUID generatedUUID)`
  - Creates a `InteractionSyncData` instance.
- `InteractionSyncData(@Nonnull InteractionSyncData other)`
  - Creates a `InteractionSyncData` instance.

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
