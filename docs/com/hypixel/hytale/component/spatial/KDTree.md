**Source Hash:** `cc63ba810830ee8dae72a9e1ab5610736306e287433f742143c7a74c3d7ad43a`

# KDTree

## Overview

## Constructor Descriptions
- `KDTree(@Nonnull Predicate<T> collectionFilter)`
  - Creates a `KDTree` instance.
- `KDTree(size=" + this.size + ")`
  - Creates a `KDTree` instance.

## Method Descriptions
- `size()`: Add description.
  - Executes `size` behavior.
- `rebuild(@Nonnull SpatialData<T> spatialData)`: Add description.
  - Executes `rebuild` behavior.
- `closest(@Nonnull Vector3d point)`: Add description.
  - Executes `closest` behavior.
- `collect(@Nonnull Vector3d center, double radius, @Nonnull List<T> results)`: Add description.
  - Executes `collect` behavior.
- `collectCylinder(@Nonnull Vector3d center, double radius, double height, @Nonnull List<T> results)`: Add description.
  - Executes `collectCylinder` behavior.
- `collectBox(@Nonnull Vector3d min, @Nonnull Vector3d max, @Nonnull List<T> results)`: Add description.
  - Executes `collectBox` behavior.
- `ordered(@Nonnull Vector3d center, double radius, @Nonnull List<T> results)`: Add description.
  - Executes `ordered` behavior.
- `ordered3DAxis(@Nonnull Vector3d center, double xSearchRadius, double YSearchRadius, double zSearchRadius, @Nonnull List<T> results)`: Add description.
  - Executes `ordered3DAxis` behavior.
- `dump()`: Add description.
  - Executes `dump` behavior.
- `getPooledNode(Vector3d vector, List<T> data)`: Add description.
  - Executes `getPooledNode` behavior.
- `getPooledDataList()`: Add description.
  - Executes `getPooledDataList` behavior.
- `build0(@Nonnull SpatialData<T> spatialData, int start, int end)`: Add description.
  - Executes `build0` behavior.
- `put0(@Nonnull Node<T> node, @Nonnull Vector3d vector, @Nonnull List<T> list, int axis)`: Add description.
  - Executes `put0` behavior.
- `closest0(@Nonnull ClosestState<T> closestState, @Nullable Node<T> node, @Nonnull Vector3d vector, int depth)`: Add description.
  - Executes `closest0` behavior.
- `collect0(@Nonnull List<T> results, @Nullable Node<T> node, @Nonnull Vector3d vector, double distanceSq, int depth)`: Add description.
  - Executes `collect0` behavior.
- `collectCylinder0(@Nonnull List<T> results, @Nullable Node<T> node, @Nonnull Vector3d center, double radiusSq, double halfHeight, double radius, int depth)`: Add description.
  - Executes `collectCylinder0` behavior.
- `collectBox0(@Nonnull List<T> results, @Nullable Node<T> node, @Nonnull Vector3d min, @Nonnull Vector3d max, int depth)`: Add description.
  - Executes `collectBox0` behavior.
- `ordered0(@Nonnull List<OrderedEntry<T>> results, @Nullable Node<T> node, @Nonnull Vector3d vector, double distanceSq, int depth)`: Add description.
  - Executes `ordered0` behavior.
- `_internal_ordered3DAxis(@Nonnull List<OrderedEntry<T>> results, @Nullable Node<T> node, @Nonnull Vector3d center, double xSearchRadius, double ySearchRadius, double zSearchRadius, int depth)`: Add description.
  - Executes `_internal_ordered3DAxis` behavior.
- `compare(@Nonnull Vector3d v1, @Nonnull Vector3d v2, int axis)`: Add description.
  - Executes `compare` behavior.
- `get(@Nonnull Vector3d v, int axis)`: Add description.
  - Executes `get` behavior.
- `reset(Vector3d vector, List<T> data)`: Add description.
  - Executes `reset` behavior.
- `dump(int depth)`: Add description.
  - Executes `dump` behavior.

## Notes
- No additional notes.
