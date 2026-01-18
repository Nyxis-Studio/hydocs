# SpatialHashGrid

## Overview
- Documentation for `SpatialHashGrid`.
- Declared as a class in `com.hypixel.hytale.builtin.portals.utils.spatial`.

## Constructors
- `SpatialHashGrid(double cellSize)`
  - Creates a `SpatialHashGrid` instance.

## Methods
- `cellFor(Vector3d p)`
  - Executes `cellFor` behavior.
- `size()`
  - Executes `size` behavior.
- `isEmpty()`
  - Executes `isEmpty` behavior.
- `add(Vector3d pos, T value)`
  - Executes `add` behavior.
- `remove(T value)`
  - Executes `remove` behavior.
- `removeIf(Predicate<T> predicate)`
  - Executes `removeIf` behavior.
- `move(T value, Vector3d newPos)`
  - Executes `move` behavior.
- `queryRange(Vector3d center, double radius)`
  - Executes `queryRange` behavior.
- `findClosest(final Vector3d center, double searchRadius)`
  - Executes `findClosest` behavior.
- `visit(List<Entry<T>> bucket)`
  - Executes `visit` behavior.
- `hasAnyWithin(final Vector3d center, final double radius)`
  - Executes `hasAnyWithin` behavior.
- `query(Vector3d center, double radius, CellVisitor<T> visitor)`
  - Executes `query` behavior.
- `visit(List<Entry<T>> var1)`
  - Executes `visit` behavior.

## Notes
- No additional notes.
