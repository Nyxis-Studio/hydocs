# WorldSupport

## Overview
- Documentation for `WorldSupport`.
- Declared as a class in `com.hypixel.hytale.server.npc.role.support`.

## Constructors
- `WorldSupport(NPCEntity parent, @Nonnull BuilderRole builder, @Nonnull BuilderSupport support)`
  - Creates a `WorldSupport` instance.

## Methods
- `tick(float dt)`
  - Executes `tick` behavior.
- `postRoleBuilt(@Nonnull BuilderSupport support)`
  - Executes `postRoleBuilt` behavior.
- `getCachedBlockTarget(int blockSet)`
  - Executes `getCachedBlockTarget` behavior.
- `resetBlockSensorFoundBlock(int blockSet)`
  - Executes `resetBlockSensorFoundBlock` behavior.
- `resetAllBlockSensors()`
  - Executes `resetAllBlockSensors` behavior.
- `getCachedSearchRayPosition(int id)`
  - Executes `getCachedSearchRayPosition` behavior.
- `resetCachedSearchRayPosition(int id)`
  - Executes `resetCachedSearchRayPosition` behavior.
- `resetAllCachedSearchRayPositions()`
  - Executes `resetAllCachedSearchRayPositions` behavior.
- `setBlockToPlace(String block)`
  - Executes `setBlockToPlace` behavior.
- `getBlockToPlace()`
  - Executes `getBlockToPlace` behavior.
- `getDefaultPlayerAttitude()`
  - Executes `getDefaultPlayerAttitude` behavior.
- `getDefaultNPCAttitude()`
  - Executes `getDefaultNPCAttitude` behavior.
- `getAttitudeGroup()`
  - Executes `getAttitudeGroup` behavior.
- `getItemAttitudeGroup()`
  - Executes `getItemAttitudeGroup` behavior.
- `getAttitude(@Nonnull Ref<EntityStore> ref, @Nonnull Ref<EntityStore> targetRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getAttitude` behavior.
- `getItemAttitude(@Nullable ItemStack item)`
  - Executes `getItemAttitude` behavior.
- `overrideAttitude(Ref<EntityStore> target, Attitude attitude, double duration)`
  - Executes `overrideAttitude` behavior.
- `getOverriddenAttitude(Ref<EntityStore> target)`
  - Executes `getOverriddenAttitude` behavior.
- `requireAttitudeCache()`
  - Executes `requireAttitudeCache` behavior.
- `requestNewPath()`
  - Executes `requestNewPath` behavior.
- `hasRequestedNewPath()`
  - Executes `hasRequestedNewPath` behavior.
- `consumeNewPathRequested()`
  - Executes `consumeNewPathRequested` behavior.
- `getEnvironmentId(@Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getEnvironmentId` behavior.
- `getCurrentWeatherIndex(@Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getCurrentWeatherIndex` behavior.
- `hasTagInGroup(int group, int tag)`
  - Executes `hasTagInGroup` behavior.
- `isGroupMember(int parentRoleIndex, @Nonnull Ref<EntityStore> ref, @Nullable int[] groups, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `isGroupMember` behavior.
- `isGroupMember(int parentRoleIndex, @Nullable Ref<EntityStore> ref, int group, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `isGroupMember` behavior.
- `createTagSetIndexArray(@Nullable String[] tagSets)`
  - Executes `createTagSetIndexArray` behavior.
- `unloaded()`
  - Executes `unloaded` behavior.

## Notes
- No additional notes.
