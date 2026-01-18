# Selector

## Overview
- Documentation for `Selector`.
- Declared as a interface in `com.hypixel.hytale.server.core.modules.interaction.interaction.config.selector`.

## Constructors
- None.

## Methods
- `selectNearbyBlocks(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Ref<EntityStore> attackerRef, double range, @Nonnull TriIntConsumer consumer)`
  - Executes `selectNearbyBlocks` behavior.
- `selectNearbyBlocks(@Nonnull Vector3d position, double range, @Nonnull TriIntConsumer consumer)`
  - Executes `selectNearbyBlocks` behavior.
- `selectNearbyBlocks(double xPos, double yPos, double zPos, double range, @Nonnull TriIntConsumer consumer)`
  - Executes `selectNearbyBlocks` behavior.
- `selectNearbyEntities(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Ref<EntityStore> attacker, double range, @Nonnull Consumer<Ref<EntityStore>> consumer, @Nonnull Predicate<Ref<EntityStore>> filter)`
  - Executes `selectNearbyEntities` behavior.
- `selectNearbyEntities(@Nonnull ComponentAccessor<EntityStore> componentAccessor, @Nonnull Vector3d position, double range, @Nonnull Consumer<Ref<EntityStore>> consumer, @Nullable Predicate<Ref<EntityStore>> filter)`
  - Executes `selectNearbyEntities` behavior.
- `tick(@Nonnull CommandBuffer<EntityStore> var1, @Nonnull Ref<EntityStore> var2, float var3, float var4)`
  - Executes `tick` behavior.
- `selectTargetEntities(@Nonnull CommandBuffer<EntityStore> var1, @Nonnull Ref<EntityStore> var2, BiConsumer<Ref<EntityStore>, Vector4d> var3, Predicate<Ref<EntityStore>> var4)`
  - Executes `selectTargetEntities` behavior.
- `selectTargetBlocks(@Nonnull CommandBuffer<EntityStore> var1, @Nonnull Ref<EntityStore> var2, @Nonnull TriIntConsumer var3)`
  - Executes `selectTargetBlocks` behavior.

## Notes
- No additional notes.
