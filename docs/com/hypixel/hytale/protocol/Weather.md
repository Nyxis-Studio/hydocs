# Weather

## Overview
- Documentation for `Weather`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `Weather()`
  - Creates a `Weather` instance.
- `Weather(@Nullable String id, @Nullable int[] tagIndexes, @Nullable String stars, @Nullable Map<Integer, String> moons, @Nullable Cloud[] clouds, @Nullable Map<Float, Float> sunlightDampingMultiplier, @Nullable Map<Float, Color> sunlightColors, @Nullable Map<Float, ColorAlpha> skyTopColors, @Nullable Map<Float, ColorAlpha> skyBottomColors, @Nullable Map<Float, ColorAlpha> skySunsetColors, @Nullable Map<Float, Color> sunColors, @Nullable Map<Float, Float> sunScales, @Nullable Map<Float, ColorAlpha> sunGlowColors, @Nullable Map<Float, ColorAlpha> moonColors, @Nullable Map<Float, Float> moonScales, @Nullable Map<Float, ColorAlpha> moonGlowColors, @Nullable Map<Float, Color> fogColors, @Nullable Map<Float, Float> fogHeightFalloffs, @Nullable Map<Float, Float> fogDensities, @Nullable String screenEffect, @Nullable Map<Float, ColorAlpha> screenEffectColors, @Nullable Map<Float, Color> colorFilters, @Nullable Map<Float, Color> waterTints, @Nullable WeatherParticle particle, @Nullable NearFar fog, @Nullable FogOptions fogOptions)`
  - Creates a `Weather` instance.
- `Weather(@Nonnull Weather other)`
  - Creates a `Weather` instance.

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
