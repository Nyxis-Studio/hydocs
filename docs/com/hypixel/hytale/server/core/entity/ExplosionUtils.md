**Source Hash:** `4b53e71f8eda3c3abbb1fef6c715391f116fd15ff55ad1ee682899b1bccb6bbd`

# ExplosionUtils

## Overview

## Constructor Descriptions
- `none()`: No documented methods.

## Method Descriptions
- `performExplosion(@Nonnull Damage.Source damageSource, @Nonnull Vector3d position, @Nonnull ExplosionConfig config, @Nullable Ref<EntityStore> ignoreRef, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull ComponentAccessor<ChunkStore> chunkStore)`: Add description.
  - Executes `performExplosion` behavior.
- `processTargetBlocks(@Nonnull Vector3d position, @Nonnull ExplosionConfig config, @Nullable Ref<EntityStore> ignoreRef, @Nonnull Set<Ref<EntityStore>> targetRefs, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull ComponentAccessor<ChunkStore> chunkStore)`: Add description.
  - Executes `processTargetBlocks` behavior.
- `isValidTargetBlock(int blockTypeId, boolean damageBlocks)`: Add description.
  - Executes `isValidTargetBlock` behavior.
- `collectPotentialTargets(@Nonnull Set<Ref<EntityStore>> targetRefs, @Nonnull List<Ref<EntityStore>> potentialTargetRefs, @Nonnull Vector3d startPosition, @Nonnull Vector3d endPosition, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `collectPotentialTargets` behavior.
- `processPotentialEntity(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d startPosition, @Nonnull Vector3d endPosition, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `processPotentialEntity` behavior.
- `calculateBlockDamageScale(float distance, float radius, float fallOff)`: Add description.
  - Executes `calculateBlockDamageScale` behavior.
- `processTargetEntities(@Nonnull ExplosionConfig config, @Nonnull Vector3d position, @Nonnull Damage.Source damageSource, @Nullable Ref<EntityStore> ignoreRef, @Nonnull Set<Ref<EntityStore>> targetRefs, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `processTargetEntities` behavior.
- `processTargetEntity(@Nonnull ExplosionConfig config, @Nonnull Ref<EntityStore> targetRef, @Nonnull Vector3d position, @Nonnull Damage.Source damageSource, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `processTargetEntity` behavior.

## Notes
- No additional notes.
