# AOECylinderSelector

## Overview
- Documentation for `AOECylinderSelector`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.interaction.interaction.config.selector`.

## Constructors
- `AOECylinderSelector(this.range, this.height, this.getOffset()`
  - Creates a `AOECylinderSelector` instance.

## Methods
- `newSelector()`
  - Executes `newSelector` behavior.
- `tick(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Ref<EntityStore> ref, float time, float runTime)`
  - Executes `tick` behavior.
- `selectTargetEntities(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Ref<EntityStore> ref, @Nonnull BiConsumer<Ref<EntityStore>, Vector4d> consumer, @Nullable Predicate<Ref<EntityStore>> filter)`
  - Executes `selectTargetEntities` behavior.
- `selectTargetBlocks(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Ref<EntityStore> ref, @Nonnull TriIntConsumer consumer)`
  - Executes `selectTargetBlocks` behavior.

## Notes
- No additional notes.
