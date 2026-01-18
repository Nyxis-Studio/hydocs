# DefaultFluidTicker

## Overview
- Documentation for `DefaultFluidTicker`.
- Declared as a class in `com.hypixel.hytale.server.core.asset.type.fluid`.

## Constructors
- `DefaultFluidTicker()`
  - Creates a `DefaultFluidTicker` instance.

## Methods
- `spread(@Nonnull World world, long tick, @Nonnull FluidTicker.Accessor accessor, @Nonnull FluidSection fluidSection, BlockSection blockSection, @Nonnull Fluid fluid, int fluidId, byte fluidLevel, int worldX, int worldY, int worldZ)`
  - Executes `spread` behavior.
- `executeCollision(@Nonnull World world, @Nonnull FluidTicker.Accessor accessor, @Nonnull FluidSection fluidSection, BlockSection blockSection, @Nonnull FluidCollisionConfig config, int blockX, int blockY, int blockZ)`
  - Executes `executeCollision` behavior.
- `isSelfFluid(int selfFluidId, int otherFluidId)`
  - Executes `isSelfFluid` behavior.
- `getSpreadFluidId(int fluidId)`
  - Executes `getSpreadFluidId` behavior.
- `getCollisionMap()`
  - Executes `getCollisionMap` behavior.
- `getBlockToPlaceIndex()`
  - Executes `getBlockToPlaceIndex` behavior.
- `getSoundEventIndex()`
  - Executes `getSoundEventIndex` behavior.

## Notes
- No additional notes.
