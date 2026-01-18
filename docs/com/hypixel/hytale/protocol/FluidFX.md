# FluidFX

## Overview
- Documentation for `FluidFX`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `FluidFX()`
  - Creates a `FluidFX` instance.
- `FluidFX(@Nullable String id, @Nonnull ShaderType shader, @Nonnull FluidFog fogMode, @Nullable Color fogColor, @Nullable NearFar fogDistance, float fogDepthStart, float fogDepthFalloff, @Nullable Color colorFilter, float colorSaturation, float distortionAmplitude, float distortionFrequency, @Nullable FluidParticle particle, @Nullable FluidFXMovementSettings movementSettings)`
  - Creates a `FluidFX` instance.
- `FluidFX(@Nonnull FluidFX other)`
  - Creates a `FluidFX` instance.

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
