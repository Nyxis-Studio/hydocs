# DespawnComponent

## Overview
- Documentation for `DespawnComponent`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entity`.

## Constructors
- `DespawnComponent()`
  - Creates a `DespawnComponent` instance.
- `DespawnComponent(@Nullable Instant timeToDespawnAt)`
  - Creates a `DespawnComponent` instance.
- `DespawnComponent(time.getNow()`
  - Creates a `DespawnComponent` instance.
- `DespawnComponent(this.timeToDespawnAt)`
  - Creates a `DespawnComponent` instance.

## Methods
- `getComponentType()`
  - Executes `getComponentType` behavior.
- `setDespawn(Instant timeToDespawnAt)`
  - Executes `setDespawn` behavior.
- `setDespawnTo(@Nonnull Instant from, float additionalSeconds)`
  - Executes `setDespawnTo` behavior.
- `getDespawn()`
  - Executes `getDespawn` behavior.
- `despawnInSeconds(@Nonnull TimeResource time, int seconds)`
  - Executes `despawnInSeconds` behavior.
- `despawnInSeconds(@Nonnull TimeResource time, float seconds)`
  - Executes `despawnInSeconds` behavior.
- `despawnInMilliseconds(@Nonnull TimeResource time, long milliseconds)`
  - Executes `despawnInMilliseconds` behavior.
- `trySetDespawn(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull TimeResource timeResource, @Nonnull Ref<EntityStore> ref, @Nullable DespawnComponent despawnComponent, @Nullable Float newLifetime)`
  - Executes `trySetDespawn` behavior.
- `clone()`
  - Executes `clone` behavior.

## Notes
- No additional notes.
