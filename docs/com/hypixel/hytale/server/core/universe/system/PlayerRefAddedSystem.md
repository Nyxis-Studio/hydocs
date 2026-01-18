# PlayerRefAddedSystem

## Overview
- Documentation for `PlayerRefAddedSystem`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.system`.

## Constructors
- `PlayerRefAddedSystem(@Nonnull ComponentType<EntityStore, PlayerRef> playerRefComponentType)`
  - Creates a `PlayerRefAddedSystem` instance.

## Methods
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `onEntityAdded(@Nonnull Ref<EntityStore> ref, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<EntityStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityRemove` behavior.

## Notes
- No additional notes.
