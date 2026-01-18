# CaveGenerator

## Overview
- Documentation for `CaveGenerator`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.cave`.

## Constructors
- `CaveGenerator(CaveType[] caveTypes)`
  - Creates a `CaveGenerator` instance.

## Methods
- `getCaveTypes()`
  - Executes `getCaveTypes` behavior.
- `generate(int seed, @Nonnull ChunkGenerator chunkGenerator, @Nonnull CaveType caveType, int x, int y, int z)`
  - Executes `generate` behavior.
- `newCave(CaveType caveType)`
  - Executes `newCave` behavior.
- `startCave(int seed, @Nonnull ChunkGenerator chunkGenerator, @Nonnull Cave cave, @Nonnull Vector3d origin, @Nonnull Random random)`
  - Executes `startCave` behavior.
- `continueNode(int seed, @Nonnull ChunkGenerator chunkGenerator, @Nonnull Cave cave, @Nonnull CaveNode parent, int depth, @Nonnull Random random)`
  - Executes `continueNode` behavior.
- `getChildrenCount(@Nonnull CaveNodeType type, Random random)`
  - Executes `getChildrenCount` behavior.
- `getRepeatCounter(@Nonnull CaveNodeType.CaveNodeChildEntry entry, Random random)`
  - Executes `getRepeatCounter` behavior.
- `getRotation(@Nonnull CaveNode caveNode)`
  - Executes `getRotation` behavior.
- `getChildOrigin(@Nonnull CaveNode parentNode, @Nullable PrefabRotation parentRotation, @Nonnull CaveNodeType.CaveNodeChildEntry childEntry)`
  - Executes `getChildOrigin` behavior.
- `getChildYaw(@Nonnull CaveNode parentNode, @Nullable PrefabRotation parentRotation, @Nonnull CaveNodeType.CaveNodeChildEntry childEntry, Random random)`
  - Executes `getChildYaw` behavior.
- `shouldGenerateChild(@Nonnull CaveNodeType.CaveNodeChildEntry entry, @Nonnull Random random)`
  - Executes `shouldGenerateChild` behavior.
- `isMatchingHeight(int seed, @Nonnull Vector3d vec, @Nonnull ICoordinateCondition condition)`
  - Executes `isMatchingHeight` behavior.
- `getNextDepth(@Nonnull CaveNodeType.CaveNodeChildEntry entry, int depth, Random random)`
  - Executes `getNextDepth` behavior.
- `generatePrefabs(int seed, @Nonnull ChunkGenerator chunkGenerator, CaveNode parent, @Nonnull CaveNode node)`
  - Executes `generatePrefabs` behavior.
- `generatePrefab(int seed, @Nonnull ChunkGenerator chunkGenerator, @Nullable CaveNode parent, @Nonnull CaveNode caveNode, @Nonnull CavePrefabContainer.CavePrefabEntry entry, @Nonnull Random random)`
  - Executes `generatePrefab` behavior.
- `isMatchingBiome(int seed, @Nonnull ChunkGenerator chunkGenerator, @Nonnull IIntCondition condition, int x, int z)`
  - Executes `isMatchingBiome` behavior.
- `getBiomeMaskResult(int seed, @Nonnull ChunkGenerator chunkGenerator, @Nonnull Int2FlagsCondition mask, @Nonnull Vector3d vec)`
  - Executes `getBiomeMaskResult` behavior.

## Notes
- No additional notes.
