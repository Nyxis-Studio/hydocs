# PermissionsModule

## Overview
- Documentation for `PermissionsModule`.
- Declared as a class in `com.hypixel.hytale.server.core.permissions`.

## Constructors
- `PermissionsModule(@Nonnull JavaPluginInit init)`
  - Creates a `PermissionsModule` instance.

## Methods
- `get()`
  - Executes `get` behavior.
- `setup()`
  - Executes `setup` behavior.
- `start()`
  - Executes `start` behavior.
- `addProvider(@Nonnull PermissionProvider permissionProvider)`
  - Executes `addProvider` behavior.
- `removeProvider(@Nonnull PermissionProvider provider)`
  - Executes `removeProvider` behavior.
- `getProviders()`
  - Executes `getProviders` behavior.
- `getFirstPermissionProvider()`
  - Executes `getFirstPermissionProvider` behavior.
- `areProvidersTampered()`
  - Executes `areProvidersTampered` behavior.
- `addUserPermission(@Nonnull UUID uuid, @Nonnull Set<String> permissions)`
  - Executes `addUserPermission` behavior.
- `removeUserPermission(@Nonnull UUID uuid, @Nonnull Set<String> permissions)`
  - Executes `removeUserPermission` behavior.
- `addGroupPermission(@Nonnull String group, @Nonnull Set<String> permissions)`
  - Executes `addGroupPermission` behavior.
- `removeGroupPermission(@Nonnull String group, @Nonnull Set<String> permissions)`
  - Executes `removeGroupPermission` behavior.
- `addUserToGroup(@Nonnull UUID uuid, @Nonnull String group)`
  - Executes `addUserToGroup` behavior.
- `removeUserFromGroup(@Nonnull UUID uuid, @Nonnull String group)`
  - Executes `removeUserFromGroup` behavior.
- `setVirtualGroups(@Nonnull Map<String, Set<String>> virtualGroups)`
  - Executes `setVirtualGroups` behavior.
- `getGroupsForUser(@Nonnull UUID uuid)`
  - Executes `getGroupsForUser` behavior.
- `hasPermission(@Nonnull UUID uuid, @Nonnull String id)`
  - Executes `hasPermission` behavior.
- `hasPermission(@Nonnull UUID uuid, @Nonnull String id, boolean def)`
  - Executes `hasPermission` behavior.
- `hasPermission(@Nullable Set<String> nodes, @Nonnull String id)`
  - Executes `hasPermission` behavior.

## Notes
- No additional notes.
