**Source Hash:** `26efe6551b47e9e5ef3036615942a9da3d27470c049a120df1d07e2d95afca62`

# EntityRefCollisionProvider

## Overview

## Constructor Descriptions
- `EntityRefCollisionProvider()`
  - Creates a `EntityRefCollisionProvider` instance.

## Method Descriptions
- `getCount()`: Add description.
  - Executes `getCount` behavior.
- `getContact(int i)`: Add description.
  - Executes `getContact` behavior.
- `clear()`: Add description.
  - Executes `clear` behavior.
- `computeNearest(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Box entityBoundingBox, @Nonnull Vector3d pos, @Nonnull Vector3d dir, @Nullable Ref<EntityStore> ignoreSelf, @Nullable Ref<EntityStore> ignore)`: Add description.
  - Executes `computeNearest` behavior.
- `computeNearest(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Vector3d pos, @Nonnull Vector3d dir, @Nonnull Box boundingBox, double radius, @Nonnull BiPredicate<Ref<EntityStore>, CommandBuffer<EntityStore>> entityFilter, @Nullable Ref<EntityStore> ignoreSelf, @Nullable Ref<EntityStore> ignoreOther)`: Add description.
  - Executes `computeNearest` behavior.
- `iterateEntitiesInSphere(@Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull Vector3d pos, @Nonnull Vector3d dir, @Nonnull Box boundingBox, double radius, @Nonnull TriConsumer<EntityRefCollisionProvider, Ref<EntityStore>, CommandBuffer<EntityStore>> consumer)`: Add description.
  - Executes `iterateEntitiesInSphere` behavior.
- `setContact(@Nonnull Ref<EntityStore> ref, @Nonnull String detailName)`: Add description.
  - Executes `setContact` behavior.
- `isColliding(@Nonnull Ref<EntityStore> ref, @Nonnull Vector2d minMax, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `isColliding` behavior.
- `clearRefs()`: Add description.
  - Executes `clearRefs` behavior.
- `defaultEntityFilter(@Nonnull Ref<EntityStore> entity, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `defaultEntityFilter` behavior.
- `acceptNearestIgnore(@Nonnull Ref<EntityStore> entity, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `acceptNearestIgnore` behavior.

## Notes
- No additional notes.
