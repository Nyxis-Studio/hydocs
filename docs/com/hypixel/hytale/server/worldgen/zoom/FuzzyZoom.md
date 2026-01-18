# FuzzyZoom

## Overview
- Documentation for `FuzzyZoom`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.zoom`.

## Constructors
- `FuzzyZoom(ICoordinateRandomizer randomizer, @Nonnull PixelProvider source, double zoomX, double zoomY, int offsetX, int offsetY)`
  - Creates a `FuzzyZoom` instance.
- `FuzzyZoom(ICoordinateRandomizer randomizer, ExactZoom exactZoom)`
  - Creates a `FuzzyZoom` instance.
- `FuzzyZoom(this.randomizer, this.exactZoom.generateUniqueZones(candidates, random, zones)`
  - Creates a `FuzzyZoom` instance.

## Methods
- `getX(int seed, double x, double y)`
  - Executes `getX` behavior.
- `getY(int seed, double x, double y)`
  - Executes `getY` behavior.
- `generate(double x, double y)`
  - Executes `generate` behavior.
- `distance(double x, double y)`
  - Executes `distance` behavior.
- `getExactZoom()`
  - Executes `getExactZoom` behavior.
- `inBounds(double x, double y)`
  - Executes `inBounds` behavior.
- `generateUniqueZones(Zone.UniqueCandidate[] candidates, FastRandom random, List<Zone.Unique> zones)`
  - Executes `generateUniqueZones` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
