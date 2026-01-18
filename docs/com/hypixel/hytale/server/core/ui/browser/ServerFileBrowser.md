# ServerFileBrowser

## Overview
- Documentation for `ServerFileBrowser`.
- Declared as a class in `com.hypixel.hytale.server.core.ui.browser`.

## Constructors
- `ServerFileBrowser(@Nonnull FileBrowserConfig config)`
  - Creates a `ServerFileBrowser` instance.
- `ServerFileBrowser(@Nonnull FileBrowserConfig config, @Nullable Path initialRoot, @Nullable Path initialDir)`
  - Creates a `ServerFileBrowser` instance.

## Methods
- `buildRootSelector(@Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder)`
  - Executes `buildRootSelector` behavior.
- `buildSearchInput(@Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder)`
  - Executes `buildSearchInput` behavior.
- `buildCurrentPath(@Nonnull UICommandBuilder commandBuilder)`
  - Executes `buildCurrentPath` behavior.
- `buildFileList(@Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder)`
  - Executes `buildFileList` behavior.
- `buildUI(@Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder)`
  - Executes `buildUI` behavior.
- `handleEvent(@Nonnull FileBrowserEventData data)`
  - Executes `handleEvent` behavior.
- `visitFile(@Nonnull Path file, @Nonnull BasicFileAttributes attrs)`
  - Executes `visitFile` behavior.
- `matchesExtension(@Nonnull String fileName)`
  - Executes `matchesExtension` behavior.
- `removeExtensions(@Nonnull String fileName)`
  - Executes `removeExtensions` behavior.
- `getRoot()`
  - Executes `getRoot` behavior.
- `setRoot(@Nonnull Path root)`
  - Executes `setRoot` behavior.
- `getCurrentDir()`
  - Executes `getCurrentDir` behavior.
- `setCurrentDir(@Nonnull Path currentDir)`
  - Executes `setCurrentDir` behavior.
- `getSearchQuery()`
  - Executes `getSearchQuery` behavior.
- `setSearchQuery(@Nonnull String searchQuery)`
  - Executes `setSearchQuery` behavior.
- `navigateUp()`
  - Executes `navigateUp` behavior.
- `navigateTo(@Nonnull Path relativePath)`
  - Executes `navigateTo` behavior.
- `getSelectedItems()`
  - Executes `getSelectedItems` behavior.
- `addSelection(@Nonnull String item)`
  - Executes `addSelection` behavior.
- `clearSelection()`
  - Executes `clearSelection` behavior.
- `getConfig()`
  - Executes `getConfig` behavior.
- `resolveSecure(@Nonnull String relativePath)`
  - Executes `resolveSecure` behavior.
- `resolveFromCurrent(@Nonnull String fileName)`
  - Executes `resolveFromCurrent` behavior.
- `findConfigRoot(@Nonnull String pathStr)`
  - Executes `findConfigRoot` behavior.

## Notes
- No additional notes.
