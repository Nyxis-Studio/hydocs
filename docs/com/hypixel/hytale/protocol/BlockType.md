# BlockType

## Overview
- Documentation for `BlockType`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `BlockType()`
  - Creates a `BlockType` instance.
- `BlockType(@Nullable String item, @Nullable String name, boolean unknown, @Nonnull DrawType drawType, @Nonnull BlockMaterial material, @Nonnull Opacity opacity, @Nullable ShaderType[] shaderEffect, int hitbox, int interactionHitbox, @Nullable String model, @Nullable ModelTexture[] modelTexture, float modelScale, @Nullable String modelAnimation, boolean looping, int maxSupportDistance, @Nonnull BlockSupportsRequiredForType blockSupportsRequiredFor, @Nullable Map<BlockNeighbor, RequiredBlockFaceSupport[]> support, @Nullable Map<BlockNeighbor, BlockFaceSupport[]> supporting, boolean requiresAlphaBlending, @Nullable BlockTextures[] cubeTextures, @Nullable String cubeSideMaskTexture, @Nonnull ShadingMode cubeShadingMode, @Nonnull RandomRotation randomRotation, @Nonnull VariantRotation variantRotation, @Nonnull Rotation rotationYawPlacementOffset, int blockSoundSetIndex, int ambientSoundEventIndex, @Nullable ModelParticle[] particles, @Nullable String blockParticleSetId, @Nullable String blockBreakingDecalId, @Nullable Color particleColor, @Nullable ColorLight light, @Nullable Tint tint, @Nullable Tint biomeTint, int group, @Nullable String transitionTexture, @Nullable int[] transitionToGroups, @Nullable BlockMovementSettings movementSettings, @Nullable BlockFlags flags, @Nullable String interactionHint, @Nullable BlockGathering gathering, @Nullable BlockPlacementSettings placementSettings, @Nullable ModelDisplay display, @Nullable RailConfig rail, boolean ignoreSupportWhenPlaced, @Nullable Map<InteractionType, Integer> interactions, @Nullable Map<String, Integer> states, int transitionToTag, @Nullable int[] tagIndexes, @Nullable Bench bench, @Nullable ConnectedBlockRuleSet connectedBlockRuleSet)`
  - Creates a `BlockType` instance.
- `BlockType(@Nonnull BlockType other)`
  - Creates a `BlockType` instance.

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
