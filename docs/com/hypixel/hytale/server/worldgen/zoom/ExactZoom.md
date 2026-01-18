# ExactZoom

## Overview
- Documentation for `ExactZoom`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.zoom`.

## Constructors
- `ExactZoom(@Nonnull PixelProvider source, double zoomX, double zoomY, int offsetX, int offsetY)`
  - Creates a `ExactZoom` instance.
- `ExactZoom(source, this.zoomX, this.zoomY, this.offsetX, this.offsetY)`
  - Creates a `ExactZoom` instance.

## Methods
- `getDistanceProvider()`
  - Executes `getDistanceProvider` behavior.
- `inBounds(double x, double y)`
  - Executes `inBounds` behavior.
- `generate(double x, double y)`
  - Executes `generate` behavior.
- `distanceToNextPixel(double x, double y)`
  - Executes `distanceToNextPixel` behavior.
- `generateUniqueZones(Zone.UniqueCandidate[] candidates, FastRandom random, List<Zone.Unique> zones)`
  - Executes `generateUniqueZones` behavior.
- `selectCandidatePosition(Zone.UniqueCandidate candidate, PixelProvider source, FastRandom random)`
  - Executes `selectCandidatePosition` behavior.
- `testZoneFit(Zone.UniqueEntry entry, PixelProvider source, int x, int y, int radius)`
  - Executes `testZoneFit` behavior.
- `exportImage()`
  - Executes `exportImage` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
