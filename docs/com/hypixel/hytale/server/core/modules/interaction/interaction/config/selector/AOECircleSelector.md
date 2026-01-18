# AOECircleSelector

## Overview
- Documentation for `AOECircleSelector`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.interaction.interaction.config.selector`.

## Constructors
- `AOECircleSelector(this.range, this.getOffset()`
  - Creates a `AOECircleSelector` instance.

## Methods
- `newSelector()`
  - Executes `newSelector` behavior.
- `getOffset()`
  - Executes `getOffset` behavior.
- `selectTargetPosition(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Ref<EntityStore> attackerRef)`
  - Executes `selectTargetPosition` behavior.
- `tick(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Ref<EntityStore> ref, float time, float runTime)`
  - Executes `tick` behavior.
- `selectTargetEntities(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Ref<EntityStore> attacker, @Nonnull BiConsumer<Ref<EntityStore>, Vector4d> consumer, Predicate<Ref<EntityStore>> filter)`
  - Executes `selectTargetEntities` behavior.
- `selectTargetBlocks(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Ref<EntityStore> attacker, @Nonnull TriIntConsumer consumer)`
  - Executes `selectTargetBlocks` behavior.

## Notes
- No additional notes.
