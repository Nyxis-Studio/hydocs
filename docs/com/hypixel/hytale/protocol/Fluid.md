# Fluid

## Overview
- Documentation for `Fluid`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `Fluid()`
  - Creates a `Fluid` instance.
- `Fluid(@Nullable String id, int maxFluidLevel, @Nullable BlockTextures[] cubeTextures, boolean requiresAlphaBlending, @Nonnull Opacity opacity, @Nullable ShaderType[] shaderEffect, @Nullable ColorLight light, int fluidFXIndex, int blockSoundSetIndex, @Nullable String blockParticleSetId, @Nullable Color particleColor, @Nullable int[] tagIndexes)`
  - Creates a `Fluid` instance.
- `Fluid(@Nonnull Fluid other)`
  - Creates a `Fluid` instance.

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
