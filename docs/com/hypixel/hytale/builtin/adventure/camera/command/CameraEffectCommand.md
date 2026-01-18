# CameraEffectCommand

**Overview**
Command collection for camera shake debugging and testing.
Provides subcommands to trigger shake effects and damage-based shakes.

**Constructors**
- `CameraEffectCommand()`: registers `damage` and `debug` subcommands.

**Methods**
- No direct public methods; behavior lives in subcommands.

**Notes**
- Uses asset-backed arguments for `CameraEffect` and `DamageCause`.

---

# CameraEffectCommand.DamageCommand

**Overview**
Triggers a damage event that can invoke camera shake effects.
Optionally selects a specific camera effect asset.

**Constructors**
- `DamageCommand()`: configures arguments and descriptions.

**Methods**
- `execute(CommandContext context, Ref<EntityStore> sourceRef, Ref<EntityStore> ref, PlayerRef playerRef, World world, Store<EntityStore> store)`: builds and dispatches a `Damage` event with optional camera effect metadata.

**Notes**
- Uses `DamageSystems.executeDamage` to apply damage.

---

# CameraEffectCommand.DebugCommand

**Overview**
Directly sends a camera shake packet to the target player.
Useful for manual testing of intensity values.

**Constructors**
- `DebugCommand()`: configures arguments and descriptions.

**Methods**
- `execute(CommandContext context, Ref<EntityStore> sourceRef, Ref<EntityStore> ref, PlayerRef playerRef, World world, Store<EntityStore> store)`: sends a camera shake packet and confirmation message.

**Notes**
- Writes packets with `writeNoCache` on the player packet handler.
