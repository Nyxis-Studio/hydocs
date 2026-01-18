**Source Hash:** `ceb6d6aaace1b01fd5026cafbd05136323d783a414fba64de6d243a1586fa1f6`

# FiniteFluidTicker

## Overview

## Constructor Descriptions
- `none()`: No documented methods.

## Method Descriptions
- `spread(World world, long tick, @Nonnull FluidTicker.Accessor accessor, @Nonnull FluidSection fluidSection, BlockSection blockSection, @Nonnull Fluid fluid, int fluidId, byte fluidLevel, int worldX, int worldY, int worldZ)`: Add description.
  - Executes `spread` behavior.
- `spreadDownwards(@Nonnull FluidTicker.Accessor accessor, @Nonnull FluidSection fluidSection, BlockSection blockSection, @Nonnull FluidSection belowFluidSection, @Nonnull BlockSection belowBlockSection, int worldX, int worldY, int worldZ, @Nonnull Fluid fluid, int fluidId, byte fluidLevel, int bottomFluidId, byte bottomFluidLevel)`: Add description.
  - Executes `spreadDownwards` behavior.
- `spreadSideways(long tick, @Nonnull FluidTicker.Accessor accessor, @Nonnull FluidSection fluidSection, BlockSection blockSection, int worldX, int worldY, int worldZ, @Nonnull Fluid fluid, int fluidId, byte fluidLevel)`: Add description.
  - Executes `spreadSideways` behavior.
- `spreadToOffset(@Nonnull FluidTicker.Accessor accessor, FluidSection fluidSection, BlockSection blockSection, @Nonnull Vector2i offset, int worldX, int worldY, int worldZ, Fluid fluid, int fluidId, byte fluidLevel)`: Add description.
  - Executes `spreadToOffset` behavior.
- `drainFromTopBlock(@Nonnull FluidTicker.Accessor accessor, @Nonnull FluidSection fluidSection, BlockSection blockSection, int worldX, int worldY, int worldZ, @Nonnull Fluid fluid, int fluidId, byte drainLevels)`: Add description.
  - Executes `drainFromTopBlock` behavior.
- `getTopY(@Nonnull FluidTicker.Accessor accessor, @Nonnull FluidSection fluidSection, int worldX, int worldY, int worldZ, @Nonnull Fluid fluid, int fluidId)`: Add description.
  - Executes `getTopY` behavior.
- `isOffsetConnected(@Nonnull FluidTicker.Accessor accessor, BlockSection blockSection, @Nonnull Vector2i offset, int worldX, int worldY, int worldZ)`: Add description.
  - Executes `isOffsetConnected` behavior.

## Notes
- No additional notes.
