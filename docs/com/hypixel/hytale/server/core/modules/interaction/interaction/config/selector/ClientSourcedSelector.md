**Source Hash:** `73dc57954a8a725bb70776705b2a6177e5e1f8c281bd953bcf625b96f0ab8f77`

# ClientSourcedSelector

## Overview

## Constructor Descriptions
- `ClientSourcedSelector(Selector parent, InteractionContext context)`
  - Creates a `ClientSourcedSelector` instance.

## Method Descriptions
- `tick(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Ref<EntityStore> ref, float time, float runTime)`: Add description.
  - Executes `tick` behavior.
- `selectTargetEntities(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Ref<EntityStore> ref, @Nonnull BiConsumer<Ref<EntityStore>, Vector4d> consumer, Predicate<Ref<EntityStore>> filter)`: Add description.
  - Executes `selectTargetEntities` behavior.
- `selectTargetBlocks(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Ref<EntityStore> ref, @Nonnull TriIntConsumer consumer)`: Add description.
  - Executes `selectTargetBlocks` behavior.

## Notes
- No additional notes.
