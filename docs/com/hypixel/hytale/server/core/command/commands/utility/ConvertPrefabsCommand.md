**Source Hash:** `1c121672ef50f53b0cbd7428b3ef82756064efa9933d200f2dc4db5fda6ef638`

# ConvertPrefabsCommand

## Overview

## Constructor Descriptions
- `ConvertPrefabsCommand()`
  - Creates a `ConvertPrefabsCommand` instance.

## Method Descriptions
- `executeAsync(@Nonnull CommandContext context)`: Add description.
  - Executes `executeAsync` behavior.
- `sendCompletionMessages(@Nonnull CommandContext context, @Nonnull Path assetPath, @Nonnull List<String> failed, @Nonnull List<String> skipped)`: Add description.
  - Executes `sendCompletionMessages` behavior.
- `convertPath(@Nonnull Path assetPath, boolean blocks, boolean filler, boolean relative, boolean entities, boolean destructive, @Nonnull List<String> failed, @Nonnull List<String> skipped)`: Add description.
  - Executes `convertPath` behavior.
- `processPrefabsInBatches(@Nonnull List<Path> prefabPaths, boolean blocks, boolean filler, boolean relative, boolean entities, boolean destructive, @Nullable CompletableFuture<World> conversionWorldFuture, @Nonnull List<String> failed, @Nonnull List<String> skipped)`: Add description.
  - Executes `processPrefabsInBatches` behavior.
- `processPrefab(@Nonnull Path path, boolean blocks, boolean filler, boolean relative, boolean entities, boolean destructive, @Nullable CompletableFuture<World> conversionWorldFuture, @Nonnull List<String> failed, @Nonnull List<String> skipped)`: Add description.
  - Executes `processPrefab` behavior.

## Notes
- No additional notes.
