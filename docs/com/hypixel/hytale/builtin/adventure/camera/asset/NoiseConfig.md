**Source Hash:** `72722e1201ae1f9a9d455c3aee7f63e65fc63455beb89167da8ddea191a21c87`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# NoiseConfig

## Overview
Defines noise parameters used to move the camera during a shake. Includes seed, type, frequency, amplitude, and clamp configuration.

## Field Descriptions
- `NOISE_TYPE_CODEC`: Enum codec for `NoiseType`.
- `CODEC`: Builder codec used to decode noise configs.
- `ARRAY_CODEC`: Array codec for noise config arrays.
- `NOISE_CONFIGS`: Shared empty packet array for null/empty conversions.
- `seed`: Seed value for the noise generator.
- `type`: Noise function type.
- `clamp`: Clamp configuration applied to noise output.
- `frequency`: Sampling frequency.
- `amplitude`: Maximum amplitude of the noise output.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `toPacket()`: Converts to protocol `NoiseConfig` packet.
- `toString()`: Returns a diagnostic string.
- `toPacket(NoiseConfig[] configs)`: Converts an array into protocol packets, skipping null entries and returning `NOISE_CONFIGS` when empty.

## Usage Notes
- `ARRAY_CODEC` supports arrays of `NoiseConfig` in asset data.

## Examples
```java
NoiseConfig[] configs = NoiseConfig.CODEC.decode(reader, extraInfo);
```

---

# NoiseConfig.ClampConfig

## Overview
Clamps noise output into a range and optionally normalizes it. Enforces min/max values for a stable output band.

## Field Descriptions
- `CODEC`: Builder codec for clamp configs.
- `NONE`: Default clamp config (-1 to 1, normalized).
- `min`: Inclusive minimum clamp value.
- `max`: Inclusive maximum clamp value.
- `normalize`: Whether to rescale output back to -1..1.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `toPacket()`: Converts to protocol `ClampConfig` packet.
- `toString()`: Returns a diagnostic string.

## Usage Notes
- After decoding, min and max are normalized to ensure `min <= max`.

## Examples
```java
NoiseConfig.ClampConfig clamp = NoiseConfig.ClampConfig.NONE;
```
