# MountPlugin

## Overview
- Documentation for `MountPlugin`.
- Declared as a class in `com.hypixel.hytale.builtin.mounts`.

## Constructors
- `MountPlugin(@Nonnull JavaPluginInit init)`
  - Creates a `MountPlugin` instance.

## Methods
- `getInstance()`
  - Executes `getInstance` behavior.
- `getMountComponentType()`
  - Executes `getMountComponentType` behavior.
- `getMountedComponentType()`
  - Executes `getMountedComponentType` behavior.
- `getMountedByComponentType()`
  - Executes `getMountedByComponentType` behavior.
- `getMinecartComponentType()`
  - Executes `getMinecartComponentType` behavior.
- `setup()`
  - Executes `setup` behavior.
- `getBlockMountComponentType()`
  - Executes `getBlockMountComponentType` behavior.
- `onPlayerDisconnect(@Nonnull PlayerDisconnectEvent event)`
  - Executes `onPlayerDisconnect` behavior.
- `checkDismountNpc(@Nonnull ComponentAccessor<EntityStore> store, @Nonnull Player playerComponent)`
  - Executes `checkDismountNpc` behavior.
- `dismountNpc(@Nonnull ComponentAccessor<EntityStore> store, int mountEntityId)`
  - Executes `dismountNpc` behavior.
- `resetOriginalMountRole(@Nonnull Ref<EntityStore> entityReference, @Nonnull ComponentAccessor<EntityStore> store, @Nonnull NPCMountComponent mountComponent)`
  - Executes `resetOriginalMountRole` behavior.
- `resetOriginalPlayerMovementSettings(@Nonnull PlayerRef playerRef, @Nonnull ComponentAccessor<EntityStore> store)`
  - Executes `resetOriginalPlayerMovementSettings` behavior.

## Notes
- No additional notes.
