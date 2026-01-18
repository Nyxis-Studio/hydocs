# AssetMonitor

## Overview
- Documentation for `AssetMonitor`.
- Declared as a class in `com.hypixel.hytale.server.core.asset.monitor`.

## Constructors
- `AssetMonitor()`
  - Creates a `AssetMonitor` instance.

## Methods
- `shutdown()`
  - Executes `shutdown` behavior.
- `monitorDirectoryFiles(@Nonnull Path path, @Nonnull AssetMonitorHandler handler)`
  - Executes `monitorDirectoryFiles` behavior.
- `removeMonitorDirectoryFiles(@Nonnull Path path, @Nonnull Object key)`
  - Executes `removeMonitorDirectoryFiles` behavior.
- `onChange(@Nonnull Path file, EventKind eventKind)`
  - Executes `onChange` behavior.
- `onDelayedChange(@Nonnull Path path, @Nonnull PathEvent pathEvent)`
  - Executes `onDelayedChange` behavior.
- `removeFileChangeTask(@Nonnull FileChangeTask fileChangeTask)`
  - Executes `removeFileChangeTask` behavior.
- `markChanged(@Nonnull Path path)`
  - Executes `markChanged` behavior.
- `removeHookChangeTask(@Nonnull DirectoryHandlerChangeTask directoryHandlerChangeTask)`
  - Executes `removeHookChangeTask` behavior.

## Notes
- No additional notes.
