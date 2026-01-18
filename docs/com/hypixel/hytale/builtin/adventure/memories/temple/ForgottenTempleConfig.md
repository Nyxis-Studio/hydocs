**Source Hash:** `ec3d30dcf7ae839a550bf497591ddf1ce303e73c8538979bbf17342e9412a258`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# ForgottenTempleConfig

## Overview
Configuration for the forgotten temple respawn behavior. Defines the Y threshold that triggers respawn and the sound to play.

## Field Descriptions
- `CODEC`: Builder codec for respawn configuration.
- `minYRespawn`: Minimum Y coordinate before a respawn is triggered.
- `respawnSound`: Sound event ID to play on respawn.

## Constructor Descriptions
- `ForgottenTempleConfig()`: Creates a config instance with defaults.

## Method Descriptions
- `getMinYRespawn()`: Returns the minimum Y threshold for respawn.
- `getRespawnSound()`: Returns the sound event ID.
- `getRespawnSoundIndex()`: Returns the sound event index or zero if none is set.

## Usage Notes
- `getRespawnSoundIndex` resolves the ID using the `SoundEvent` asset map.

## Examples
```java
ForgottenTempleConfig config = gameplayConfig.getPluginConfig().get(ForgottenTempleConfig.class);
```
