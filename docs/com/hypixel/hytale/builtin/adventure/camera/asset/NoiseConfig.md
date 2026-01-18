# NoiseConfig

**Overview**
Defines noise parameters used to move the camera during a shake.
Includes seed, type, frequency, amplitude, and clamp configuration.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `toPacket()`: converts to protocol `NoiseConfig`.
- `toString()`: returns a diagnostic string.
- `toPacket(NoiseConfig[] configs)`: converts an array of configs into protocol packets.

**Notes**
- `ARRAY_CODEC` supports arrays of `NoiseConfig` in asset data.
- `NOISE_CONFIGS` is the shared empty packet array.

---

# NoiseConfig.ClampConfig

**Overview**
Clamps noise output into a range and optionally normalizes it.
Enforces min/max values for a stable output band.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `toPacket()`: converts to protocol `ClampConfig`.
- `toString()`: returns a diagnostic string.

**Notes**
- `NONE` provides a default clamp range of -1 to 1.
