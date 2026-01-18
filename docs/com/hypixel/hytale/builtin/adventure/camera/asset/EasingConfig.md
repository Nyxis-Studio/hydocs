**Source Hash:** `e2d8cd1430da9375f7977da95b514472b0bd6ebf6386f0ce306642637c217cf9`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# EasingConfig

## Overview
Defines easing parameters for camera shake transitions. Encodes duration and easing curve type for fade-in/out behavior.

## Field Descriptions
- `CODEC`: Builder codec used to decode easing configs.
- `NONE`: Default easing config with zero time and linear curve.
- `time`: Duration of the easing segment.
- `type`: Easing curve type.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `toPacket()`: Converts to a protocol `EasingConfig` packet.
- `toString()`: Returns a diagnostic string.

## Usage Notes
- `NONE` provides a zeroed configuration with linear easing.

## Examples
```java
EasingConfig config = EasingConfig.NONE;
```
