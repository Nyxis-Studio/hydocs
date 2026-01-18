# ProjectileConfig

## Overview
- Documentation for `ProjectileConfig`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ProjectileConfig()`
  - Creates a `ProjectileConfig` instance.
- `ProjectileConfig(@Nullable PhysicsConfig physicsConfig, @Nullable Model model, double launchForce, @Nullable Vector3f spawnOffset, @Nullable Direction rotationOffset, @Nullable Map<InteractionType, Integer> interactions, int launchLocalSoundEventIndex, int projectileSoundEventIndex)`
  - Creates a `ProjectileConfig` instance.
- `ProjectileConfig(@Nonnull ProjectileConfig other)`
  - Creates a `ProjectileConfig` instance.

## Methods
- `deserialize(@Nonnull ByteBuf buf, int offset)`
  - Executes `deserialize` behavior.
- `computeBytesConsumed(@Nonnull ByteBuf buf, int offset)`
  - Executes `computeBytesConsumed` behavior.
- `serialize(@Nonnull ByteBuf buf)`
  - Executes `serialize` behavior.
- `computeSize()`
  - Executes `computeSize` behavior.
- `validateStructure(@Nonnull ByteBuf buffer, int offset)`
  - Executes `validateStructure` behavior.
- `clone()`
  - Executes `clone` behavior.
- `equals(Object obj)`
  - Executes `equals` behavior.
- `hashCode()`
  - Executes `hashCode` behavior.

## Notes
- No additional notes.
