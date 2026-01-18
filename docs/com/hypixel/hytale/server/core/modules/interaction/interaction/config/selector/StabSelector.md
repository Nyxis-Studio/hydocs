# StabSelector

## Overview
- Documentation for `StabSelector`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.interaction.interaction.config.selector`.

## Constructors
- `StabSelector()`
  - Creates a `StabSelector` instance.

## Methods
- `newSelector()`
  - Executes `newSelector` behavior.
- `tick(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Ref<EntityStore> attacker, float time, float runTime)`
  - Executes `tick` behavior.
- `selectTargetEntities(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Ref<EntityStore> attacker, @Nonnull BiConsumer<Ref<EntityStore>, Vector4d> consumer, Predicate<Ref<EntityStore>> filter)`
  - Executes `selectTargetEntities` behavior.
- `selectTargetBlocks(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Ref<EntityStore> attacker, @Nonnull TriIntConsumer consumer)`
  - Executes `selectTargetBlocks` behavior.

## Notes
- No additional notes.
