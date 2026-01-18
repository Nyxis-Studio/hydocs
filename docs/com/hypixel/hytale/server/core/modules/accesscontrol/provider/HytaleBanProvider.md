# HytaleBanProvider

## Overview
- Documentation for `HytaleBanProvider`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.accesscontrol.provider`.

## Constructors
- `HytaleBanProvider()`
  - Creates a `HytaleBanProvider` instance.

## Methods
- `getDisconnectReason(UUID uuid)`
  - Executes `getDisconnectReason` behavior.
- `read(@Nonnull BufferedReader fileReader)`
  - Executes `read` behavior.
- `write(@Nonnull BufferedWriter fileWriter)`
  - Executes `write` behavior.
- `create(@Nonnull BufferedWriter fileWriter)`
  - Executes `create` behavior.
- `hasBan(UUID uuid)`
  - Executes `hasBan` behavior.
- `modify(@Nonnull Function<Map<UUID, Ban>, Boolean> function)`
  - Executes `modify` behavior.

## Notes
- No additional notes.
