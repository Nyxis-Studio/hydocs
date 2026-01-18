**Source Hash:** `46a637225adb5d5d44b4c773ee2715f45a1b4762809f5ac235696e834ef73d63`

# EntityList

## Overview

## Constructor Descriptions
- `EntityList(@Nullable BucketItemPool<Ref<EntityStore>> holderPool, @Nonnull BiPredicate<Ref<EntityStore>, ComponentAccessor<EntityStore>> validator)`
  - Creates a `EntityList` instance.

## Method Descriptions
- `getMaxDistanceUnsorted()`: Add description.
  - Executes `getMaxDistanceUnsorted` behavior.
- `getMaxDistanceSorted()`: Add description.
  - Executes `getMaxDistanceSorted` behavior.
- `getMaxDistanceAvoidance()`: Add description.
  - Executes `getMaxDistanceAvoidance` behavior.
- `getSearchRadius()`: Add description.
  - Executes `getSearchRadius` behavior.
- `getBucketRanges()`: Add description.
  - Executes `getBucketRanges` behavior.
- `reset()`: Add description.
  - Executes `reset` behavior.
- `requireDistanceSorted(int value)`: Add description.
  - Executes `requireDistanceSorted` behavior.
- `requireDistanceUnsorted(int value)`: Add description.
  - Executes `requireDistanceUnsorted` behavior.
- `requireDistanceAvoidance(int value)`: Add description.
  - Executes `requireDistanceAvoidance` behavior.
- `finalizeConfiguration()`: Add description.
  - Executes `finalizeConfiguration` behavior.
- `add(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d parentPosition, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `add` behavior.
- `forEachEntity(@Nonnull DoubleQuadObjectConsumer<Ref<EntityStore>, T, U, V> consumer, T t, U u, V v, double d, ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `forEachEntity` behavior.
- `forEachEntityUnordered(double maxDistance, @Nonnull QuadPredicate<Ref<EntityStore>, T, U, ComponentAccessor<EntityStore>> predicate, @Nonnull QuadConsumer<Ref<EntityStore>, T, V, R> consumer, T t, U u, V v, R r, ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `forEachEntityUnordered` behavior.
- `forEachEntityAvoidance(@Nonnull Set<Ref<EntityStore>> ignoredEntitiesForAvoidance, @Nonnull TriConsumer<Ref<EntityStore>, T, CommandBuffer<EntityStore>> consumer, T t, CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `forEachEntityAvoidance` behavior.
- `forEachEntityAvoidance(@Nonnull Set<Ref<EntityStore>> ignoredEntitiesForAvoidance, @Nonnull QuadConsumer<Ref<EntityStore>, T, U, CommandBuffer<EntityStore>> consumer, T t, U u, CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `forEachEntityAvoidance` behavior.
- `countEntitiesInRange(double minRange, double maxRange, int maxCount, @Nonnull QuadPredicate<S, Ref<EntityStore>, T, ComponentAccessor<EntityStore>> filter, S s, T t, ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `countEntitiesInRange` behavior.
- `getClosestEntityInRange(double minRange, double maxRange, @Nonnull Predicate<Ref<EntityStore>> filter, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `getClosestEntityInRange` behavior.
- `getClosestEntityInRange(@Nullable Ref<EntityStore> ignoredEntityReference, double minRange, double maxRange, @Nonnull QuadPredicate<S, Ref<EntityStore>, Role, T> filter, Role role, S s, T t, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `getClosestEntityInRange` behavior.
- `getClosestEntityInRangeProjected(@Nonnull Ref<EntityStore> parentRef, @Nullable Ref<EntityStore> ignoredEntityReference, @Nonnull MotionController motionController, double minRange, double maxRange, @Nonnull QuadPredicate<S, Ref<EntityStore>, Role, T> filter, Role role, S s, T t, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `getClosestEntityInRangeProjected` behavior.
- `testAnyEntity(double maxDistance, @Nonnull QuadObjectDoublePredicate<S, Ref<EntityStore>, T, ComponentAccessor<EntityStore>> predicate, S s, T t, ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `testAnyEntity` behavior.
- `testAnyEntityDistanceSquared(double maxDistanceSquared, @Nonnull QuadObjectDoublePredicate<S, Ref<EntityStore>, T, ComponentAccessor<EntityStore>> predicate, S s, T t, ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `testAnyEntityDistanceSquared` behavior.
- `testAnyEntityDistanceSquared(double maxDistanceSquared, @Nonnull QuadObjectDoublePredicate<S, Ref<EntityStore>, T, ComponentAccessor<EntityStore>> predicate, S s, T t, double d, ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `testAnyEntityDistanceSquared` behavior.
- `validateEntityRef(@Nonnull BucketItem<Ref<EntityStore>> holder, ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `validateEntityRef` behavior.

## Notes
- No additional notes.
