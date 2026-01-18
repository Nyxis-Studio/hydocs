# PrefabUtil

## Overview
- Documentation for `PrefabUtil`.
- Declared as a class in `com.hypixel.hytale.server.core.util`.

## Constructors
- None.

## Methods
- `prefabMatchesAtPosition(@Nonnull IPrefabBuffer prefabBuffer, World world, @Nonnull Vector3i position, @Nonnull Rotation yaw, Random random)`
  - Executes `prefabMatchesAtPosition` behavior.
- `canPlacePrefab(@Nonnull IPrefabBuffer prefabBuffer, World world, @Nonnull Vector3i position, @Nonnull Rotation yaw, @Nullable IntSet mask, Random random, boolean ignoreOrigin)`
  - Executes `canPlacePrefab` behavior.
- `paste(@Nonnull IPrefabBuffer buffer, @Nonnull World world, @Nonnull Vector3i position, @Nonnull Rotation yaw, boolean force, Random random, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `paste` behavior.
- `paste(@Nonnull IPrefabBuffer buffer, @Nonnull World world, @Nonnull Vector3i position, @Nonnull Rotation yaw, boolean force, Random random, int setBlockSettings, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `paste` behavior.
- `getNextPrefabId()`
  - Executes `getNextPrefabId` behavior.
- `paste(@Nonnull IPrefabBuffer buffer, @Nonnull World world, @Nonnull Vector3i position, @Nonnull Rotation yaw, boolean force, Random random, int setBlockSettings, boolean technicalPaste, boolean pasteAnchorAsBlock, boolean loadEntities, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `paste` behavior.
- `remove(@Nonnull IPrefabBuffer prefabBuffer, @Nonnull World world, @Nonnull Vector3i position, boolean force, @Nonnull Random random, int setBlockSettings)`
  - Executes `remove` behavior.
- `remove(@Nonnull IPrefabBuffer prefabBuffer, @Nonnull World world, @Nonnull Vector3i position, boolean force, @Nonnull Random random, int setBlockSettings, double brokenParticlesRate)`
  - Executes `remove` behavior.
- `remove(@Nonnull IPrefabBuffer prefabBuffer, @Nonnull World world, @Nonnull Vector3i position, Rotation prefabRotation, boolean force, @Nonnull Random random, int setBlockSettings, double brokenParticlesRate)`
  - Executes `remove` behavior.

## Notes
- No additional notes.
