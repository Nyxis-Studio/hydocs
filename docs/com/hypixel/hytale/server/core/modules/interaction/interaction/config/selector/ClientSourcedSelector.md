# ClientSourcedSelector

## Overview
- Documentation for `ClientSourcedSelector`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.interaction.interaction.config.selector`.

## Constructors
- `ClientSourcedSelector(Selector parent, InteractionContext context)`
  - Creates a `ClientSourcedSelector` instance.

## Methods
- `tick(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Ref<EntityStore> ref, float time, float runTime)`
  - Executes `tick` behavior.
- `selectTargetEntities(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Ref<EntityStore> ref, @Nonnull BiConsumer<Ref<EntityStore>, Vector4d> consumer, Predicate<Ref<EntityStore>> filter)`
  - Executes `selectTargetEntities` behavior.
- `selectTargetBlocks(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Ref<EntityStore> ref, @Nonnull TriIntConsumer consumer)`
  - Executes `selectTargetBlocks` behavior.

## Notes
- No additional notes.
