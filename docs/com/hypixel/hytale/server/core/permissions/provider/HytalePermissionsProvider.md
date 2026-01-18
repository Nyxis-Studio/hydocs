# HytalePermissionsProvider

## Overview
- Documentation for `HytalePermissionsProvider`.
- Declared as a class in `com.hypixel.hytale.server.core.permissions.provider`.

## Constructors
- `HytalePermissionsProvider()`
  - Creates a `HytalePermissionsProvider` instance.

## Methods
- `getName()`
  - Executes `getName` behavior.
- `addUserPermissions(@Nonnull UUID uuid, @Nonnull Set<String> permissions)`
  - Executes `addUserPermissions` behavior.
- `removeUserPermissions(@Nonnull UUID uuid, @Nonnull Set<String> permissions)`
  - Executes `removeUserPermissions` behavior.
- `getUserPermissions(@Nonnull UUID uuid)`
  - Executes `getUserPermissions` behavior.
- `addGroupPermissions(@Nonnull String group, @Nonnull Set<String> permissions)`
  - Executes `addGroupPermissions` behavior.
- `removeGroupPermissions(@Nonnull String group, @Nonnull Set<String> permissions)`
  - Executes `removeGroupPermissions` behavior.
- `getGroupPermissions(@Nonnull String group)`
  - Executes `getGroupPermissions` behavior.
- `addUserToGroup(@Nonnull UUID uuid, @Nonnull String group)`
  - Executes `addUserToGroup` behavior.
- `removeUserFromGroup(@Nonnull UUID uuid, @Nonnull String group)`
  - Executes `removeUserFromGroup` behavior.
- `getGroupsForUser(@Nonnull UUID uuid)`
  - Executes `getGroupsForUser` behavior.
- `read(@Nonnull BufferedReader fileReader)`
  - Executes `read` behavior.
- `write(@Nonnull BufferedWriter fileWriter)`
  - Executes `write` behavior.
- `create(@Nonnull BufferedWriter fileWriter)`
  - Executes `create` behavior.

## Notes
- No additional notes.
