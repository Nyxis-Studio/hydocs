**Source Hash:** `6a4c6278ec37722c441371334b97aae5ffb9f9d3cfc63310989ac2e3a2898f26`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# CameraShakeConfig

## Overview
Configuration for a camera shake, including duration, easing, and noise sources. Serializes into protocol packets for runtime playback.

## Field Descriptions
- `CODEC`: Builder codec used to decode camera shake configs.
- `duration`: Time period that the camera shakes at full intensity.
- `startTime`: Optional initial time sample for noise; null uses a continuous clock.
- `easeIn`: Easing config for fade-in.
- `easeOut`: Easing config for fade-out.
- `offset`: Translational noise configuration.
- `rotation`: Rotational noise configuration.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `toPacket()`: Converts the config into a protocol `CameraShakeConfig`, setting continuous mode when `startTime` is absent.
- `toString()`: Returns a diagnostic string with all fields.

## Usage Notes
- Uses `EasingConfig` for ease-in/out and `NoiseConfig` arrays for motion.

## Examples
```java
CameraShakeConfig config = CameraShakeConfig.CODEC.decode(reader, extraInfo);
```

---

# CameraShakeConfig.OffsetNoise

## Overview
Defines translational noise sources for X/Y/Z camera offsets. Each axis is a list of `NoiseConfig` entries summed together.

## Field Descriptions
- `CODEC`: Builder codec for offset noise.
- `NONE`: Default empty offset noise.
- `x`: Noise sources for X translation.
- `y`: Noise sources for Y translation.
- `z`: Noise sources for Z translation.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `toPacket()`: Converts to protocol `OffsetNoise` packet.
- `toString()`: Returns a diagnostic string.

## Usage Notes
- `NONE` provides a zeroed configuration.

## Examples
```java
CameraShakeConfig.OffsetNoise noise = CameraShakeConfig.OffsetNoise.NONE;
```

---

# CameraShakeConfig.RotationNoise

## Overview
Defines rotational noise sources for pitch, yaw, and roll. Each axis is a list of `NoiseConfig` entries summed together.

## Field Descriptions
- `CODEC`: Builder codec for rotation noise.
- `NONE`: Default empty rotation noise.
- `pitch`: Noise sources for pitch.
- `yaw`: Noise sources for yaw.
- `roll`: Noise sources for roll.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `toPacket()`: Converts to protocol `RotationNoise` packet.
- `toString()`: Returns a diagnostic string.

## Usage Notes
- `NONE` provides a zeroed configuration.

## Examples
```java
CameraShakeConfig.RotationNoise noise = CameraShakeConfig.RotationNoise.NONE;
```
