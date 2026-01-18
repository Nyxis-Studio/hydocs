# ItemComponent

## Overview
- Documentation for `ItemComponent`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entity.item`.

## Constructors
- `ItemComponent()`
  - Creates a `ItemComponent` instance.
- `ItemComponent(@Nullable ItemStack itemStack)`
  - Creates a `ItemComponent` instance.
- `ItemComponent(@Nullable ItemStack itemStack, float mergeDelay, float pickupDelay, float pickupThrottle, boolean removedByPlayerPickup)`
  - Creates a `ItemComponent` instance.
- `ItemComponent(this.itemStack, this.mergeDelay, this.pickupDelay, this.pickupThrottle, this.removedByPlayerPickup)`
  - Creates a `ItemComponent` instance.
- `ItemComponent(itemStack)`
  - Creates a `ItemComponent` instance.
- `ItemComponent(new ItemStack(itemStack.getItemId()`
  - Creates a `ItemComponent` instance.

## Methods
- `getComponentType()`
  - Executes `getComponentType` behavior.
- `getItemStack()`
  - Executes `getItemStack` behavior.
- `setItemStack(@Nullable ItemStack itemStack)`
  - Executes `setItemStack` behavior.
- `setPickupDelay(float pickupDelay)`
  - Executes `setPickupDelay` behavior.
- `getPickupRadius(@Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getPickupRadius` behavior.
- `computeLifetimeSeconds(@Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `computeLifetimeSeconds` behavior.
- `computeDynamicLight()`
  - Executes `computeDynamicLight` behavior.
- `pollPickupDelay(float dt)`
  - Executes `pollPickupDelay` behavior.
- `pollPickupThrottle(float dt)`
  - Executes `pollPickupThrottle` behavior.
- `pollMergeDelay(float dt)`
  - Executes `pollMergeDelay` behavior.
- `canPickUp()`
  - Executes `canPickUp` behavior.
- `isRemovedByPlayerPickup()`
  - Executes `isRemovedByPlayerPickup` behavior.
- `setRemovedByPlayerPickup(boolean removedByPlayerPickup)`
  - Executes `setRemovedByPlayerPickup` behavior.
- `consumeNetworkOutdated()`
  - Executes `consumeNetworkOutdated` behavior.
- `clone()`
  - Executes `clone` behavior.
- `generateItemDrops(@Nonnull ComponentAccessor<EntityStore> accessor, @Nonnull List<ItemStack> itemStacks, @Nonnull Vector3d position, @Nonnull Vector3f rotation)`
  - Executes `generateItemDrops` behavior.
- `generateItemDrop(@Nonnull ComponentAccessor<EntityStore> accessor, @Nullable ItemStack itemStack, @Nonnull Vector3d position, @Nonnull Vector3f rotation, float velocityX, float velocityY, float velocityZ)`
  - Executes `generateItemDrop` behavior.
- `generatePickedUpItem(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor, @Nonnull Ref<EntityStore> targetRef, @Nonnull Vector3d targetPosition)`
  - Executes `generatePickedUpItem` behavior.
- `generatePickedUpItem(@Nonnull ItemStack itemStack, @Nonnull Vector3d position, @Nonnull ComponentAccessor<EntityStore> componentAccessor, @Nonnull Ref<EntityStore> targetRef)`
  - Executes `generatePickedUpItem` behavior.
- `addToItemContainer(@Nonnull Store<EntityStore> store, @Nonnull Ref<EntityStore> itemRef, @Nonnull ItemContainer itemContainer)`
  - Executes `addToItemContainer` behavior.

## Notes
- No additional notes.
