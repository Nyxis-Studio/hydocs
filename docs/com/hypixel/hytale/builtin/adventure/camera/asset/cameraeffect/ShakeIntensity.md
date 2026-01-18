# ShakeIntensity

**Overview**
Defines how camera shake intensity is derived and accumulated.
Includes a value, accumulation mode, and optional modifier curve.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `getValue()`: returns the default intensity value.
- `getAccumulationMode()`: returns the accumulation mode.
- `getModifier()`: returns the modifier, if any.
- `toString()`: returns a diagnostic string.

**Notes**
- `CODEC` validates ranges and non-null fields.
- `DEFAULT_ACCUMULATION_MODE` defaults to `AccumulationMode.Set`.

---

# ShakeIntensity.Modifier

**Overview**
Maps contextual intensity values to shake intensity using input/output arrays.
Implements `FloatUnaryOperator` for interpolation behavior.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `apply(float intensityContext)`: maps an input intensity to an output intensity.
- `toString()`: returns a diagnostic string.

**Notes**
- Uses `MathUtil.mapToRange` for interpolation across segments.
