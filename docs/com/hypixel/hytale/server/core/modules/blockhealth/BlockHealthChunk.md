# BlockHealthChunk

## Overview
- Documentation for `BlockHealthChunk`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.blockhealth`.

## Constructors
- `BlockHealthChunk()`
  - Creates a `BlockHealthChunk` instance.

## Methods
- `getLastRepairGameTime()`
  - Executes `getLastRepairGameTime` behavior.
- `setLastRepairGameTime(Instant lastRepairGameTime)`
  - Executes `setLastRepairGameTime` behavior.
- `getBlockHealthMap()`
  - Executes `getBlockHealthMap` behavior.
- `getBlockFragilityMap()`
  - Executes `getBlockFragilityMap` behavior.
- `damageBlock(Instant currentUptime, @Nonnull World world, @Nonnull Vector3i block, float health)`
  - Executes `damageBlock` behavior.
- `repairBlock(@Nonnull World world, @Nonnull Vector3i block, float progress)`
  - Executes `repairBlock` behavior.
- `removeBlock(@Nonnull World world, @Nonnull Vector3i block)`
  - Executes `removeBlock` behavior.
- `makeBlockFragile(Vector3i blockLocation, float fragileDuration)`
  - Executes `makeBlockFragile` behavior.
- `isBlockFragile(Vector3i block)`
  - Executes `isBlockFragile` behavior.
- `getBlockHealth(Vector3i block)`
  - Executes `getBlockHealth` behavior.
- `createBlockDamagePackets(@Nonnull List<Packet> list)`
  - Executes `createBlockDamagePackets` behavior.
- `clone()`
  - Executes `clone` behavior.
- `deserialize(@Nonnull byte[] data)`
  - Executes `deserialize` behavior.
- `serialize()`
  - Executes `serialize` behavior.

## Notes
- No additional notes.
