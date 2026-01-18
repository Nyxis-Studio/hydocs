# ActiveEntityEffect

## Overview
- Documentation for `ActiveEntityEffect`.
- Declared as a class in `com.hypixel.hytale.server.core.entity.effect`.

## Constructors
- `ActiveEntityEffect()`
  - Creates a `ActiveEntityEffect` instance.
- `ActiveEntityEffect(@Nonnull String entityEffectId, int entityEffectIndex, float initialDuration, float remainingDuration, boolean infinite, boolean debuff, @Nullable String statusEffectIcon, float sinceLastDamage, boolean hasBeenDamaged, @Nonnull DamageCalculatorSystems.Sequence sequentialHits, boolean invulnerable)`
  - Creates a `ActiveEntityEffect` instance.
- `ActiveEntityEffect(@Nonnull String entityEffectId, int entityEffectIndex, float duration, boolean debuff, @Nullable String statusEffectIcon, boolean invulnerable)`
  - Creates a `ActiveEntityEffect` instance.
- `ActiveEntityEffect(@Nonnull String entityEffectId, int entityEffectIndex, boolean infinite, boolean invulnerable)`
  - Creates a `ActiveEntityEffect` instance.

## Methods
- `tick(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Ref<EntityStore> ref, @Nonnull EntityEffect entityEffect, @Nonnull EntityStatMap entityStatMapComponent, float dt)`
  - Executes `tick` behavior.
- `calculateCyclesToRun(@Nonnull EntityEffect entityEffect, float dt)`
  - Executes `calculateCyclesToRun` behavior.
- `tickStatChanges(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Ref<EntityStore> ref, @Nonnull EntityEffect entityEffect, @Nonnull EntityStatMap entityStatMapComponent, int cyclesToRun)`
  - Executes `tickStatChanges` behavior.
- `tickDamage(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Ref<EntityStore> ref, @Nonnull EntityEffect entityEffect, int cyclesToRun)`
  - Executes `tickDamage` behavior.
- `getEntityEffectIndex()`
  - Executes `getEntityEffectIndex` behavior.
- `getInitialDuration()`
  - Executes `getInitialDuration` behavior.
- `getRemainingDuration()`
  - Executes `getRemainingDuration` behavior.
- `isInfinite()`
  - Executes `isInfinite` behavior.
- `isDebuff()`
  - Executes `isDebuff` behavior.
- `isInvulnerable()`
  - Executes `isInvulnerable` behavior.
- `getDeathMessage(@Nonnull Damage info, @Nonnull Ref<EntityStore> targetRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getDeathMessage` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
