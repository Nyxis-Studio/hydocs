**Source Hash:** `65c13e6d72c0dcddd8a293ffe9a971da46526108b6bf8ce9f2406040b4198bba`

# ClimateMaskProvider

## Overview

## Constructor Descriptions
- `ClimateMaskProvider(@Nonnull ICoordinateRandomizer randomizer, @Nonnull ClimateNoise noise, @Nonnull ClimateGraph graph, @Nonnull UniqueClimateGenerator uniqueGenerator)`
  - Creates a `ClimateMaskProvider` instance.
- `ClimateMaskProvider(@Nonnull ClimateMaskProvider other, @Nonnull UniqueClimateGenerator uniqueGenerator)`
  - Creates a `ClimateMaskProvider` instance.
- `ClimateMaskProvider(this, this.uniqueGenerator.apply(seed, candidates, this.noise, this.graph, collector)`
  - Creates a `ClimateMaskProvider` instance.

## Method Descriptions
- `getGraph()`: Add description.
  - Executes `getGraph` behavior.
- `inBounds(double x, double y)`: Add description.
  - Executes `inBounds` behavior.
- `getX(int seed, double x, double y)`: Add description.
  - Executes `getX` behavior.
- `getY(int seed, double x, double y)`: Add description.
  - Executes `getY` behavior.
- `get(int seed, double x, double y)`: Add description.
  - Executes `get` behavior.
- `distance(double x, double y)`: Add description.
  - Executes `distance` behavior.
- `generateUniqueZones(int seed, @Nonnull Zone.UniqueCandidate[] candidates, @Nonnull FastRandom random, @Nonnull List<Zone.Unique> collector)`: Add description.
  - Executes `generateUniqueZones` behavior.

## Notes
- No additional notes.
