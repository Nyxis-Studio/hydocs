**Source Hash:** `7496da07bfe2d44e4b6da574ad04f9e98b704609ef8fbaeede300c892880ac1a`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# CameraShakeEffect

## Overview
Camera effect that triggers a camera shake using a referenced `CameraShake` asset. Maps optional intensity configuration and converts it into protocol packets.

## Field Descriptions
- `CODEC`: Builder codec used to decode camera shake effects.
- `cameraShakeId`: Asset id for the camera shake to play.
- `cameraShakeIndex`: Cached index for the camera shake asset.
- `intensity`: Optional intensity configuration used for scaling.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `getAccumulationMode()`: Returns the accumulation mode from `ShakeIntensity` or the default when missing.
- `getDefaultIntensityContext()`: Returns the default intensity value, or 0 when missing.
- `calculateIntensity(float intensityContext)`: Applies the modifier curve when present; otherwise returns the original context.
- `createCameraShakePacket()`: Creates a camera shake packet using the default intensity context.
- `createCameraShakePacket(float intensityContext)`: Creates a camera shake packet using calculated intensity and accumulation mode.
- `toString()`: Returns a diagnostic string with ids and intensity data.

## Usage Notes
- `CODEC` resolves the shake id and caches the asset index on decode.

## Examples
```java
CameraShakeEffect effect = CameraShakeEffect.CODEC.decode(reader, extraInfo);
```
