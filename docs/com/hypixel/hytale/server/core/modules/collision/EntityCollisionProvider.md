# EntityCollisionProvider

## Overview
- Documentation for `EntityCollisionProvider`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.collision`.

## Constructors
- `EntityCollisionProvider()`
  - Creates a `EntityCollisionProvider` instance.

## Methods
- `getCount()`
  - Executes `getCount` behavior.
- `getContact(int index)`
  - Executes `getContact` behavior.
- `clear()`
  - Executes `clear` behavior.
- `computeNearest(@Nonnull Box entityBoundingBox, @Nonnull Vector3d pos, @Nonnull Vector3d dir, @Nullable Ref<EntityStore> ignoreSelf, @Nullable Ref<EntityStore> ignore, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `computeNearest` behavior.
- `computeNearest(@Nonnull Vector3d pos, @Nonnull Vector3d dir, @Nonnull Box boundingBox, double radius, @Nonnull BiPredicate<Ref<EntityStore>, ComponentAccessor<EntityStore>> entityFilter, @Nullable Ref<EntityStore> ignoreSelf, @Nullable Ref<EntityStore> ignoreOther, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `computeNearest` behavior.
- `iterateEntitiesInSphere(@Nonnull Vector3d pos, @Nonnull Vector3d dir, @Nonnull Box boundingBox, double radius, @Nonnull BiConsumer<Ref<EntityStore>, EntityCollisionProvider> consumer, @Nonnull BiConsumer<Ref<EntityStore>, EntityCollisionProvider> consumerPlayer, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `iterateEntitiesInSphere` behavior.
- `setContact(@Nonnull Entity entity)`
  - Executes `setContact` behavior.
- `isColliding(@Nonnull Ref<EntityStore> ref, @Nonnull Vector2d minMax, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `isColliding` behavior.
- `clearRefs()`
  - Executes `clearRefs` behavior.
- `defaultEntityFilter(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `defaultEntityFilter` behavior.
- `acceptNearestIgnore(@Nonnull Ref<EntityStore> ref, @Nonnull EntityCollisionProvider collisionProvider, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `acceptNearestIgnore` behavior.

## Notes
- No additional notes.
