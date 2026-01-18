# DamageEffects

## Overview
- Documentation for `DamageEffects`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.interaction.interaction.config.server.combat`.

## Constructors
- `DamageEffects(ModelParticle[] modelParticles, com.hypixel.hytale.server.core.asset.type.particle.config.WorldParticle[] worldParticles, String localSoundEventId, String worldSoundEventId, double viewDistance, Knockback knockback)`
  - Creates a `DamageEffects` instance.
- `DamageEffects()`
  - Creates a `DamageEffects` instance.
- `DamageEffects(modelParticlesProtocol, worldParticlesProtocol, this.localSoundEventIndex != 0 ? this.localSoundEventIndex : this.worldSoundEventIndex)`
  - Creates a `DamageEffects` instance.

## Methods
- `getModelParticles()`
  - Executes `getModelParticles` behavior.
- `getWorldSoundEventId()`
  - Executes `getWorldSoundEventId` behavior.
- `getWorldSoundEventIndex()`
  - Executes `getWorldSoundEventIndex` behavior.
- `getLocalSoundEventId()`
  - Executes `getLocalSoundEventId` behavior.
- `getLocalSoundEventIndex()`
  - Executes `getLocalSoundEventIndex` behavior.
- `getViewDistance()`
  - Executes `getViewDistance` behavior.
- `getKnockback()`
  - Executes `getKnockback` behavior.
- `getCameraEffectId()`
  - Executes `getCameraEffectId` behavior.
- `processConfig()`
  - Executes `processConfig` behavior.
- `addToDamage(@Nonnull Damage damageEvent)`
  - Executes `addToDamage` behavior.
- `spawnAtEntity(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Ref<EntityStore> ref)`
  - Executes `spawnAtEntity` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
