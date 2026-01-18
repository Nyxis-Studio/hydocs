# LivingEntity

## Overview
- Documentation for `LivingEntity`.
- Declared as a class in `com.hypixel.hytale.server.core.entity`.

## Constructors
- `LivingEntity()`
  - Creates a `LivingEntity` instance.
- `LivingEntity(@Nonnull World world)`
  - Creates a `LivingEntity` instance.

## Methods
- `createDefaultInventory()`
  - Executes `createDefaultInventory` behavior.
- `canBreathe(@Nonnull Ref<EntityStore> ref, @Nonnull BlockMaterial breathingMaterial, int fluidId, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `canBreathe` behavior.
- `getPackedMaterialAndFluidAtBreathingHeight(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getPackedMaterialAndFluidAtBreathingHeight` behavior.
- `getInventory()`
  - Executes `getInventory` behavior.
- `setInventory(Inventory inventory)`
  - Executes `setInventory` behavior.
- `setInventory(Inventory inventory, boolean ensureCapacity)`
  - Executes `setInventory` behavior.
- `setInventory(Inventory inventory, boolean ensureCapacity, List<ItemStack> remainder)`
  - Executes `setInventory` behavior.
- `moveTo(@Nonnull Ref<EntityStore> ref, double locX, double locY, double locZ, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `moveTo` behavior.
- `canDecreaseItemStackDurability(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `canDecreaseItemStackDurability` behavior.
- `canApplyItemStackPenalties(Ref<EntityStore> ref, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `canApplyItemStackPenalties` behavior.
- `decreaseItemStackDurability(@Nonnull Ref<EntityStore> ref, @Nullable ItemStack itemStack, int inventoryId, int slotId, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `decreaseItemStackDurability` behavior.
- `updateItemStackDurability(@Nonnull Ref<EntityStore> ref, @Nonnull ItemStack itemStack, ItemContainer container, int slotId, double durabilityChange, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `updateItemStackDurability` behavior.
- `invalidateEquipmentNetwork()`
  - Executes `invalidateEquipmentNetwork` behavior.
- `consumeEquipmentNetworkOutdated()`
  - Executes `consumeEquipmentNetworkOutdated` behavior.
- `getStatModifiersManager()`
  - Executes `getStatModifiersManager` behavior.
- `getCurrentFallDistance()`
  - Executes `getCurrentFallDistance` behavior.
- `setCurrentFallDistance(double currentFallDistance)`
  - Executes `setCurrentFallDistance` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
