**Source Hash:** `c48b9e0b408c4ea1b9dbc0ca9ac7bc694c6ae461ac4701cca60bb358b9d6ff40`

# MeshVoxelizer

## Overview

## Constructor Descriptions
- `MeshVoxelizer()`
  - Creates a `MeshVoxelizer` instance.

## Method Descriptions
- `voxelize(@Nonnull ObjParser.ObjMesh mesh, int targetHeight, boolean fillSolid)`: Add description.
  - Executes `voxelize` behavior.
- `voxelize(@Nonnull ObjParser.ObjMesh mesh, int targetHeight, boolean fillSolid, @Nullable Map<String, Integer> materialToBlockId)`: Add description.
  - Executes `voxelize` behavior.
- `voxelize(@Nonnull ObjParser.ObjMesh mesh, int targetHeight, boolean fillSolid, @Nullable Map<String, Integer> materialToBlockId, int defaultBlockId)`: Add description.
  - Executes `voxelize` behavior.
- `voxelize(@Nonnull ObjParser.ObjMesh mesh, int targetHeight, boolean fillSolid, @Nullable Map<String, BufferedImage> materialTextures, @Nullable Map<String, Integer> materialToBlockId, @Nullable BlockColorIndex colorIndex, int defaultBlockId)`: Add description.
  - Executes `voxelize` behavior.
- `voxelize(@Nonnull ObjParser.ObjMesh mesh, int targetHeight, boolean fillSolid, @Nullable Map<String, BufferedImage> materialTextures, @Nullable Map<String, Integer> materialToBlockId, @Nullable BlockColorIndex colorIndex, int defaultBlockId, boolean preserveOrigin)`: Add description.
  - Executes `voxelize` behavior.
- `resolveIndex(int index, int count)`: Add description.
  - Executes `resolveIndex` behavior.
- `rasterizeSurface(boolean[][][] voxels, @Nullable int[][][] blockIds, float[][] vertices, ObjParser.ObjMesh mesh, @Nullable Map<String, BufferedImage> materialTextures, @Nullable Map<String, Integer> materialToBlockId, @Nullable BlockColorIndex colorIndex, int defaultBlockId, int sizeX, int sizeY, int sizeZ)`: Add description.
  - Executes `rasterizeSurface` behavior.
- `rasterizeLine(boolean[][][] voxels, @Nullable int[][][] blockIds, float[] a, float[] b, @Nullable float[] uvA, @Nullable float[] uvB, @Nullable BufferedImage texture, @Nullable BlockColorIndex colorIndex, int fallbackBlockId, int sizeX, int sizeY, int sizeZ)`: Add description.
  - Executes `rasterizeLine` behavior.
- `interpolateUv(@Nullable float[] uvA, @Nullable float[] uvB, float t)`: Add description.
  - Executes `interpolateUv` behavior.
- `sampleBlockId(@Nullable float[] uv, @Nullable BufferedImage texture, @Nullable BlockColorIndex colorIndex, int fallbackBlockId)`: Add description.
  - Executes `sampleBlockId` behavior.
- `setVoxel(boolean[][][] voxels, @Nullable int[][][] blockIds, int x, int y, int z, int blockId, int sizeX, int sizeY, int sizeZ)`: Add description.
  - Executes `setVoxel` behavior.
- `rasterizeTriangle(boolean[][][] voxels, @Nullable int[][][] blockIds, float[] v0, float[] v1, float[] v2, @Nullable float[] uv0, @Nullable float[] uv1, @Nullable float[] uv2, @Nullable BufferedImage texture, @Nullable BlockColorIndex colorIndex, int fallbackBlockId, int sizeX, int sizeY, int sizeZ)`: Add description.
  - Executes `rasterizeTriangle` behavior.
- `barycentric(float px, float py, float pz, float[] v0, float[] v1, float[] v2)`: Add description.
  - Executes `barycentric` behavior.
- `pointNearTriangle(float px, float py, float pz, float[] v0, float[] v1, float[] v2, float threshold)`: Add description.
  - Executes `pointNearTriangle` behavior.
- `pointInTriangleWithTolerance(float px, float py, float pz, float[] v0, float[] v1, float[] v2, float tolerance)`: Add description.
  - Executes `pointInTriangleWithTolerance` behavior.
- `floodFillSolid(boolean[][][] shell, int sizeX, int sizeY, int sizeZ)`: Add description.
  - Executes `floodFillSolid` behavior.
- `tryEnqueue(boolean[][][] shell, int sizeX, int sizeY, int sizeZ, boolean[] visited, int[] queue, int ex, int ey, int ez, int dx, int plane, int writeIndex)`: Add description.
  - Executes `tryEnqueue` behavior.
- `cropToSolidBounds(boolean[][][] voxels, @Nullable int[][][] blockIds, int sizeX, int sizeY, int sizeZ)`: Add description.
  - Executes `cropToSolidBounds` behavior.
- `fillInteriorBlockIds(boolean[][][] solid, boolean[][][] shell, int[][][] blockIds, int defaultBlockId, int sizeX, int sizeY, int sizeZ)`: Add description.
  - Executes `fillInteriorBlockIds` behavior.
- `findNearestSurfaceBlockId(int[][][] blockIds, boolean[][][] shell, int cx, int cy, int cz, int sizeX, int sizeY, int sizeZ)`: Add description.
  - Executes `findNearestSurfaceBlockId` behavior.
- `VoxelResult(boolean[][][] voxels, @Nullable int[][][] blockIds, int sizeX, int sizeY, int sizeZ)`: Add description.
  - Executes `VoxelResult` behavior.
- `countSolid()`: Add description.
  - Executes `countSolid` behavior.
- `getBlockId(int x, int y, int z)`: Add description.
  - Executes `getBlockId` behavior.

## Notes
- No additional notes.
