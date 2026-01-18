**Source Hash:** `5cd89d7a31328ae8bb09d09d3a46aecea68aec76c670d2674637ccfe85cdbb2f`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# ShakeIntensity

## Overview
Defines how camera shake intensity is derived and accumulated. Includes a base intensity value, accumulation mode, and optional modifier curve.

## Field Descriptions
- `CODEC`: Builder codec used to decode shake intensity configs.
- `DEFAULT_ACCUMULATION_MODE`: Default accumulation mode (`AccumulationMode.Set`).
- `DEFAULT_CONTEXT_VALUE`: Default context value used when intensity is absent.
- `value`: Base intensity value when no contextual value is supplied.
- `accumulationMode`: Accumulation behavior for overlapping effects.
- `modifier`: Optional modifier curve that maps context values to intensity.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `getValue()`: Returns the default intensity value.
- `getAccumulationMode()`: Returns the accumulation mode.
- `getModifier()`: Returns the modifier, if any.
- `toString()`: Returns a diagnostic string.

## Usage Notes
- `CODEC` enforces ranges and non-null fields for value and accumulation mode.

## Examples
```java
ShakeIntensity intensity = ShakeIntensity.CODEC.decode(reader, extraInfo);
```

---

# ShakeIntensity.Modifier

## Overview
Maps contextual intensity values to shake intensity using input/output arrays. Implements `FloatUnaryOperator` for interpolation behavior.

## Field Descriptions
- `CODEC`: Builder codec for modifier curves.
- `input`: Input control points for context values.
- `output`: Output values corresponding to the input points.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `apply(float intensityContext)`: Maps an input intensity to an output intensity, interpolating between control points.
- `toString()`: Returns a diagnostic string.

## Usage Notes
- Uses `MathUtil.mapToRange` to interpolate across segments.

## Examples
```java
ShakeIntensity.Modifier modifier = ShakeIntensity.Modifier.CODEC.decode(reader, extraInfo);
```
