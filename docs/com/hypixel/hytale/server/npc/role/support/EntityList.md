# EntityList

## Overview
- Documentation for `EntityList`.
- Declared as a class in `com.hypixel.hytale.server.npc.role.support`.

## Constructors
- `EntityList(@Nullable BucketItemPool<Ref<EntityStore>> holderPool, @Nonnull BiPredicate<Ref<EntityStore>, ComponentAccessor<EntityStore>> validator)`
  - Creates a `EntityList` instance.

## Methods
- `getMaxDistanceUnsorted()`
  - Executes `getMaxDistanceUnsorted` behavior.
- `getMaxDistanceSorted()`
  - Executes `getMaxDistanceSorted` behavior.
- `getMaxDistanceAvoidance()`
  - Executes `getMaxDistanceAvoidance` behavior.
- `getSearchRadius()`
  - Executes `getSearchRadius` behavior.
- `getBucketRanges()`
  - Executes `getBucketRanges` behavior.
- `reset()`
  - Executes `reset` behavior.
- `requireDistanceSorted(int value)`
  - Executes `requireDistanceSorted` behavior.
- `requireDistanceUnsorted(int value)`
  - Executes `requireDistanceUnsorted` behavior.
- `requireDistanceAvoidance(int value)`
  - Executes `requireDistanceAvoidance` behavior.
- `finalizeConfiguration()`
  - Executes `finalizeConfiguration` behavior.
- `add(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d parentPosition, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `add` behavior.
- `forEachEntity(@Nonnull DoubleQuadObjectConsumer<Ref<EntityStore>, T, U, V> consumer, T t, U u, V v, double d, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `forEachEntity` behavior.
- `forEachEntityUnordered(double maxDistance, @Nonnull QuadPredicate<Ref<EntityStore>, T, U, ComponentAccessor<EntityStore>> predicate, @Nonnull QuadConsumer<Ref<EntityStore>, T, V, R> consumer, T t, U u, V v, R r, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `forEachEntityUnordered` behavior.
- `forEachEntityAvoidance(@Nonnull Set<Ref<EntityStore>> ignoredEntitiesForAvoidance, @Nonnull TriConsumer<Ref<EntityStore>, T, CommandBuffer<EntityStore>> consumer, T t, CommandBuffer<EntityStore> commandBuffer)`
  - Executes `forEachEntityAvoidance` behavior.
- `forEachEntityAvoidance(@Nonnull Set<Ref<EntityStore>> ignoredEntitiesForAvoidance, @Nonnull QuadConsumer<Ref<EntityStore>, T, U, CommandBuffer<EntityStore>> consumer, T t, U u, CommandBuffer<EntityStore> commandBuffer)`
  - Executes `forEachEntityAvoidance` behavior.
- `countEntitiesInRange(double minRange, double maxRange, int maxCount, @Nonnull QuadPredicate<S, Ref<EntityStore>, T, ComponentAccessor<EntityStore>> filter, S s, T t, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `countEntitiesInRange` behavior.
- `getClosestEntityInRange(double minRange, double maxRange, @Nonnull Predicate<Ref<EntityStore>> filter, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getClosestEntityInRange` behavior.
- `getClosestEntityInRange(@Nullable Ref<EntityStore> ignoredEntityReference, double minRange, double maxRange, @Nonnull QuadPredicate<S, Ref<EntityStore>, Role, T> filter, Role role, S s, T t, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getClosestEntityInRange` behavior.
- `getClosestEntityInRangeProjected(@Nonnull Ref<EntityStore> parentRef, @Nullable Ref<EntityStore> ignoredEntityReference, @Nonnull MotionController motionController, double minRange, double maxRange, @Nonnull QuadPredicate<S, Ref<EntityStore>, Role, T> filter, Role role, S s, T t, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getClosestEntityInRangeProjected` behavior.
- `testAnyEntity(double maxDistance, @Nonnull QuadObjectDoublePredicate<S, Ref<EntityStore>, T, ComponentAccessor<EntityStore>> predicate, S s, T t, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `testAnyEntity` behavior.
- `testAnyEntityDistanceSquared(double maxDistanceSquared, @Nonnull QuadObjectDoublePredicate<S, Ref<EntityStore>, T, ComponentAccessor<EntityStore>> predicate, S s, T t, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `testAnyEntityDistanceSquared` behavior.
- `testAnyEntityDistanceSquared(double maxDistanceSquared, @Nonnull QuadObjectDoublePredicate<S, Ref<EntityStore>, T, ComponentAccessor<EntityStore>> predicate, S s, T t, double d, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `testAnyEntityDistanceSquared` behavior.
- `validateEntityRef(@Nonnull BucketItem<Ref<EntityStore>> holder, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `validateEntityRef` behavior.

## Notes
- No additional notes.
