# ComponentUpdate

## Overview
- Documentation for `ComponentUpdate`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ComponentUpdate()`
  - Creates a `ComponentUpdate` instance.
- `ComponentUpdate(@Nonnull ComponentUpdateType type, @Nullable Nameplate nameplate, @Nullable int[] entityUIComponents, @Nullable CombatTextUpdate combatTextUpdate, @Nullable Model model, @Nullable PlayerSkin skin, @Nullable ItemWithAllMetadata item, int blockId, float entityScale, @Nullable Equipment equipment, @Nullable Map<Integer, EntityStatUpdate[]> entityStatUpdates, @Nullable ModelTransform transform, @Nullable MovementStates movementStates, @Nullable EntityEffectUpdate[] entityEffectUpdates, @Nullable Map<InteractionType, Integer> interactions, @Nullable ColorLight dynamicLight, int hitboxCollisionConfigIndex, int repulsionConfigIndex, @Nonnull UUID predictionId, @Nullable int[] soundEventIds, @Nullable String interactionHint, @Nullable MountedUpdate mounted, @Nullable String[] activeAnimations)`
  - Creates a `ComponentUpdate` instance.
- `ComponentUpdate(@Nonnull ComponentUpdate other)`
  - Creates a `ComponentUpdate` instance.

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
