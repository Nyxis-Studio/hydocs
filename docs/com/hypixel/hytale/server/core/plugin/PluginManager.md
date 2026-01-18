# PluginManager

## Overview
- Documentation for `PluginManager`.
- Declared as a class in `com.hypixel.hytale.server.core.plugin`.

## Constructors
- `PluginManager()`
  - Creates a `PluginManager` instance.

## Methods
- `get()`
  - Executes `get` behavior.
- `registerCorePlugin(@Nonnull PluginManifest builder)`
  - Executes `registerCorePlugin` behavior.
- `canLoadOnBoot(@Nonnull PluginManifest manifest)`
  - Executes `canLoadOnBoot` behavior.
- `setup()`
  - Executes `setup` behavior.
- `start()`
  - Executes `start` behavior.
- `shutdown()`
  - Executes `shutdown` behavior.
- `getState()`
  - Executes `getState` behavior.
- `getBridgeClassLoader()`
  - Executes `getBridgeClassLoader` behavior.
- `validatePluginDeps(@Nonnull PendingLoadPlugin pendingLoadPlugin, @Nullable Map<PluginIdentifier, PendingLoadPlugin> pending)`
  - Executes `validatePluginDeps` behavior.
- `loadPluginsFromDirectory(@Nonnull Map<PluginIdentifier, PendingLoadPlugin> pending, @Nonnull Path path, boolean create, @Nonnull Map<PluginIdentifier, PluginManifest> bootRejectMap)`
  - Executes `loadPluginsFromDirectory` behavior.
- `loadPendingJavaPlugin(@Nonnull Path file)`
  - Executes `loadPendingJavaPlugin` behavior.
- `loadPluginsInClasspath(@Nonnull Map<PluginIdentifier, PendingLoadPlugin> pending, @Nonnull Map<PluginIdentifier, PluginManifest> rejectedBootList)`
  - Executes `loadPluginsInClasspath` behavior.
- `getPlugins()`
  - Executes `getPlugins` behavior.
- `getPlugin(PluginIdentifier identifier)`
  - Executes `getPlugin` behavior.
- `hasPlugin(PluginIdentifier identifier, @Nonnull SemverRange range)`
  - Executes `hasPlugin` behavior.
- `reload(@Nonnull PluginIdentifier identifier)`
  - Executes `reload` behavior.
- `unload(@Nonnull PluginIdentifier identifier)`
  - Executes `unload` behavior.
- `unloadJavaPlugin(JavaPlugin plugin)`
  - Executes `unloadJavaPlugin` behavior.
- `load(@Nonnull PluginIdentifier identifier)`
  - Executes `load` behavior.
- `findAndLoadPlugin(PluginIdentifier identifier)`
  - Executes `findAndLoadPlugin` behavior.
- `findPluginInDirectory(@Nonnull PluginIdentifier identifier, @Nonnull Path modsPath)`
  - Executes `findPluginInDirectory` behavior.
- `loadManifest(@Nonnull Path file)`
  - Executes `loadManifest` behavior.
- `load(@Nullable PendingLoadPlugin pendingLoadPlugin)`
  - Executes `load` behavior.
- `setup(@Nonnull PluginBase plugin)`
  - Executes `setup` behavior.
- `start(@Nonnull PluginBase plugin)`
  - Executes `start` behavior.
- `dependenciesMatchState(PluginBase plugin, PluginState requiredState, PluginState stage)`
  - Executes `dependenciesMatchState` behavior.
- `loadPendingPlugin(@Nonnull Map<PluginIdentifier, PendingLoadPlugin> pending, @Nonnull PendingLoadPlugin plugin)`
  - Executes `loadPendingPlugin` behavior.
- `getAvailablePlugins()`
  - Executes `getAvailablePlugins` behavior.
- `getResource0(@Nonnull String name, @Nullable PluginClassLoader pluginClassLoader)`
  - Executes `getResource0` behavior.
- `getResource0(@Nonnull String name, @Nullable PluginClassLoader pluginClassLoader, @Nonnull PluginManifest manifest)`
  - Executes `getResource0` behavior.
- `getResources0(@Nonnull String name, @Nullable PluginClassLoader pluginClassLoader)`
  - Executes `getResources0` behavior.
- `getResources0(@Nonnull String name, @Nullable PluginClassLoader pluginClassLoader, @Nonnull PluginManifest manifest)`
  - Executes `getResources0` behavior.
- `tryGetResource(@Nonnull String name, @Nullable PluginClassLoader pluginClassLoader, @Nullable PluginBase pluginBase)`
  - Executes `tryGetResource` behavior.

## Notes
- No additional notes.
