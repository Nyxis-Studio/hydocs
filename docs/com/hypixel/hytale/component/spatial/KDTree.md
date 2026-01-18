# KDTree

## Overview
- Documentation for `KDTree`.
- Declared as a class in `com.hypixel.hytale.component.spatial`.

## Constructors
- `KDTree(@Nonnull Predicate<T> collectionFilter)`
  - Creates a `KDTree` instance.
- `KDTree(size=" + this.size + ")`
  - Creates a `KDTree` instance.

## Methods
- `size()`
  - Executes `size` behavior.
- `rebuild(@Nonnull SpatialData<T> spatialData)`
  - Executes `rebuild` behavior.
- `closest(@Nonnull Vector3d point)`
  - Executes `closest` behavior.
- `collect(@Nonnull Vector3d center, double radius, @Nonnull List<T> results)`
  - Executes `collect` behavior.
- `collectCylinder(@Nonnull Vector3d center, double radius, double height, @Nonnull List<T> results)`
  - Executes `collectCylinder` behavior.
- `collectBox(@Nonnull Vector3d min, @Nonnull Vector3d max, @Nonnull List<T> results)`
  - Executes `collectBox` behavior.
- `ordered(@Nonnull Vector3d center, double radius, @Nonnull List<T> results)`
  - Executes `ordered` behavior.
- `ordered3DAxis(@Nonnull Vector3d center, double xSearchRadius, double YSearchRadius, double zSearchRadius, @Nonnull List<T> results)`
  - Executes `ordered3DAxis` behavior.
- `dump()`
  - Executes `dump` behavior.
- `getPooledNode(Vector3d vector, List<T> data)`
  - Executes `getPooledNode` behavior.
- `getPooledDataList()`
  - Executes `getPooledDataList` behavior.
- `build0(@Nonnull SpatialData<T> spatialData, int start, int end)`
  - Executes `build0` behavior.
- `put0(@Nonnull Node<T> node, @Nonnull Vector3d vector, @Nonnull List<T> list, int axis)`
  - Executes `put0` behavior.
- `closest0(@Nonnull ClosestState<T> closestState, @Nullable Node<T> node, @Nonnull Vector3d vector, int depth)`
  - Executes `closest0` behavior.
- `collect0(@Nonnull List<T> results, @Nullable Node<T> node, @Nonnull Vector3d vector, double distanceSq, int depth)`
  - Executes `collect0` behavior.
- `collectCylinder0(@Nonnull List<T> results, @Nullable Node<T> node, @Nonnull Vector3d center, double radiusSq, double halfHeight, double radius, int depth)`
  - Executes `collectCylinder0` behavior.
- `collectBox0(@Nonnull List<T> results, @Nullable Node<T> node, @Nonnull Vector3d min, @Nonnull Vector3d max, int depth)`
  - Executes `collectBox0` behavior.
- `ordered0(@Nonnull List<OrderedEntry<T>> results, @Nullable Node<T> node, @Nonnull Vector3d vector, double distanceSq, int depth)`
  - Executes `ordered0` behavior.
- `_internal_ordered3DAxis(@Nonnull List<OrderedEntry<T>> results, @Nullable Node<T> node, @Nonnull Vector3d center, double xSearchRadius, double ySearchRadius, double zSearchRadius, int depth)`
  - Executes `_internal_ordered3DAxis` behavior.
- `compare(@Nonnull Vector3d v1, @Nonnull Vector3d v2, int axis)`
  - Executes `compare` behavior.
- `get(@Nonnull Vector3d v, int axis)`
  - Executes `get` behavior.
- `reset(Vector3d vector, List<T> data)`
  - Executes `reset` behavior.
- `dump(int depth)`
  - Executes `dump` behavior.

## Notes
- No additional notes.
