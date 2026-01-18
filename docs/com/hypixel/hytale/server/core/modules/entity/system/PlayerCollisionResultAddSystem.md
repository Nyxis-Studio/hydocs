# PlayerCollisionResultAddSystem

## Overview
- Documentation for `PlayerCollisionResultAddSystem`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entity.system`.

## Constructors
- `PlayerCollisionResultAddSystem(@Nonnull ComponentType<EntityStore, Player> playerComponentType, @Nonnull ComponentType<EntityStore, CollisionResultComponent> collisionResultComponentType)`
  - Creates a `PlayerCollisionResultAddSystem` instance.

## Methods
- `onEntityAdd(@Nonnull Holder<EntityStore> holder, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<EntityStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityRemoved` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.

## Notes
- No additional notes.
