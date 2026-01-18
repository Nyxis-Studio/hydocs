# FiniteFluidTicker

## Overview
- Documentation for `FiniteFluidTicker`.
- Declared as a class in `com.hypixel.hytale.server.core.asset.type.fluid`.

## Constructors
- None.

## Methods
- `spread(World world, long tick, @Nonnull FluidTicker.Accessor accessor, @Nonnull FluidSection fluidSection, BlockSection blockSection, @Nonnull Fluid fluid, int fluidId, byte fluidLevel, int worldX, int worldY, int worldZ)`
  - Executes `spread` behavior.
- `spreadDownwards(@Nonnull FluidTicker.Accessor accessor, @Nonnull FluidSection fluidSection, BlockSection blockSection, @Nonnull FluidSection belowFluidSection, @Nonnull BlockSection belowBlockSection, int worldX, int worldY, int worldZ, @Nonnull Fluid fluid, int fluidId, byte fluidLevel, int bottomFluidId, byte bottomFluidLevel)`
  - Executes `spreadDownwards` behavior.
- `spreadSideways(long tick, @Nonnull FluidTicker.Accessor accessor, @Nonnull FluidSection fluidSection, BlockSection blockSection, int worldX, int worldY, int worldZ, @Nonnull Fluid fluid, int fluidId, byte fluidLevel)`
  - Executes `spreadSideways` behavior.
- `spreadToOffset(@Nonnull FluidTicker.Accessor accessor, FluidSection fluidSection, BlockSection blockSection, @Nonnull Vector2i offset, int worldX, int worldY, int worldZ, Fluid fluid, int fluidId, byte fluidLevel)`
  - Executes `spreadToOffset` behavior.
- `drainFromTopBlock(@Nonnull FluidTicker.Accessor accessor, @Nonnull FluidSection fluidSection, BlockSection blockSection, int worldX, int worldY, int worldZ, @Nonnull Fluid fluid, int fluidId, byte drainLevels)`
  - Executes `drainFromTopBlock` behavior.
- `getTopY(@Nonnull FluidTicker.Accessor accessor, @Nonnull FluidSection fluidSection, int worldX, int worldY, int worldZ, @Nonnull Fluid fluid, int fluidId)`
  - Executes `getTopY` behavior.
- `isOffsetConnected(@Nonnull FluidTicker.Accessor accessor, BlockSection blockSection, @Nonnull Vector2i offset, int worldX, int worldY, int worldZ)`
  - Executes `isOffsetConnected` behavior.

## Notes
- No additional notes.
