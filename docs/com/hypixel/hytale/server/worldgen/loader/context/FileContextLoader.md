# FileContextLoader

## Overview
- Documentation for `FileContextLoader`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.loader.context`.

## Constructors
- `FileContextLoader(Path dataFolder, Set<String> zoneRequirement)`
  - Creates a `FileContextLoader` instance.

## Methods
- `load()`
  - Executes `load` behavior.
- `loadPrefabCategories(@Nonnull Path folder, @Nonnull FileLoadingContext context)`
  - Executes `loadPrefabCategories` behavior.
- `loadZoneContext(String name, @Nonnull Path folder, @Nonnull FileLoadingContext context)`
  - Executes `loadZoneContext` behavior.
- `compareBiomePaths(@Nonnull Path a, @Nonnull Path b)`
  - Executes `compareBiomePaths` behavior.
- `isValidBiomeFile(@Nonnull Path path)`
  - Executes `isValidBiomeFile` behavior.
- `validateZones(@Nonnull FileLoadingContext context, @Nonnull Set<String> zoneRequirement)`
  - Executes `validateZones` behavior.
- `parseName(@Nonnull Path path, @Nonnull BiomeFileContext.Type type)`
  - Executes `parseName` behavior.

## Notes
- No additional notes.
