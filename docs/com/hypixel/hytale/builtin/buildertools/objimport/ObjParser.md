# ObjParser

## Overview
- Documentation for `ObjParser`.
- Declared as a class in `com.hypixel.hytale.builtin.buildertools.objimport`.

## Constructors
- `ObjParser()`
  - Creates a `ObjParser` instance.

## Methods
- `parse(@Nonnull Path path)`
  - Executes `parse` behavior.
- `parseVertex(String[] parts, List<float[]> vertices, int lineNum)`
  - Executes `parseVertex` behavior.
- `parseUvCoordinate(String[] parts, List<float[]> uvCoordinates, int lineNum)`
  - Executes `parseUvCoordinate` behavior.
- `parseFace(String[] parts, List<int[]> faces, List<int[]> faceUvIndices, int uvCount, int lineNum)`
  - Executes `parseFace` behavior.
- `ObjMesh(List<float[]> vertices, List<float[]> uvCoordinates, List<int[]> faces, List<int[]> faceUvIndices, List<String> faceMaterials, @Nullable String mtlLib)`
  - Executes `ObjMesh` behavior.
- `getBounds()`
  - Executes `getBounds` behavior.
- `getHeight()`
  - Executes `getHeight` behavior.
- `hasMaterials()`
  - Executes `hasMaterials` behavior.
- `hasUvCoordinates()`
  - Executes `hasUvCoordinates` behavior.
- `transformZUpToYUp()`
  - Executes `transformZUpToYUp` behavior.
- `transformXUpToYUp()`
  - Executes `transformXUpToYUp` behavior.

## Notes
- No additional notes.
