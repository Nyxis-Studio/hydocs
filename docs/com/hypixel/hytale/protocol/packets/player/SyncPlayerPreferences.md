# SyncPlayerPreferences

## Overview
- Documentation for `SyncPlayerPreferences`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.player`.

## Constructors
- `SyncPlayerPreferences()`
  - Creates a `SyncPlayerPreferences` instance.
- `SyncPlayerPreferences(boolean showEntityMarkers, @Nonnull PickupLocation armorItemsPreferredPickupLocation, @Nonnull PickupLocation weaponAndToolItemsPreferredPickupLocation, @Nonnull PickupLocation usableItemsItemsPreferredPickupLocation, @Nonnull PickupLocation solidBlockItemsPreferredPickupLocation, @Nonnull PickupLocation miscItemsPreferredPickupLocation, boolean allowNPCDetection, boolean respondToHit)`
  - Creates a `SyncPlayerPreferences` instance.
- `SyncPlayerPreferences(@Nonnull SyncPlayerPreferences other)`
  - Creates a `SyncPlayerPreferences` instance.

## Methods
- `getId()`
  - Executes `getId` behavior.
- `deserialize(@Nonnull ByteBuf buf, int offset)`
  - Executes `deserialize` behavior.
- `computeBytesConsumed(@Nonnull ByteBuf buf, int offset)`
  - Executes `computeBytesConsumed` behavior.
- `serialize(@Nonnull ByteBuf buf)`
  - Executes `serialize` behavior.
- `computeSize()`
  - Executes `computeSize` behavior.
- `validateStructure(@Nonnull ByteBuf buffer, int offset)`
  - Executes `validateStructure` behavior.
- `clone()`
  - Executes `clone` behavior.
- `equals(Object obj)`
  - Executes `equals` behavior.
- `hashCode()`
  - Executes `hashCode` behavior.

## Notes
- No additional notes.
