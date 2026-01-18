# ValidationUtil

## Overview
- Documentation for `ValidationUtil`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.chunk`.

## Constructors
- None.

## Methods
- `isInvalid(@Nonnull ZonePatternProvider zonePatternProvider, @Nonnull Executor executor)`
  - Executes `isInvalid` behavior.
- `isZoneInvalid(@Nonnull Zone zone, @Nonnull Deque<String> trace)`
  - Executes `isZoneInvalid` behavior.
- `isBiomeInvalid(@Nonnull Biome biome, @Nonnull Deque<String> trace)`
  - Executes `isBiomeInvalid` behavior.
- `isCaveNodeInvalid(@Nonnull CaveNodeType caveNodeType, @Nonnull Set<String> encounteredNodes, @Nonnull Deque<String> trace)`
  - Executes `isCaveNodeInvalid` behavior.
- `arePrefabsInvalid(@Nonnull IWeightedMap<WorldGenPrefabSupplier> prefabs, @Nonnull Deque<String> trace)`
  - Executes `arePrefabsInvalid` behavior.
- `isChildPrefabInvalid(@Nonnull PrefabBuffer.ChildPrefab childMarker, @Nonnull WorldGenPrefabLoader loader, @Nonnull Deque<String> trace)`
  - Executes `isChildPrefabInvalid` behavior.

## Notes
- No additional notes.
