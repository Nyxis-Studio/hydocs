# OctTree

## Overview
- Documentation for `OctTree`.
- Declared as a class in `com.hypixel.hytale.builtin.portals.utils.spatial`.

## Constructors
- `OctTree(double inradius)`
  - Creates a `OctTree` instance.
- `OctTree(Box boundary)`
  - Creates a `OctTree` instance.
- `OctTree(Box boundary, int nodeCapacity)`
  - Creates a `OctTree` instance.

## Methods
- `add(Vector3d pos, T value)`
  - Executes `add` behavior.
- `add(Node node, Vector3d pos, T value)`
  - Executes `add` behavior.
- `subdivide(Node node)`
  - Executes `subdivide` behavior.
- `getAllPoints()`
  - Executes `getAllPoints` behavior.
- `queryRange(Vector3d position, double inradius)`
  - Executes `queryRange` behavior.
- `queryRange(Box range)`
  - Executes `queryRange` behavior.
- `queryRange(Node node, Box range, Map<T, Vector3d> out)`
  - Executes `queryRange` behavior.
- `size()`
  - Executes `size` behavior.
- `addPoint(Vector3d pos, T value)`
  - Executes `addPoint` behavior.

## Notes
- No additional notes.
