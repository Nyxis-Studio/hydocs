# ClimateMaskProvider

## Overview
- Documentation for `ClimateMaskProvider`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.climate`.

## Constructors
- `ClimateMaskProvider(@Nonnull ICoordinateRandomizer randomizer, @Nonnull ClimateNoise noise, @Nonnull ClimateGraph graph, @Nonnull UniqueClimateGenerator uniqueGenerator)`
  - Creates a `ClimateMaskProvider` instance.
- `ClimateMaskProvider(@Nonnull ClimateMaskProvider other, @Nonnull UniqueClimateGenerator uniqueGenerator)`
  - Creates a `ClimateMaskProvider` instance.
- `ClimateMaskProvider(this, this.uniqueGenerator.apply(seed, candidates, this.noise, this.graph, collector)`
  - Creates a `ClimateMaskProvider` instance.

## Methods
- `getGraph()`
  - Executes `getGraph` behavior.
- `inBounds(double x, double y)`
  - Executes `inBounds` behavior.
- `getX(int seed, double x, double y)`
  - Executes `getX` behavior.
- `getY(int seed, double x, double y)`
  - Executes `getY` behavior.
- `get(int seed, double x, double y)`
  - Executes `get` behavior.
- `distance(double x, double y)`
  - Executes `distance` behavior.
- `generateUniqueZones(int seed, @Nonnull Zone.UniqueCandidate[] candidates, @Nonnull FastRandom random, @Nonnull List<Zone.Unique> collector)`
  - Executes `generateUniqueZones` behavior.

## Notes
- No additional notes.
