# ClimateSearch

## Overview
- Documentation for `ClimateSearch`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.climate`.

## Constructors
- None.

## Methods
- `search(int seed, int cx, int cy, int startRadius, int searchRadius, @Nonnull Rule rule, @Nonnull ClimateNoise noise, @Nonnull ClimateGraph graph)`
  - Executes `search` behavior.
- `collect(int seed, int x, int y, ClimateNoise noise, ClimateGraph graph, Rule rule)`
  - Executes `collect` behavior.
- `score(double continent, double temperature, double intensity, double fade)`
  - Executes `score` behavior.
- `score(double value)`
  - Executes `score` behavior.
- `test(double value)`
  - Executes `test` behavior.
- `Result(Vector2i position, double score, long time_ms)`
  - Executes `Result` behavior.
- `pretty()`
  - Executes `pretty` behavior.

## Notes
- No additional notes.
