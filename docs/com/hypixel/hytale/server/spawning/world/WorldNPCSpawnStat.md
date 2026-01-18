# WorldNPCSpawnStat

## Overview
- Documentation for `WorldNPCSpawnStat`.
- Declared as a class in `com.hypixel.hytale.server.spawning.world`.

## Constructors
- `WorldNPCSpawnStat(int roleIndex, WorldSpawnWrapper spawnWrapper, @Nonnull RoleSpawnParameters spawnParams, World world)`
  - Creates a `WorldNPCSpawnStat` instance.
- `WorldNPCSpawnStat(int roleIndex)`
  - Creates a `WorldNPCSpawnStat` instance.

## Methods
- `getRoleIndex()`
  - Executes `getRoleIndex` behavior.
- `getExpected()`
  - Executes `getExpected` behavior.
- `setExpected(double expected)`
  - Executes `setExpected` behavior.
- `getActual()`
  - Executes `getActual` behavior.
- `adjustActual(int count)`
  - Executes `adjustActual` behavior.
- `isUnspawnable()`
  - Executes `isUnspawnable` behavior.
- `setUnspawnable(boolean unspawnable)`
  - Executes `setUnspawnable` behavior.
- `getSpawnWrapper()`
  - Executes `getSpawnWrapper` behavior.
- `getSpawnParams()`
  - Executes `getSpawnParams` behavior.
- `getSpansTried()`
  - Executes `getSpansTried` behavior.
- `getSpansSuccess()`
  - Executes `getSpansSuccess` behavior.
- `getSuccessfulJobCount()`
  - Executes `getSuccessfulJobCount` behavior.
- `getSuccessfulJobTotalBudget()`
  - Executes `getSuccessfulJobTotalBudget` behavior.
- `getFailedJobCount()`
  - Executes `getFailedJobCount` behavior.
- `getFailedJobTotalBudget()`
  - Executes `getFailedJobTotalBudget` behavior.
- `getWeight(int moonPhase)`
  - Executes `getWeight` behavior.
- `getMissingCount(@Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getMissingCount` behavior.
- `getAvailableSlots()`
  - Executes `getAvailableSlots` behavior.
- `getRejectionCount(SpawnRejection rejection)`
  - Executes `getRejectionCount` behavior.
- `updateSpawnStats(int spansTried, int spansSuccess, int budgetUsed, @Nonnull Object2IntMap<SpawnRejection> rejections, boolean success)`
  - Executes `updateSpawnStats` behavior.
- `resetUnspawnable()`
  - Executes `resetUnspawnable` behavior.
- `isSpawnable()`
  - Executes `isSpawnable` behavior.
- `recomputeSpawnSize()`
  - Executes `recomputeSpawnSize` behavior.

## Notes
- No additional notes.
