# MeshVoxelizer

## Overview
- Documentation for `MeshVoxelizer`.
- Declared as a class in `com.hypixel.hytale.builtin.buildertools.objimport`.

## Constructors
- `MeshVoxelizer()`
  - Creates a `MeshVoxelizer` instance.

## Methods
- `voxelize(@Nonnull ObjParser.ObjMesh mesh, int targetHeight, boolean fillSolid)`
  - Executes `voxelize` behavior.
- `voxelize(@Nonnull ObjParser.ObjMesh mesh, int targetHeight, boolean fillSolid, @Nullable Map<String, Integer> materialToBlockId)`
  - Executes `voxelize` behavior.
- `voxelize(@Nonnull ObjParser.ObjMesh mesh, int targetHeight, boolean fillSolid, @Nullable Map<String, Integer> materialToBlockId, int defaultBlockId)`
  - Executes `voxelize` behavior.
- `voxelize(@Nonnull ObjParser.ObjMesh mesh, int targetHeight, boolean fillSolid, @Nullable Map<String, BufferedImage> materialTextures, @Nullable Map<String, Integer> materialToBlockId, @Nullable BlockColorIndex colorIndex, int defaultBlockId)`
  - Executes `voxelize` behavior.
- `voxelize(@Nonnull ObjParser.ObjMesh mesh, int targetHeight, boolean fillSolid, @Nullable Map<String, BufferedImage> materialTextures, @Nullable Map<String, Integer> materialToBlockId, @Nullable BlockColorIndex colorIndex, int defaultBlockId, boolean preserveOrigin)`
  - Executes `voxelize` behavior.
- `resolveIndex(int index, int count)`
  - Executes `resolveIndex` behavior.
- `rasterizeSurface(boolean[][][] voxels, @Nullable int[][][] blockIds, float[][] vertices, ObjParser.ObjMesh mesh, @Nullable Map<String, BufferedImage> materialTextures, @Nullable Map<String, Integer> materialToBlockId, @Nullable BlockColorIndex colorIndex, int defaultBlockId, int sizeX, int sizeY, int sizeZ)`
  - Executes `rasterizeSurface` behavior.
- `rasterizeLine(boolean[][][] voxels, @Nullable int[][][] blockIds, float[] a, float[] b, @Nullable float[] uvA, @Nullable float[] uvB, @Nullable BufferedImage texture, @Nullable BlockColorIndex colorIndex, int fallbackBlockId, int sizeX, int sizeY, int sizeZ)`
  - Executes `rasterizeLine` behavior.
- `interpolateUv(@Nullable float[] uvA, @Nullable float[] uvB, float t)`
  - Executes `interpolateUv` behavior.
- `sampleBlockId(@Nullable float[] uv, @Nullable BufferedImage texture, @Nullable BlockColorIndex colorIndex, int fallbackBlockId)`
  - Executes `sampleBlockId` behavior.
- `setVoxel(boolean[][][] voxels, @Nullable int[][][] blockIds, int x, int y, int z, int blockId, int sizeX, int sizeY, int sizeZ)`
  - Executes `setVoxel` behavior.
- `rasterizeTriangle(boolean[][][] voxels, @Nullable int[][][] blockIds, float[] v0, float[] v1, float[] v2, @Nullable float[] uv0, @Nullable float[] uv1, @Nullable float[] uv2, @Nullable BufferedImage texture, @Nullable BlockColorIndex colorIndex, int fallbackBlockId, int sizeX, int sizeY, int sizeZ)`
  - Executes `rasterizeTriangle` behavior.
- `barycentric(float px, float py, float pz, float[] v0, float[] v1, float[] v2)`
  - Executes `barycentric` behavior.
- `pointNearTriangle(float px, float py, float pz, float[] v0, float[] v1, float[] v2, float threshold)`
  - Executes `pointNearTriangle` behavior.
- `pointInTriangleWithTolerance(float px, float py, float pz, float[] v0, float[] v1, float[] v2, float tolerance)`
  - Executes `pointInTriangleWithTolerance` behavior.
- `floodFillSolid(boolean[][][] shell, int sizeX, int sizeY, int sizeZ)`
  - Executes `floodFillSolid` behavior.
- `tryEnqueue(boolean[][][] shell, int sizeX, int sizeY, int sizeZ, boolean[] visited, int[] queue, int ex, int ey, int ez, int dx, int plane, int writeIndex)`
  - Executes `tryEnqueue` behavior.
- `cropToSolidBounds(boolean[][][] voxels, @Nullable int[][][] blockIds, int sizeX, int sizeY, int sizeZ)`
  - Executes `cropToSolidBounds` behavior.
- `fillInteriorBlockIds(boolean[][][] solid, boolean[][][] shell, int[][][] blockIds, int defaultBlockId, int sizeX, int sizeY, int sizeZ)`
  - Executes `fillInteriorBlockIds` behavior.
- `findNearestSurfaceBlockId(int[][][] blockIds, boolean[][][] shell, int cx, int cy, int cz, int sizeX, int sizeY, int sizeZ)`
  - Executes `findNearestSurfaceBlockId` behavior.
- `VoxelResult(boolean[][][] voxels, @Nullable int[][][] blockIds, int sizeX, int sizeY, int sizeZ)`
  - Executes `VoxelResult` behavior.
- `countSolid()`
  - Executes `countSolid` behavior.
- `getBlockId(int x, int y, int z)`
  - Executes `getBlockId` behavior.

## Notes
- No additional notes.
