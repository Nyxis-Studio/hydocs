# CameraShakeInteraction

**Overview**
Instant interaction that triggers a camera shake on use.
Resolves a `CameraEffect` asset and sends the corresponding packet.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `firstRun(InteractionType type, InteractionContext context, CooldownHandler cooldownHandler)`: sends the camera shake packet if the effect is resolved.
- `toString()`: returns a diagnostic string.

**Notes**
- Caches the effect index after decoding the asset reference.
