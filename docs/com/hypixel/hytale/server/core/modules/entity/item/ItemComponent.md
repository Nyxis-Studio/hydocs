**Source Hash:** `8368d2389c903d102526231ba2c355b2eb0f079563829a6ec41a8523db60e0ce`

# ItemComponent

## Overview

## Constructor Descriptions
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

## Method Descriptions
- `getComponentType()`: Add description.
  - Executes `getComponentType` behavior.
- `getItemStack()`: Add description.
  - Executes `getItemStack` behavior.
- `setItemStack(@Nullable ItemStack itemStack)`: Add description.
  - Executes `setItemStack` behavior.
- `setPickupDelay(float pickupDelay)`: Add description.
  - Executes `setPickupDelay` behavior.
- `getPickupRadius(@Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `getPickupRadius` behavior.
- `computeLifetimeSeconds(@Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `computeLifetimeSeconds` behavior.
- `computeDynamicLight()`: Add description.
  - Executes `computeDynamicLight` behavior.
- `pollPickupDelay(float dt)`: Add description.
  - Executes `pollPickupDelay` behavior.
- `pollPickupThrottle(float dt)`: Add description.
  - Executes `pollPickupThrottle` behavior.
- `pollMergeDelay(float dt)`: Add description.
  - Executes `pollMergeDelay` behavior.
- `canPickUp()`: Add description.
  - Executes `canPickUp` behavior.
- `isRemovedByPlayerPickup()`: Add description.
  - Executes `isRemovedByPlayerPickup` behavior.
- `setRemovedByPlayerPickup(boolean removedByPlayerPickup)`: Add description.
  - Executes `setRemovedByPlayerPickup` behavior.
- `consumeNetworkOutdated()`: Add description.
  - Executes `consumeNetworkOutdated` behavior.
- `clone()`: Add description.
  - Executes `clone` behavior.
- `generateItemDrops(@Nonnull ComponentAccessor<EntityStore> accessor, @Nonnull List<ItemStack> itemStacks, @Nonnull Vector3d position, @Nonnull Vector3f rotation)`: Add description.
  - Executes `generateItemDrops` behavior.
- `generateItemDrop(@Nonnull ComponentAccessor<EntityStore> accessor, @Nullable ItemStack itemStack, @Nonnull Vector3d position, @Nonnull Vector3f rotation, float velocityX, float velocityY, float velocityZ)`: Add description.
  - Executes `generateItemDrop` behavior.
- `generatePickedUpItem(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor, @Nonnull Ref<EntityStore> targetRef, @Nonnull Vector3d targetPosition)`: Add description.
  - Executes `generatePickedUpItem` behavior.
- `generatePickedUpItem(@Nonnull ItemStack itemStack, @Nonnull Vector3d position, @Nonnull ComponentAccessor<EntityStore> componentAccessor, @Nonnull Ref<EntityStore> targetRef)`: Add description.
  - Executes `generatePickedUpItem` behavior.
- `addToItemContainer(@Nonnull Store<EntityStore> store, @Nonnull Ref<EntityStore> itemRef, @Nonnull ItemContainer itemContainer)`: Add description.
  - Executes `addToItemContainer` behavior.

## Notes
- No additional notes.
