# ObjectivePlayerSetupSystem

## Overview
- Documentation for `ObjectivePlayerSetupSystem`.
- Declared as a class in `com.hypixel.hytale.builtin.adventure.objectives.systems`.

## Constructors
- `ObjectivePlayerSetupSystem(@Nonnull ComponentType<EntityStore, ObjectiveHistoryComponent> objectiveHistoryComponentType, @Nonnull ComponentType<EntityStore, Player> playerComponentType)`
  - Creates a `ObjectivePlayerSetupSystem` instance.

## Methods
- `getQuery()`
  - Executes `getQuery` behavior.
- `onEntityAdded(@Nonnull Ref<EntityStore> ref, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<EntityStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityRemove` behavior.

## Notes
- No additional notes.
