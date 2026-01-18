**Source Hash:** `05a7914ea55711acd3f26a61106baf84d506f6ea37b90e3dee1a0054d1f6390e`

# PermissionsModule

## Overview

## Constructor Descriptions
- `PermissionsModule(@Nonnull JavaPluginInit init)`
  - Creates a `PermissionsModule` instance.

## Method Descriptions
- `get()`: Add description.
  - Executes `get` behavior.
- `setup()`: Add description.
  - Executes `setup` behavior.
- `start()`: Add description.
  - Executes `start` behavior.
- `addProvider(@Nonnull PermissionProvider permissionProvider)`: Add description.
  - Executes `addProvider` behavior.
- `removeProvider(@Nonnull PermissionProvider provider)`: Add description.
  - Executes `removeProvider` behavior.
- `getProviders()`: Add description.
  - Executes `getProviders` behavior.
- `getFirstPermissionProvider()`: Add description.
  - Executes `getFirstPermissionProvider` behavior.
- `areProvidersTampered()`: Add description.
  - Executes `areProvidersTampered` behavior.
- `addUserPermission(@Nonnull UUID uuid, @Nonnull Set<String> permissions)`: Add description.
  - Executes `addUserPermission` behavior.
- `removeUserPermission(@Nonnull UUID uuid, @Nonnull Set<String> permissions)`: Add description.
  - Executes `removeUserPermission` behavior.
- `addGroupPermission(@Nonnull String group, @Nonnull Set<String> permissions)`: Add description.
  - Executes `addGroupPermission` behavior.
- `removeGroupPermission(@Nonnull String group, @Nonnull Set<String> permissions)`: Add description.
  - Executes `removeGroupPermission` behavior.
- `addUserToGroup(@Nonnull UUID uuid, @Nonnull String group)`: Add description.
  - Executes `addUserToGroup` behavior.
- `removeUserFromGroup(@Nonnull UUID uuid, @Nonnull String group)`: Add description.
  - Executes `removeUserFromGroup` behavior.
- `setVirtualGroups(@Nonnull Map<String, Set<String>> virtualGroups)`: Add description.
  - Executes `setVirtualGroups` behavior.
- `getGroupsForUser(@Nonnull UUID uuid)`: Add description.
  - Executes `getGroupsForUser` behavior.
- `hasPermission(@Nonnull UUID uuid, @Nonnull String id)`: Add description.
  - Executes `hasPermission` behavior.
- `hasPermission(@Nonnull UUID uuid, @Nonnull String id, boolean def)`: Add description.
  - Executes `hasPermission` behavior.
- `hasPermission(@Nullable Set<String> nodes, @Nonnull String id)`: Add description.
  - Executes `hasPermission` behavior.

## Notes
- No additional notes.
