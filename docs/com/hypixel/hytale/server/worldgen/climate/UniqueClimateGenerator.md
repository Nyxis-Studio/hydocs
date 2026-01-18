**Source Hash:** `47cb4d7982cd7c4a67cd54e350b185990d8979b03f652d0c9d79d7839956fc98`

# UniqueClimateGenerator

## Overview

## Constructor Descriptions
- `UniqueClimateGenerator(Entry.EMPTY_ARRAY, Unique.EMPTY_ARRAY)`
  - Creates a `UniqueClimateGenerator` instance.
- `UniqueClimateGenerator(@Nonnull Entry[] entries)`
  - Creates a `UniqueClimateGenerator` instance.
- `UniqueClimateGenerator(@Nonnull Entry[] entries, @Nonnull Unique[] zones)`
  - Creates a `UniqueClimateGenerator` instance.
- `UniqueClimateGenerator(this.entries, unique)`
  - Creates a `UniqueClimateGenerator` instance.
- `UniqueClimateGenerator(newEntries, newUnique)`
  - Creates a `UniqueClimateGenerator` instance.

## Method Descriptions
- `entries()`: Add description.
  - Executes `entries` behavior.
- `zones()`: Add description.
  - Executes `zones` behavior.
- `generate(int x, int y)`: Add description.
  - Executes `generate` behavior.
- `apply(int seed, @Nonnull Zone.UniqueCandidate[] candidates, @Nonnull ClimateNoise noise, @Nonnull ClimateGraph graph, @Nonnull List<Zone.Unique> collector)`: Add description.
  - Executes `apply` behavior.
- `apply(int seed, @Nonnull ClimateNoise noise, @Nonnull ClimateGraph graph)`: Add description.
  - Executes `apply` behavior.
- `findZonePosition(int seed, Vector2i origin, @Nonnull Entry entry, @Nullable Unique parent, @Nonnull ClimateNoise noise, @Nonnull ClimateGraph graph)`: Add description.
  - Executes `findZonePosition` behavior.
- `Unique(int color, int radius, int radius2, @Nonnull CompletableFuture<Vector2i> position)`: Add description.
  - Executes `Unique` behavior.
- `contains(int x, int y)`: Add description.
  - Executes `contains` behavior.
- `Entry(@Nonnull String zone, @Nonnull String parent, int color, int radius, @Nonnull Vector2i origin, int minDistance, int maxDistance, @Nonnull ClimateSearch.Rule rule)`: Add description.
  - Executes `Entry` behavior.

## Notes
- No additional notes.
