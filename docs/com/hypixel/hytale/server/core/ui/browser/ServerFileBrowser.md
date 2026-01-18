**Source Hash:** `e2a77bfffa46ff9950e6ab0c82f56a79719e1b9dcf8f52f809ebef5146d8c664`

# ServerFileBrowser

## Overview

## Constructor Descriptions
- `ServerFileBrowser(@Nonnull FileBrowserConfig config)`
  - Creates a `ServerFileBrowser` instance.
- `ServerFileBrowser(@Nonnull FileBrowserConfig config, @Nullable Path initialRoot, @Nullable Path initialDir)`
  - Creates a `ServerFileBrowser` instance.

## Method Descriptions
- `buildRootSelector(@Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder)`: Add description.
  - Executes `buildRootSelector` behavior.
- `buildSearchInput(@Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder)`: Add description.
  - Executes `buildSearchInput` behavior.
- `buildCurrentPath(@Nonnull UICommandBuilder commandBuilder)`: Add description.
  - Executes `buildCurrentPath` behavior.
- `buildFileList(@Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder)`: Add description.
  - Executes `buildFileList` behavior.
- `buildUI(@Nonnull UICommandBuilder commandBuilder, @Nonnull UIEventBuilder eventBuilder)`: Add description.
  - Executes `buildUI` behavior.
- `handleEvent(@Nonnull FileBrowserEventData data)`: Add description.
  - Executes `handleEvent` behavior.
- `visitFile(@Nonnull Path file, @Nonnull BasicFileAttributes attrs)`: Add description.
  - Executes `visitFile` behavior.
- `matchesExtension(@Nonnull String fileName)`: Add description.
  - Executes `matchesExtension` behavior.
- `removeExtensions(@Nonnull String fileName)`: Add description.
  - Executes `removeExtensions` behavior.
- `getRoot()`: Add description.
  - Executes `getRoot` behavior.
- `setRoot(@Nonnull Path root)`: Add description.
  - Executes `setRoot` behavior.
- `getCurrentDir()`: Add description.
  - Executes `getCurrentDir` behavior.
- `setCurrentDir(@Nonnull Path currentDir)`: Add description.
  - Executes `setCurrentDir` behavior.
- `getSearchQuery()`: Add description.
  - Executes `getSearchQuery` behavior.
- `setSearchQuery(@Nonnull String searchQuery)`: Add description.
  - Executes `setSearchQuery` behavior.
- `navigateUp()`: Add description.
  - Executes `navigateUp` behavior.
- `navigateTo(@Nonnull Path relativePath)`: Add description.
  - Executes `navigateTo` behavior.
- `getSelectedItems()`: Add description.
  - Executes `getSelectedItems` behavior.
- `addSelection(@Nonnull String item)`: Add description.
  - Executes `addSelection` behavior.
- `clearSelection()`: Add description.
  - Executes `clearSelection` behavior.
- `getConfig()`: Add description.
  - Executes `getConfig` behavior.
- `resolveSecure(@Nonnull String relativePath)`: Add description.
  - Executes `resolveSecure` behavior.
- `resolveFromCurrent(@Nonnull String fileName)`: Add description.
  - Executes `resolveFromCurrent` behavior.
- `findConfigRoot(@Nonnull String pathStr)`: Add description.
  - Executes `findConfigRoot` behavior.

## Notes
- No additional notes.
