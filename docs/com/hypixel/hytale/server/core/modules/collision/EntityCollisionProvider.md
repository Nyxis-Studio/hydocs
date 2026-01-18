**Source Hash:** `655088ad3f192aac1f77e0bc8e2a1ca19309293fc875876247ab1974ed799a40`

# EntityCollisionProvider

## Overview

## Constructor Descriptions
- `EntityCollisionProvider()`
  - Creates a `EntityCollisionProvider` instance.

## Method Descriptions
- `getCount()`: Add description.
  - Executes `getCount` behavior.
- `getContact(int index)`: Add description.
  - Executes `getContact` behavior.
- `clear()`: Add description.
  - Executes `clear` behavior.
- `computeNearest(@Nonnull Box entityBoundingBox, @Nonnull Vector3d pos, @Nonnull Vector3d dir, @Nullable Ref<EntityStore> ignoreSelf, @Nullable Ref<EntityStore> ignore, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `computeNearest` behavior.
- `computeNearest(@Nonnull Vector3d pos, @Nonnull Vector3d dir, @Nonnull Box boundingBox, double radius, @Nonnull BiPredicate<Ref<EntityStore>, ComponentAccessor<EntityStore>> entityFilter, @Nullable Ref<EntityStore> ignoreSelf, @Nullable Ref<EntityStore> ignoreOther, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `computeNearest` behavior.
- `iterateEntitiesInSphere(@Nonnull Vector3d pos, @Nonnull Vector3d dir, @Nonnull Box boundingBox, double radius, @Nonnull BiConsumer<Ref<EntityStore>, EntityCollisionProvider> consumer, @Nonnull BiConsumer<Ref<EntityStore>, EntityCollisionProvider> consumerPlayer, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `iterateEntitiesInSphere` behavior.
- `setContact(@Nonnull Entity entity)`: Add description.
  - Executes `setContact` behavior.
- `isColliding(@Nonnull Ref<EntityStore> ref, @Nonnull Vector2d minMax, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `isColliding` behavior.
- `clearRefs()`: Add description.
  - Executes `clearRefs` behavior.
- `defaultEntityFilter(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `defaultEntityFilter` behavior.
- `acceptNearestIgnore(@Nonnull Ref<EntityStore> ref, @Nonnull EntityCollisionProvider collisionProvider, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `acceptNearestIgnore` behavior.

## Notes
- No additional notes.
