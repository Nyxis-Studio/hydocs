# UniqueClimateGenerator

## Overview
- Documentation for `UniqueClimateGenerator`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.climate`.

## Constructors
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

## Methods
- `entries()`
  - Executes `entries` behavior.
- `zones()`
  - Executes `zones` behavior.
- `generate(int x, int y)`
  - Executes `generate` behavior.
- `apply(int seed, @Nonnull Zone.UniqueCandidate[] candidates, @Nonnull ClimateNoise noise, @Nonnull ClimateGraph graph, @Nonnull List<Zone.Unique> collector)`
  - Executes `apply` behavior.
- `apply(int seed, @Nonnull ClimateNoise noise, @Nonnull ClimateGraph graph)`
  - Executes `apply` behavior.
- `findZonePosition(int seed, Vector2i origin, @Nonnull Entry entry, @Nullable Unique parent, @Nonnull ClimateNoise noise, @Nonnull ClimateGraph graph)`
  - Executes `findZonePosition` behavior.
- `Unique(int color, int radius, int radius2, @Nonnull CompletableFuture<Vector2i> position)`
  - Executes `Unique` behavior.
- `contains(int x, int y)`
  - Executes `contains` behavior.
- `Entry(@Nonnull String zone, @Nonnull String parent, int color, int radius, @Nonnull Vector2i origin, int minDistance, int maxDistance, @Nonnull ClimateSearch.Rule rule)`
  - Executes `Entry` behavior.

## Notes
- No additional notes.
