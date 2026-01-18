# PluginManifest

## Overview
- Documentation for `PluginManifest`.
- Declared as a class in `com.hypixel.hytale.common.plugin`.

## Constructors
- `PluginManifest()`
  - Creates a `PluginManifest` instance.
- `PluginManifest(@Nonnull String group, @Nonnull String name, @Nonnull Semver version, @Nullable String description, @Nonnull List<AuthorInfo> authors, @Nullable String website, @Nullable String main, @Nullable SemverRange serverVersion, @Nonnull Map<PluginIdentifier, SemverRange> dependencies, @Nonnull Map<PluginIdentifier, SemverRange> optionalDependencies, @Nonnull Map<PluginIdentifier, SemverRange> loadBefore, @Nonnull List<PluginManifest> subPlugins, boolean disabledByDefault)`
  - Creates a `PluginManifest` instance.
- `PluginManifest(this.group, this.name, this.version, this.description, Collections.emptyList()`
  - Creates a `PluginManifest` instance.

## Methods
- `getGroup()`
  - Executes `getGroup` behavior.
- `getName()`
  - Executes `getName` behavior.
- `getVersion()`
  - Executes `getVersion` behavior.
- `getDescription()`
  - Executes `getDescription` behavior.
- `getAuthors()`
  - Executes `getAuthors` behavior.
- `getWebsite()`
  - Executes `getWebsite` behavior.
- `setGroup(@Nonnull String group)`
  - Executes `setGroup` behavior.
- `setName(@Nonnull String name)`
  - Executes `setName` behavior.
- `setVersion(@Nullable Semver version)`
  - Executes `setVersion` behavior.
- `setDescription(@Nullable String description)`
  - Executes `setDescription` behavior.
- `setAuthors(@Nonnull List<AuthorInfo> authors)`
  - Executes `setAuthors` behavior.
- `setWebsite(@Nullable String website)`
  - Executes `setWebsite` behavior.
- `getMain()`
  - Executes `getMain` behavior.
- `getServerVersion()`
  - Executes `getServerVersion` behavior.
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `injectDependency(PluginIdentifier identifier, SemverRange range)`
  - Executes `injectDependency` behavior.
- `getOptionalDependencies()`
  - Executes `getOptionalDependencies` behavior.
- `getLoadBefore()`
  - Executes `getLoadBefore` behavior.
- `isDisabledByDefault()`
  - Executes `isDisabledByDefault` behavior.
- `includesAssetPack()`
  - Executes `includesAssetPack` behavior.
- `getSubPlugins()`
  - Executes `getSubPlugins` behavior.
- `inherit(@Nonnull PluginManifest manifest)`
  - Executes `inherit` behavior.
- `toString()`
  - Executes `toString` behavior.
- `corePlugin(@Nonnull Class<?> pluginClass)`
  - Executes `corePlugin` behavior.
- `description(@Nonnull String description)`
  - Executes `description` behavior.
- `depends(Class<?> ... dependencies)`
  - Executes `depends` behavior.
- `optDepends(Class<?> ... dependencies)`
  - Executes `optDepends` behavior.
- `loadsBefore(Class<?> ... plugins)`
  - Executes `loadsBefore` behavior.
- `build()`
  - Executes `build` behavior.

## Notes
- No additional notes.
