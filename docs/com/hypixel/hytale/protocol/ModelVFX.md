# ModelVFX

## Overview
- Documentation for `ModelVFX`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ModelVFX()`
  - Creates a `ModelVFX` instance.
- `ModelVFX(@Nullable String id, @Nonnull SwitchTo switchTo, @Nonnull EffectDirection effectDirection, float animationDuration, @Nullable Vector2f animationRange, @Nonnull LoopOption loopOption, @Nonnull CurveType curveType, @Nullable Color highlightColor, float highlightThickness, boolean useBloomOnHighlight, boolean useProgessiveHighlight, @Nullable Vector2f noiseScale, @Nullable Vector2f noiseScrollSpeed, @Nullable Color postColor, float postColorOpacity)`
  - Creates a `ModelVFX` instance.
- `ModelVFX(@Nonnull ModelVFX other)`
  - Creates a `ModelVFX` instance.

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
