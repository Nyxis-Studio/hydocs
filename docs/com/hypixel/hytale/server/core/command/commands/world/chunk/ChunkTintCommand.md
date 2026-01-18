# ChunkTintCommand

## Overview
- Documentation for `ChunkTintCommand`.
- Declared as a class in `com.hypixel.hytale.server.core.command.commands.world.chunk`.

## Constructors
- `ChunkTintCommand()`
  - Creates a `ChunkTintCommand` instance.

## Methods
- `execute(@Nonnull CommandContext context, @Nonnull Store<EntityStore> store, @Nonnull Ref<EntityStore> ref, @Nonnull PlayerRef playerRef, @Nonnull World world)`
  - Executes `execute` behavior.
- `blur(@Nonnull ChunkAccessor<WorldChunk> chunkAccessor, int radius, double[] matrix, int x, int z)`
  - Executes `blur` behavior.
- `gaussian2d(double sigma, double x, double y)`
  - Executes `gaussian2d` behavior.
- `gaussianMatrix(double sigma, int radius)`
  - Executes `gaussianMatrix` behavior.
- `gaussianIndex(int radius, int x, int y)`
  - Executes `gaussianIndex` behavior.
- `build(@Nonnull Ref<EntityStore> ref, @Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder, @Nonnull Store<EntityStore> store)`
  - Executes `build` behavior.
- `handleDataEvent(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull TintChunkPageEventData data)`
  - Executes `handleDataEvent` behavior.
- `getColor()`
  - Executes `getColor` behavior.
- `getRadius()`
  - Executes `getRadius` behavior.
- `getSigma()`
  - Executes `getSigma` behavior.
- `isBlurEnabled()`
  - Executes `isBlurEnabled` behavior.
- `getKeyHexColor()`
  - Executes `getKeyHexColor` behavior.
- `getAction()`
  - Executes `getAction` behavior.

## Notes
- No additional notes.
