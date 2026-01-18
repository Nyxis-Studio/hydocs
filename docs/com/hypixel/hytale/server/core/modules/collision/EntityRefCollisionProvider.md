# EntityRefCollisionProvider

## Overview
- Documentation for `EntityRefCollisionProvider`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.collision`.

## Constructors
- `EntityRefCollisionProvider()`
  - Creates a `EntityRefCollisionProvider` instance.

## Methods
- `getCount()`
  - Executes `getCount` behavior.
- `getContact(int i)`
  - Executes `getContact` behavior.
- `clear()`
  - Executes `clear` behavior.
- `computeNearest(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Box entityBoundingBox, @Nonnull Vector3d pos, @Nonnull Vector3d dir, @Nullable Ref<EntityStore> ignoreSelf, @Nullable Ref<EntityStore> ignore)`
  - Executes `computeNearest` behavior.
- `computeNearest(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Vector3d pos, @Nonnull Vector3d dir, @Nonnull Box boundingBox, double radius, @Nonnull BiPredicate<Ref<EntityStore>, CommandBuffer<EntityStore>> entityFilter, @Nullable Ref<EntityStore> ignoreSelf, @Nullable Ref<EntityStore> ignoreOther)`
  - Executes `computeNearest` behavior.
- `iterateEntitiesInSphere(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Vector3d pos, @Nonnull Vector3d dir, @Nonnull Box boundingBox, double radius, @Nonnull TriConsumer<EntityRefCollisionProvider, Ref<EntityStore>, CommandBuffer<EntityStore>> consumer)`
  - Executes `iterateEntitiesInSphere` behavior.
- `setContact(@Nonnull Ref<EntityStore> ref, @Nonnull String detailName)`
  - Executes `setContact` behavior.
- `isColliding(@Nonnull Ref<EntityStore> ref, @Nonnull Vector2d minMax, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `isColliding` behavior.
- `clearRefs()`
  - Executes `clearRefs` behavior.
- `defaultEntityFilter(@Nonnull Ref<EntityStore> entity, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `defaultEntityFilter` behavior.
- `acceptNearestIgnore(@Nonnull Ref<EntityStore> entity, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `acceptNearestIgnore` behavior.

## Notes
- No additional notes.
