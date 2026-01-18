# ConvertPrefabsCommand

## Overview
- Documentation for `ConvertPrefabsCommand`.
- Declared as a class in `com.hypixel.hytale.server.core.command.commands.utility`.

## Constructors
- `ConvertPrefabsCommand()`
  - Creates a `ConvertPrefabsCommand` instance.

## Methods
- `executeAsync(@Nonnull CommandContext context)`
  - Executes `executeAsync` behavior.
- `sendCompletionMessages(@Nonnull CommandContext context, @Nonnull Path assetPath, @Nonnull List<String> failed, @Nonnull List<String> skipped)`
  - Executes `sendCompletionMessages` behavior.
- `convertPath(@Nonnull Path assetPath, boolean blocks, boolean filler, boolean relative, boolean entities, boolean destructive, @Nonnull List<String> failed, @Nonnull List<String> skipped)`
  - Executes `convertPath` behavior.
- `processPrefabsInBatches(@Nonnull List<Path> prefabPaths, boolean blocks, boolean filler, boolean relative, boolean entities, boolean destructive, @Nullable CompletableFuture<World> conversionWorldFuture, @Nonnull List<String> failed, @Nonnull List<String> skipped)`
  - Executes `processPrefabsInBatches` behavior.
- `processPrefab(@Nonnull Path path, boolean blocks, boolean filler, boolean relative, boolean entities, boolean destructive, @Nullable CompletableFuture<World> conversionWorldFuture, @Nonnull List<String> failed, @Nonnull List<String> skipped)`
  - Executes `processPrefab` behavior.

## Notes
- No additional notes.
