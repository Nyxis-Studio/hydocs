# CaveType

## Overview
- Documentation for `CaveType`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.cave`.

## Constructors
- `CaveType(String name, CaveNodeType entryNodeType, IFloatRange yaw, IFloatRange pitch, IFloatRange depth, IHeightThresholdInterpreter heightFactors, IPointGenerator pointGenerator, Int2FlagsCondition biomeMask, BlockMaskCondition blockMask, ICoordinateCondition mapCondition, ICoordinateCondition heightCondition, IDoubleRange fixedEntryHeight, NoiseProperty fixedEntryHeightNoise, FluidLevel fluidLevel, int environment, boolean surfaceLimited, boolean submerge, double maximumSize)`
  - Creates a `CaveType` instance.

## Methods
- `getName()`
  - Executes `getName` behavior.
- `getEntryNode()`
  - Executes `getEntryNode` behavior.
- `getModifiedStartHeight(int seed, int x, int y, int z, Random random)`
  - Executes `getModifiedStartHeight` behavior.
- `getStartPitch(Random random)`
  - Executes `getStartPitch` behavior.
- `getStartYaw(Random random)`
  - Executes `getStartYaw` behavior.
- `getStartDepth(Random random)`
  - Executes `getStartDepth` behavior.
- `getHeightRadiusFactor(int seed, double x, double z, int y)`
  - Executes `getHeightRadiusFactor` behavior.
- `getHeightCondition()`
  - Executes `getHeightCondition` behavior.
- `getEntryPointGenerator()`
  - Executes `getEntryPointGenerator` behavior.
- `getBiomeMask()`
  - Executes `getBiomeMask` behavior.
- `getBlockMask()`
  - Executes `getBlockMask` behavior.
- `getFluidLevel()`
  - Executes `getFluidLevel` behavior.
- `getEnvironment()`
  - Executes `getEnvironment` behavior.
- `isSurfaceLimited()`
  - Executes `isSurfaceLimited` behavior.
- `isSubmerge()`
  - Executes `isSubmerge` behavior.
- `isEntryThreshold(int seed, int x, int z)`
  - Executes `isEntryThreshold` behavior.
- `isHeightThreshold(int seed, int x, int y, int z)`
  - Executes `isHeightThreshold` behavior.
- `getMaximumSize()`
  - Executes `getMaximumSize` behavior.
- `_hashCode()`
  - Executes `_hashCode` behavior.
- `hashCode()`
  - Executes `hashCode` behavior.
- `toString()`
  - Executes `toString` behavior.
- `getBlockEntry()`
  - Executes `getBlockEntry` behavior.
- `getHeight()`
  - Executes `getHeight` behavior.

## Notes
- No additional notes.
