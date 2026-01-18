# InternalContainerUtilMaterial

## Overview
- Documentation for `InternalContainerUtilMaterial`.
- Declared as a class in `com.hypixel.hytale.server.core.inventory.container`.

## Constructors
- None.

## Methods
- `internal_removeMaterialFromSlot(@Nonnull ItemContainer itemContainer, short slot, @Nonnull MaterialQuantity material, boolean allOrNothing, boolean filter)`
  - Executes `internal_removeMaterialFromSlot` behavior.
- `internal_removeMaterial(@Nonnull ItemContainer itemContainer, @Nonnull MaterialQuantity material, boolean allOrNothing, boolean exactAmount, boolean filter)`
  - Executes `internal_removeMaterial` behavior.
- `internal_removeMaterials(@Nonnull ItemContainer itemContainer, @Nullable List<MaterialQuantity> materials, boolean allOrNothing, boolean exactAmount, boolean filter)`
  - Executes `internal_removeMaterials` behavior.
- `testRemoveMaterialFromItems(@Nonnull ItemContainer container, @Nonnull MaterialQuantity material, int testQuantityRemaining, boolean filter)`
  - Executes `testRemoveMaterialFromItems` behavior.
- `getTestRemoveMaterialFromItems(@Nonnull ItemContainer container, @Nonnull MaterialQuantity material, int testQuantityRemaining, boolean filter)`
  - Executes `getTestRemoveMaterialFromItems` behavior.
- `internal_removeMaterialsOrdered(@Nonnull ItemContainer itemContainer, short offset, @Nullable List<MaterialQuantity> materials, boolean allOrNothing, boolean exactAmount, boolean filter)`
  - Executes `internal_removeMaterialsOrdered` behavior.
- `testRemoveMaterialFromSlot(@Nonnull ItemContainer container, short slot, @Nonnull MaterialQuantity material, int testQuantityRemaining, boolean filter)`
  - Executes `testRemoveMaterialFromSlot` behavior.

## Notes
- No additional notes.
