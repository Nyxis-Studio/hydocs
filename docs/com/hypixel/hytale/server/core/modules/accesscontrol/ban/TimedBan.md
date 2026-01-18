# TimedBan

## Overview
- Documentation for `TimedBan`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.accesscontrol.ban`.

## Constructors
- `TimedBan(target, by, timestamp, expiresOn, reason)`
  - Creates a `TimedBan` instance.
- `TimedBan(UUID target, UUID by, Instant timestamp, Instant expiresOn, String reason)`
  - Creates a `TimedBan` instance.

## Methods
- `fromJsonObject(@Nonnull JsonObject object)`
  - Executes `fromJsonObject` behavior.
- `isInEffect()`
  - Executes `isInEffect` behavior.
- `getType()`
  - Executes `getType` behavior.
- `getExpiresOn()`
  - Executes `getExpiresOn` behavior.
- `getDisconnectReason(UUID uuid)`
  - Executes `getDisconnectReason` behavior.
- `toJsonObject()`
  - Executes `toJsonObject` behavior.

## Notes
- No additional notes.
