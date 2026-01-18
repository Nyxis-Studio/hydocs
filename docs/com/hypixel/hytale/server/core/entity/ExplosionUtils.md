# ExplosionUtils

## Overview
- Documentation for `ExplosionUtils`.
- Declared as a class in `com.hypixel.hytale.server.core.entity`.

## Constructors
- None.

## Methods
- `performExplosion(@Nonnull Damage.Source damageSource, @Nonnull Vector3d position, @Nonnull ExplosionConfig config, @Nullable Ref<EntityStore> ignoreRef, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull ComponentAccessor<ChunkStore> chunkStore)`
  - Executes `performExplosion` behavior.
- `processTargetBlocks(@Nonnull Vector3d position, @Nonnull ExplosionConfig config, @Nullable Ref<EntityStore> ignoreRef, @Nonnull Set<Ref<EntityStore>> targetRefs, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull ComponentAccessor<ChunkStore> chunkStore)`
  - Executes `processTargetBlocks` behavior.
- `isValidTargetBlock(int blockTypeId, boolean damageBlocks)`
  - Executes `isValidTargetBlock` behavior.
- `collectPotentialTargets(@Nonnull Set<Ref<EntityStore>> targetRefs, @Nonnull List<Ref<EntityStore>> potentialTargetRefs, @Nonnull Vector3d startPosition, @Nonnull Vector3d endPosition, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `collectPotentialTargets` behavior.
- `processPotentialEntity(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d startPosition, @Nonnull Vector3d endPosition, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `processPotentialEntity` behavior.
- `calculateBlockDamageScale(float distance, float radius, float fallOff)`
  - Executes `calculateBlockDamageScale` behavior.
- `processTargetEntities(@Nonnull ExplosionConfig config, @Nonnull Vector3d position, @Nonnull Damage.Source damageSource, @Nullable Ref<EntityStore> ignoreRef, @Nonnull Set<Ref<EntityStore>> targetRefs, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `processTargetEntities` behavior.
- `processTargetEntity(@Nonnull ExplosionConfig config, @Nonnull Ref<EntityStore> targetRef, @Nonnull Vector3d position, @Nonnull Damage.Source damageSource, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `processTargetEntity` behavior.

## Notes
- No additional notes.
