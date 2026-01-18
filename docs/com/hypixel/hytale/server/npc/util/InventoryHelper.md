# InventoryHelper

## Overview
- Documentation for `InventoryHelper`.
- Declared as a class in `com.hypixel.hytale.server.npc.util`.

## Constructors
- `InventoryHelper()`
  - Creates a `InventoryHelper` instance.

## Methods
- `matchesItem(@Nullable String pattern, @Nonnull ItemStack itemStack)`
  - Executes `matchesItem` behavior.
- `matchesItem(@Nullable List<String> patterns, @Nonnull ItemStack itemStack)`
  - Executes `matchesItem` behavior.
- `matchesPatterns(@Nonnull List<String> patterns, @Nullable String name)`
  - Executes `matchesPatterns` behavior.
- `itemKeyExists(@Nullable String name)`
  - Executes `itemKeyExists` behavior.
- `itemKeyIsBlockType(@Nullable String name)`
  - Executes `itemKeyIsBlockType` behavior.
- `itemDropListKeyExists(@Nullable String name)`
  - Executes `itemDropListKeyExists` behavior.
- `findHotbarSlotWithItem(@Nonnull Inventory inventory, String name)`
  - Executes `findHotbarSlotWithItem` behavior.
- `findHotbarSlotWithItem(@Nonnull Inventory inventory, List<String> name)`
  - Executes `findHotbarSlotWithItem` behavior.
- `findHotbarEmptySlot(@Nonnull Inventory inventory)`
  - Executes `findHotbarEmptySlot` behavior.
- `findInventorySlotWithItem(@Nonnull Inventory inventory, String name)`
  - Executes `findInventorySlotWithItem` behavior.
- `findInventorySlotWithItem(@Nonnull Inventory inventory, List<String> name)`
  - Executes `findInventorySlotWithItem` behavior.
- `countItems(@Nonnull ItemContainer container, List<String> name)`
  - Executes `countItems` behavior.
- `countFreeSlots(@Nonnull ItemContainer container)`
  - Executes `countFreeSlots` behavior.
- `hotbarContainsItem(@Nonnull Inventory inventory, String name)`
  - Executes `hotbarContainsItem` behavior.
- `hotbarContainsItem(@Nonnull Inventory inventory, List<String> name)`
  - Executes `hotbarContainsItem` behavior.
- `holdsItem(@Nonnull Inventory inventory, String name)`
  - Executes `holdsItem` behavior.
- `containsItem(@Nonnull Inventory inventory, String name)`
  - Executes `containsItem` behavior.
- `containsItem(@Nonnull Inventory inventory, List<String> name)`
  - Executes `containsItem` behavior.
- `clearItemInHand(@Nonnull Inventory inventory, byte slotHint)`
  - Executes `clearItemInHand` behavior.
- `removeItemInHand(@Nonnull Inventory inventory)`
  - Executes `removeItemInHand` behavior.
- `checkHotbarSlot(@Nonnull Inventory inventory, byte slot)`
  - Executes `checkHotbarSlot` behavior.
- `checkOffHandSlot(@Nonnull Inventory inventory, byte slot)`
  - Executes `checkOffHandSlot` behavior.
- `setHotbarSlot(@Nonnull Inventory inventory, byte slot)`
  - Executes `setHotbarSlot` behavior.
- `setOffHandSlot(@Nonnull Inventory inventory, byte slot)`
  - Executes `setOffHandSlot` behavior.
- `setHotbarItem(@Nonnull Inventory inventory, @Nullable String name, byte slot)`
  - Executes `setHotbarItem` behavior.
- `setOffHandItem(@Nonnull Inventory inventory, @Nullable String name, byte slot)`
  - Executes `setOffHandItem` behavior.
- `useItem(@Nonnull Inventory inventory, @Nullable String name, byte slotHint)`
  - Executes `useItem` behavior.
- `createItem(@Nullable String name)`
  - Executes `createItem` behavior.
- `useItem(@Nonnull Inventory inventory, @Nullable String name)`
  - Executes `useItem` behavior.
- `useArmor(@Nonnull ItemContainer armorInventory, @Nullable String armorItem)`
  - Executes `useArmor` behavior.
- `useArmor(@Nonnull ItemContainer armorInventory, @Nullable ItemStack itemStack)`
  - Executes `useArmor` behavior.

## Notes
- No additional notes.
