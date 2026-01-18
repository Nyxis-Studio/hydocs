**Source Hash:** `291c54f39b7c50f1d0cc5114a5d8da67d47d8452dff5f6ba14fcb94795e578b5`

# ActiveEntityEffect

## Overview

## Constructor Descriptions
- `ActiveEntityEffect()`
  - Creates a `ActiveEntityEffect` instance.
- `ActiveEntityEffect(@Nonnull String entityEffectId, int entityEffectIndex, float initialDuration, float remainingDuration, boolean infinite, boolean debuff, @Nullable String statusEffectIcon, float sinceLastDamage, boolean hasBeenDamaged, @Nonnull DamageCalculatorSystems.Sequence sequentialHits, boolean invulnerable)`
  - Creates a `ActiveEntityEffect` instance.
- `ActiveEntityEffect(@Nonnull String entityEffectId, int entityEffectIndex, float duration, boolean debuff, @Nullable String statusEffectIcon, boolean invulnerable)`
  - Creates a `ActiveEntityEffect` instance.
- `ActiveEntityEffect(@Nonnull String entityEffectId, int entityEffectIndex, boolean infinite, boolean invulnerable)`
  - Creates a `ActiveEntityEffect` instance.

## Method Descriptions
- `tick(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Ref<EntityStore> ref, @Nonnull EntityEffect entityEffect, @Nonnull EntityStatMap entityStatMapComponent, float dt)`: Add description.
  - Executes `tick` behavior.
- `calculateCyclesToRun(@Nonnull EntityEffect entityEffect, float dt)`: Add description.
  - Executes `calculateCyclesToRun` behavior.
- `tickStatChanges(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Ref<EntityStore> ref, @Nonnull EntityEffect entityEffect, @Nonnull EntityStatMap entityStatMapComponent, int cyclesToRun)`: Add description.
  - Executes `tickStatChanges` behavior.
- `tickDamage(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Ref<EntityStore> ref, @Nonnull EntityEffect entityEffect, int cyclesToRun)`: Add description.
  - Executes `tickDamage` behavior.
- `getEntityEffectIndex()`: Add description.
  - Executes `getEntityEffectIndex` behavior.
- `getInitialDuration()`: Add description.
  - Executes `getInitialDuration` behavior.
- `getRemainingDuration()`: Add description.
  - Executes `getRemainingDuration` behavior.
- `isInfinite()`: Add description.
  - Executes `isInfinite` behavior.
- `isDebuff()`: Add description.
  - Executes `isDebuff` behavior.
- `isInvulnerable()`: Add description.
  - Executes `isInvulnerable` behavior.
- `getDeathMessage(@Nonnull Damage info, @Nonnull Ref<EntityStore> targetRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `getDeathMessage` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.

## Notes
- No additional notes.
