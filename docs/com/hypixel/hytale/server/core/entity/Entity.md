# Entity

## Overview
- Documentation for `Entity`.
- Declared as a class in `com.hypixel.hytale.server.core.entity`.

## Constructors
- `Entity(@Nullable World world)`
  - Creates a `Entity` instance.
- `Entity()`
  - Creates a `Entity` instance.

## Methods
- `markNeedsSave()`
  - Executes `markNeedsSave` behavior.
- `setLegacyUUID(@Nullable UUID uuid)`
  - Executes `setLegacyUUID` behavior.
- `remove()`
  - Executes `remove` behavior.
- `loadIntoWorld(@Nonnull World world)`
  - Executes `loadIntoWorld` behavior.
- `unloadFromWorld()`
  - Executes `unloadFromWorld` behavior.
- `getNetworkId()`
  - Executes `getNetworkId` behavior.
- `getLegacyDisplayName()`
  - Executes `getLegacyDisplayName` behavior.
- `getUuid()`
  - Executes `getUuid` behavior.
- `setTransformComponent(TransformComponent transform)`
  - Executes `setTransformComponent` behavior.
- `getTransformComponent()`
  - Executes `getTransformComponent` behavior.
- `moveTo(@Nonnull Ref<EntityStore> ref, double locX, double locY, double locZ, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `moveTo` behavior.
- `getWorld()`
  - Executes `getWorld` behavior.
- `wasRemoved()`
  - Executes `wasRemoved` behavior.
- `isCollidable()`
  - Executes `isCollidable` behavior.
- `hashCode()`
  - Executes `hashCode` behavior.
- `equals(@Nullable Object o)`
  - Executes `equals` behavior.
- `toString()`
  - Executes `toString` behavior.
- `isHiddenFromLivingEntity(@Nonnull Ref<EntityStore> ref, @Nonnull Ref<EntityStore> targetRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `isHiddenFromLivingEntity` behavior.
- `setReference(@Nonnull Ref<EntityStore> reference)`
  - Executes `setReference` behavior.
- `getReference()`
  - Executes `getReference` behavior.
- `clearReference()`
  - Executes `clearReference` behavior.
- `clone()`
  - Executes `clone` behavior.
- `toHolder()`
  - Executes `toHolder` behavior.
- `getHurtAnimationIds(@Nonnull MovementStates movementStates, @Nonnull DamageCause damageCause)`
  - Executes `getHurtAnimationIds` behavior.
- `getDeathAnimationIds(@Nonnull MovementStates movementStates, @Nonnull DamageCause damageCause)`
  - Executes `getDeathAnimationIds` behavior.

## Notes
- No additional notes.
