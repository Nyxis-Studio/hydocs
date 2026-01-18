# PlayerInteractEvent

## Overview
- Documentation for `PlayerInteractEvent`.
- Declared as a class in `com.hypixel.hytale.server.core.event.events.player`.

## Constructors
- `PlayerInteractEvent(@Nonnull Ref<EntityStore> ref, @Nonnull Player player, long clientUseTime, InteractionType actionType, ItemStack itemInHand, Vector3i targetBlock, Ref<EntityStore> targetRef, Entity targetEntity)`
  - Creates a `PlayerInteractEvent` instance.

## Methods
- `isCancelled()`
  - Executes `isCancelled` behavior.
- `setCancelled(boolean cancelled)`
  - Executes `setCancelled` behavior.
- `getActionType()`
  - Executes `getActionType` behavior.
- `getClientUseTime()`
  - Executes `getClientUseTime` behavior.
- `getItemInHand()`
  - Executes `getItemInHand` behavior.
- `getTargetBlock()`
  - Executes `getTargetBlock` behavior.
- `getTargetEntity()`
  - Executes `getTargetEntity` behavior.
- `getTargetRef()`
  - Executes `getTargetRef` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
