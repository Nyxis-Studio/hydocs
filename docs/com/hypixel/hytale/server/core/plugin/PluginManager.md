**Source Hash:** `116eb5c7747463d409ad215338a4bff902dd23bd9d9aa0b8f5307eae6a7d3bd7`

# PluginManager

## Overview

## Constructor Descriptions
- `PluginManager()`
  - Creates a `PluginManager` instance.

## Method Descriptions
- `get()`: Add description.
  - Executes `get` behavior.
- `registerCorePlugin(@Nonnull PluginManifest builder)`: Add description.
  - Executes `registerCorePlugin` behavior.
- `canLoadOnBoot(@Nonnull PluginManifest manifest)`: Add description.
  - Executes `canLoadOnBoot` behavior.
- `setup()`: Add description.
  - Executes `setup` behavior.
- `start()`: Add description.
  - Executes `start` behavior.
- `shutdown()`: Add description.
  - Executes `shutdown` behavior.
- `getState()`: Add description.
  - Executes `getState` behavior.
- `getBridgeClassLoader()`: Add description.
  - Executes `getBridgeClassLoader` behavior.
- `validatePluginDeps(@Nonnull PendingLoadPlugin pendingLoadPlugin, @Nullable Map<PluginIdentifier, PendingLoadPlugin> pending)`: Add description.
  - Executes `validatePluginDeps` behavior.
- `loadPluginsFromDirectory(@Nonnull Map<PluginIdentifier, PendingLoadPlugin> pending, @Nonnull Path path, boolean create, @Nonnull Map<PluginIdentifier, PluginManifest> bootRejectMap)`: Add description.
  - Executes `loadPluginsFromDirectory` behavior.
- `loadPendingJavaPlugin(@Nonnull Path file)`: Add description.
  - Executes `loadPendingJavaPlugin` behavior.
- `loadPluginsInClasspath(@Nonnull Map<PluginIdentifier, PendingLoadPlugin> pending, @Nonnull Map<PluginIdentifier, PluginManifest> rejectedBootList)`: Add description.
  - Executes `loadPluginsInClasspath` behavior.
- `getPlugins()`: Add description.
  - Executes `getPlugins` behavior.
- `getPlugin(PluginIdentifier identifier)`: Add description.
  - Executes `getPlugin` behavior.
- `hasPlugin(PluginIdentifier identifier, @Nonnull SemverRange range)`: Add description.
  - Executes `hasPlugin` behavior.
- `reload(@Nonnull PluginIdentifier identifier)`: Add description.
  - Executes `reload` behavior.
- `unload(@Nonnull PluginIdentifier identifier)`: Add description.
  - Executes `unload` behavior.
- `unloadJavaPlugin(JavaPlugin plugin)`: Add description.
  - Executes `unloadJavaPlugin` behavior.
- `load(@Nonnull PluginIdentifier identifier)`: Add description.
  - Executes `load` behavior.
- `findAndLoadPlugin(PluginIdentifier identifier)`: Add description.
  - Executes `findAndLoadPlugin` behavior.
- `findPluginInDirectory(@Nonnull PluginIdentifier identifier, @Nonnull Path modsPath)`: Add description.
  - Executes `findPluginInDirectory` behavior.
- `loadManifest(@Nonnull Path file)`: Add description.
  - Executes `loadManifest` behavior.
- `load(@Nullable PendingLoadPlugin pendingLoadPlugin)`: Add description.
  - Executes `load` behavior.
- `setup(@Nonnull PluginBase plugin)`: Add description.
  - Executes `setup` behavior.
- `start(@Nonnull PluginBase plugin)`: Add description.
  - Executes `start` behavior.
- `dependenciesMatchState(PluginBase plugin, PluginState requiredState, PluginState stage)`: Add description.
  - Executes `dependenciesMatchState` behavior.
- `loadPendingPlugin(@Nonnull Map<PluginIdentifier, PendingLoadPlugin> pending, @Nonnull PendingLoadPlugin plugin)`: Add description.
  - Executes `loadPendingPlugin` behavior.
- `getAvailablePlugins()`: Add description.
  - Executes `getAvailablePlugins` behavior.
- `getResource0(@Nonnull String name, @Nullable PluginClassLoader pluginClassLoader)`: Add description.
  - Executes `getResource0` behavior.
- `getResource0(@Nonnull String name, @Nullable PluginClassLoader pluginClassLoader, @Nonnull PluginManifest manifest)`: Add description.
  - Executes `getResource0` behavior.
- `getResources0(@Nonnull String name, @Nullable PluginClassLoader pluginClassLoader)`: Add description.
  - Executes `getResources0` behavior.
- `getResources0(@Nonnull String name, @Nullable PluginClassLoader pluginClassLoader, @Nonnull PluginManifest manifest)`: Add description.
  - Executes `getResources0` behavior.
- `tryGetResource(@Nonnull String name, @Nullable PluginClassLoader pluginClassLoader, @Nullable PluginBase pluginBase)`: Add description.
  - Executes `tryGetResource` behavior.

## Notes
- No additional notes.
