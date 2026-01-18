**Source Hash:** `46f4fe825a9cb6295f51872995a59945134d224e8e5daddab71bf3ca2efa1702`

# BlockHealthChunk

## Overview

## Constructor Descriptions
- `BlockHealthChunk()`
  - Creates a `BlockHealthChunk` instance.

## Method Descriptions
- `getLastRepairGameTime()`: Add description.
  - Executes `getLastRepairGameTime` behavior.
- `setLastRepairGameTime(Instant lastRepairGameTime)`: Add description.
  - Executes `setLastRepairGameTime` behavior.
- `getBlockHealthMap()`: Add description.
  - Executes `getBlockHealthMap` behavior.
- `getBlockFragilityMap()`: Add description.
  - Executes `getBlockFragilityMap` behavior.
- `damageBlock(Instant currentUptime, @Nonnull World world, @Nonnull Vector3i block, float health)`: Add description.
  - Executes `damageBlock` behavior.
- `repairBlock(@Nonnull World world, @Nonnull Vector3i block, float progress)`: Add description.
  - Executes `repairBlock` behavior.
- `removeBlock(@Nonnull World world, @Nonnull Vector3i block)`: Add description.
  - Executes `removeBlock` behavior.
- `makeBlockFragile(Vector3i blockLocation, float fragileDuration)`: Add description.
  - Executes `makeBlockFragile` behavior.
- `isBlockFragile(Vector3i block)`: Add description.
  - Executes `isBlockFragile` behavior.
- `getBlockHealth(Vector3i block)`: Add description.
  - Executes `getBlockHealth` behavior.
- `createBlockDamagePackets(@Nonnull List<Packet> list)`: Add description.
  - Executes `createBlockDamagePackets` behavior.
- `clone()`: Add description.
  - Executes `clone` behavior.
- `deserialize(@Nonnull byte[] data)`: Add description.
  - Executes `deserialize` behavior.
- `serialize()`: Add description.
  - Executes `serialize` behavior.

## Notes
- No additional notes.
