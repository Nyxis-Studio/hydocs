**Source Hash:** `9c84226ccdddf7cb467958122e3a57088e7da31b07a583c5631a6c70ade970bd`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# CameraShakeInteraction

## Overview
Instant interaction that triggers a camera shake on use. Resolves a `CameraEffect` asset and sends the corresponding packet.

## Field Descriptions
- `CODEC`: Builder codec for decoding camera shake interactions.
- `effectId`: Camera effect asset id to play.
- `effectIndex`: Cached asset index for the camera effect.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `firstRun(InteractionType type, InteractionContext context, CooldownHandler cooldownHandler)`: Resolves the player, looks up the camera effect asset by index, and sends the shake packet when available.
- `toString()`: Returns a diagnostic string.

## Usage Notes
- Effect indices are cached after decode to avoid repeated asset lookups.

## Examples
```java
CameraShakeInteraction interaction = CameraShakeInteraction.CODEC.decode(reader, extraInfo);
```
