**Source Hash:** `8222265a69579af4ae3aa39f6ff918c4e06841043794206ca21a60abd0c39d7a`

# BlockType

## Overview

## Constructor Descriptions
- `BlockType()`
  - Creates a `BlockType` instance.
- `BlockType(@Nullable String item, @Nullable String name, boolean unknown, @Nonnull DrawType drawType, @Nonnull BlockMaterial material, @Nonnull Opacity opacity, @Nullable ShaderType[] shaderEffect, int hitbox, int interactionHitbox, @Nullable String model, @Nullable ModelTexture[] modelTexture, float modelScale, @Nullable String modelAnimation, boolean looping, int maxSupportDistance, @Nonnull BlockSupportsRequiredForType blockSupportsRequiredFor, @Nullable Map<BlockNeighbor, RequiredBlockFaceSupport[]> support, @Nullable Map<BlockNeighbor, BlockFaceSupport[]> supporting, boolean requiresAlphaBlending, @Nullable BlockTextures[] cubeTextures, @Nullable String cubeSideMaskTexture, @Nonnull ShadingMode cubeShadingMode, @Nonnull RandomRotation randomRotation, @Nonnull VariantRotation variantRotation, @Nonnull Rotation rotationYawPlacementOffset, int blockSoundSetIndex, int ambientSoundEventIndex, @Nullable ModelParticle[] particles, @Nullable String blockParticleSetId, @Nullable String blockBreakingDecalId, @Nullable Color particleColor, @Nullable ColorLight light, @Nullable Tint tint, @Nullable Tint biomeTint, int group, @Nullable String transitionTexture, @Nullable int[] transitionToGroups, @Nullable BlockMovementSettings movementSettings, @Nullable BlockFlags flags, @Nullable String interactionHint, @Nullable BlockGathering gathering, @Nullable BlockPlacementSettings placementSettings, @Nullable ModelDisplay display, @Nullable RailConfig rail, boolean ignoreSupportWhenPlaced, @Nullable Map<InteractionType, Integer> interactions, @Nullable Map<String, Integer> states, int transitionToTag, @Nullable int[] tagIndexes, @Nullable Bench bench, @Nullable ConnectedBlockRuleSet connectedBlockRuleSet)`
  - Creates a `BlockType` instance.
- `BlockType(@Nonnull BlockType other)`
  - Creates a `BlockType` instance.

## Method Descriptions
- `deserialize(@Nonnull ByteBuf buf, int offset)`: Add description.
  - Executes `deserialize` behavior.
- `computeBytesConsumed(@Nonnull ByteBuf buf, int offset)`: Add description.
  - Executes `computeBytesConsumed` behavior.
- `serialize(@Nonnull ByteBuf buf)`: Add description.
  - Executes `serialize` behavior.
- `computeSize()`: Add description.
  - Executes `computeSize` behavior.
- `validateStructure(@Nonnull ByteBuf buffer, int offset)`: Add description.
  - Executes `validateStructure` behavior.
- `clone()`: Add description.
  - Executes `clone` behavior.
- `equals(Object obj)`: Add description.
  - Executes `equals` behavior.
- `hashCode()`: Add description.
  - Executes `hashCode` behavior.

## Notes
- No additional notes.
