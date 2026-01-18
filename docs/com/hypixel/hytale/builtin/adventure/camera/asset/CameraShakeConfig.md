# CameraShakeConfig

**Overview**
Configuration for a camera shake, including duration, easing, and noise sources.
Serializes into protocol packets for runtime playback.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `toPacket()`: converts the config into a protocol `CameraShakeConfig` packet.
- `toString()`: returns a diagnostic string with all fields.

**Notes**
- Uses `EasingConfig` for ease-in/out and `NoiseConfig` arrays for motion.

---

# CameraShakeConfig.OffsetNoise

**Overview**
Defines translational noise sources for X/Y/Z camera offsets.
Each axis is a list of `NoiseConfig` entries summed together.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `toPacket()`: converts to protocol `OffsetNoise`.
- `toString()`: returns a diagnostic string.

**Notes**
- `NONE` provides a zeroed configuration.

---

# CameraShakeConfig.RotationNoise

**Overview**
Defines rotational noise sources for pitch, yaw, and roll.
Each axis is a list of `NoiseConfig` entries summed together.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `toPacket()`: converts to protocol `RotationNoise`.
- `toString()`: returns a diagnostic string.

**Notes**
- `NONE` provides a zeroed configuration.
