# EasingConfig

**Overview**
Defines easing parameters for camera shake transitions.
Encodes duration and easing curve type for fade-in/out behavior.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `toPacket()`: converts to protocol `EasingConfig`.
- `toString()`: returns a diagnostic string.

**Notes**
- `NONE` provides a zeroed configuration with linear easing.
