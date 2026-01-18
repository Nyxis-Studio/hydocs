**Source Hash:** `a42e0e2ef5ade426ea953e2a450bf9aa4ad2adfe0ff9e3647bcec2187f85482f`

# CaveGenerator

## Overview

## Constructor Descriptions
- `CaveGenerator(CaveType[] caveTypes)`
  - Creates a `CaveGenerator` instance.

## Method Descriptions
- `getCaveTypes()`: Add description.
  - Executes `getCaveTypes` behavior.
- `generate(int seed, @Nonnull ChunkGenerator chunkGenerator, @Nonnull CaveType caveType, int x, int y, int z)`: Add description.
  - Executes `generate` behavior.
- `newCave(CaveType caveType)`: Add description.
  - Executes `newCave` behavior.
- `startCave(int seed, @Nonnull ChunkGenerator chunkGenerator, @Nonnull Cave cave, @Nonnull Vector3d origin, @Nonnull Random random)`: Add description.
  - Executes `startCave` behavior.
- `continueNode(int seed, @Nonnull ChunkGenerator chunkGenerator, @Nonnull Cave cave, @Nonnull CaveNode parent, int depth, @Nonnull Random random)`: Add description.
  - Executes `continueNode` behavior.
- `getChildrenCount(@Nonnull CaveNodeType type, Random random)`: Add description.
  - Executes `getChildrenCount` behavior.
- `getRepeatCounter(@Nonnull CaveNodeType.CaveNodeChildEntry entry, Random random)`: Add description.
  - Executes `getRepeatCounter` behavior.
- `getRotation(@Nonnull CaveNode caveNode)`: Add description.
  - Executes `getRotation` behavior.
- `getChildOrigin(@Nonnull CaveNode parentNode, @Nullable PrefabRotation parentRotation, @Nonnull CaveNodeType.CaveNodeChildEntry childEntry)`: Add description.
  - Executes `getChildOrigin` behavior.
- `getChildYaw(@Nonnull CaveNode parentNode, @Nullable PrefabRotation parentRotation, @Nonnull CaveNodeType.CaveNodeChildEntry childEntry, Random random)`: Add description.
  - Executes `getChildYaw` behavior.
- `shouldGenerateChild(@Nonnull CaveNodeType.CaveNodeChildEntry entry, @Nonnull Random random)`: Add description.
  - Executes `shouldGenerateChild` behavior.
- `isMatchingHeight(int seed, @Nonnull Vector3d vec, @Nonnull ICoordinateCondition condition)`: Add description.
  - Executes `isMatchingHeight` behavior.
- `getNextDepth(@Nonnull CaveNodeType.CaveNodeChildEntry entry, int depth, Random random)`: Add description.
  - Executes `getNextDepth` behavior.
- `generatePrefabs(int seed, @Nonnull ChunkGenerator chunkGenerator, CaveNode parent, @Nonnull CaveNode node)`: Add description.
  - Executes `generatePrefabs` behavior.
- `generatePrefab(int seed, @Nonnull ChunkGenerator chunkGenerator, @Nullable CaveNode parent, @Nonnull CaveNode caveNode, @Nonnull CavePrefabContainer.CavePrefabEntry entry, @Nonnull Random random)`: Add description.
  - Executes `generatePrefab` behavior.
- `isMatchingBiome(int seed, @Nonnull ChunkGenerator chunkGenerator, @Nonnull IIntCondition condition, int x, int z)`: Add description.
  - Executes `isMatchingBiome` behavior.
- `getBiomeMaskResult(int seed, @Nonnull ChunkGenerator chunkGenerator, @Nonnull Int2FlagsCondition mask, @Nonnull Vector3d vec)`: Add description.
  - Executes `getBiomeMaskResult` behavior.

## Notes
- No additional notes.
