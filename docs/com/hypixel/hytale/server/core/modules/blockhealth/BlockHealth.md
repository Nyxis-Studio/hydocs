# BlockHealth

## Overview
- Documentation for `BlockHealth`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.blockhealth`.

## Constructors
- `BlockHealth(1.0f, Instant.MIN)`
  - Creates a `BlockHealth` instance.
- `BlockHealth()`
  - Creates a `BlockHealth` instance.
- `BlockHealth(float health, Instant lastDamageGameTime)`
  - Creates a `BlockHealth` instance.
- `BlockHealth(this.health, this.lastDamageGameTime)`
  - Creates a `BlockHealth` instance.

## Methods
- `setHealth(float health)`
  - Executes `setHealth` behavior.
- `setLastDamageGameTime(Instant lastDamageGameTime)`
  - Executes `setLastDamageGameTime` behavior.
- `getHealth()`
  - Executes `getHealth` behavior.
- `getLastDamageGameTime()`
  - Executes `getLastDamageGameTime` behavior.
- `isDestroyed()`
  - Executes `isDestroyed` behavior.
- `isFullHealth()`
  - Executes `isFullHealth` behavior.
- `deserialize(@Nonnull ByteBuf buf, byte version)`
  - Executes `deserialize` behavior.
- `serialize(@Nonnull ByteBuf buf)`
  - Executes `serialize` behavior.
- `clone()`
  - Executes `clone` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
