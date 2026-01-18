# EffectControllerComponent

## Overview
- Documentation for `EffectControllerComponent`.
- Declared as a class in `com.hypixel.hytale.server.core.entity.effect`.

## Constructors
- `EffectControllerComponent()`
  - Creates a `EffectControllerComponent` instance.
- `EffectControllerComponent(@Nonnull EffectControllerComponent effectControllerComponent)`
  - Creates a `EffectControllerComponent` instance.
- `EffectControllerComponent(this)`
  - Creates a `EffectControllerComponent` instance.

## Methods
- `getComponentType()`
  - Executes `getComponentType` behavior.
- `isInvulnerable()`
  - Executes `isInvulnerable` behavior.
- `setInvulnerable(boolean invulnerable)`
  - Executes `setInvulnerable` behavior.
- `addEffect(@Nonnull Ref<EntityStore> ownerRef, @Nonnull EntityEffect entityEffect, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `addEffect` behavior.
- `addEffect(@Nonnull Ref<EntityStore> ownerRef, int entityEffectIndex, @Nonnull EntityEffect entityEffect, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `addEffect` behavior.
- `addEffect(@Nonnull Ref<EntityStore> ownerRef, @Nonnull EntityEffect entityEffect, float duration, @Nonnull OverlapBehavior overlapBehavior, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `addEffect` behavior.
- `addEffect(@Nonnull Ref<EntityStore> ownerRef, int entityEffectIndex, @Nonnull EntityEffect entityEffect, float duration, @Nonnull OverlapBehavior overlapBehavior, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `addEffect` behavior.
- `addInfiniteEffect(@Nonnull Ref<EntityStore> ownerRef, int entityEffectIndex, @Nonnull EntityEffect entityEffect, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `addInfiniteEffect` behavior.
- `setModelChange(@Nonnull Ref<EntityStore> ownerRef, @Nonnull EntityEffect entityEffect, int entityEffectIndex, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `setModelChange` behavior.
- `tryResetModelChange(@Nonnull Ref<EntityStore> ownerRef, int activeEffectIndex, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `tryResetModelChange` behavior.
- `addActiveEntityEffects(@Nonnull ActiveEntityEffect[] activeEntityEffects)`
  - Executes `addActiveEntityEffects` behavior.
- `removeEffect(@Nonnull Ref<EntityStore> ownerRef, int entityEffectIndex, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `removeEffect` behavior.
- `removeEffect(@Nonnull Ref<EntityStore> ownerRef, int entityEffectIndex, @Nonnull RemovalBehavior removalBehavior, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `removeEffect` behavior.
- `addChange(@Nonnull EntityEffectUpdate update)`
  - Executes `addChange` behavior.
- `clearEffects(@Nonnull Ref<EntityStore> ownerRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `clearEffects` behavior.
- `invalidateCache()`
  - Executes `invalidateCache` behavior.
- `getActiveEffects()`
  - Executes `getActiveEffects` behavior.
- `getActiveEffectIndexes()`
  - Executes `getActiveEffectIndexes` behavior.
- `consumeNetworkOutdated()`
  - Executes `consumeNetworkOutdated` behavior.
- `consumeChanges()`
  - Executes `consumeChanges` behavior.
- `clearChanges()`
  - Executes `clearChanges` behavior.
- `createInitUpdates()`
  - Executes `createInitUpdates` behavior.
- `getAllActiveEntityEffects()`
  - Executes `getAllActiveEntityEffects` behavior.
- `toString()`
  - Executes `toString` behavior.
- `clone()`
  - Executes `clone` behavior.

## Notes
- No additional notes.
