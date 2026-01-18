# CameraShakeEffect

**Overview**
Camera effect that triggers a camera shake using a referenced `CameraShake` asset.
Maps optional intensity configuration and converts it into protocol packets.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `getAccumulationMode()`: returns how shake intensity accumulates, using defaults when missing.
- `getDefaultIntensityContext()`: returns the default intensity value.
- `calculateIntensity(float intensityContext)`: applies the modifier to the context when configured.
- `createCameraShakePacket()`: creates a packet using the default intensity.
- `createCameraShakePacket(float intensityContext)`: creates a packet using calculated intensity.
- `toString()`: returns a diagnostic string with ids and intensity data.

**Notes**
- `CODEC` resolves the shake id and caches the asset index on decode.
- Inherits from `CameraEffect` and uses `ShakeIntensity` for intensity behavior.
