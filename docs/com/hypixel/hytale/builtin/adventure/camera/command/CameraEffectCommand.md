**Source Hash:** `f8e1996453eeef2c7d1516704f7e5f592a82cbb04e6cda13520bfe8e9539689d`
**Last Updated:** `2026-01-18T17:26:43-03:00`

## Overview
Command collection for camera shake debugging and testing. Provides `damage` and `debug` subcommands.

## Field Descriptions
- `CAMERA_EFFECT_ARGUMENT_TYPE`: Asset argument type for camera effects.

## Constructor Descriptions
- `CameraEffectCommand()`: Registers the `damage` and `debug` subcommands.

## Method Descriptions
- `none()`: Behavior lives in subcommands.

## Usage Notes
- Subcommands require asset-backed arguments for `CameraEffect` and `DamageCause`.

## Examples
```java
commandRegistry.registerCommand(new CameraEffectCommand());
```

---

## Overview
Triggers a damage event that can invoke camera shake effects. Optionally selects a specific camera effect asset.

## Field Descriptions
- `DAMAGE_CAUSE_ARGUMENT_TYPE`: Asset argument type for damage causes.
- `effectArg`: Optional camera effect argument.
- `causeArg`: Required damage cause argument.
- `damageArg`: Required damage amount argument.

## Constructor Descriptions
- `DamageCommand()`: Configures arguments for damage simulation.

## Method Descriptions
- `execute(CommandContext context, Ref<EntityStore> sourceRef, Ref<EntityStore> ref, PlayerRef playerRef, World world, Store<EntityStore> store)`: Builds a `Damage` event, injects camera effect metadata when provided, executes damage, and sends a confirmation message.

## Usage Notes
- Uses `DamageSystems.executeDamage` to apply damage to the target.

## Examples
```java
// /camshake damage <cause> <amount> [effect]
```

---

## Overview
Directly sends a camera shake packet to the target player. Useful for manual testing of intensity values.

## Field Descriptions
- `MESSAGE_SUCCESS`: Translation key used for success feedback.
- `effectArg`: Required camera effect argument.
- `intensityArg`: Required intensity argument.

## Constructor Descriptions
- `DebugCommand()`: Configures arguments for direct camera shake testing.

## Method Descriptions
- `execute(CommandContext context, Ref<EntityStore> sourceRef, Ref<EntityStore> ref, PlayerRef playerRef, World world, Store<EntityStore> store)`: Sends a camera shake packet to the target and returns a confirmation message.

## Usage Notes
- Writes packets with `writeNoCache` on the player packet handler.

## Examples
```java
// /camshake debug <effect> <intensity>
```
